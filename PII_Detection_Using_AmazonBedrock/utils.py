# -- Processing the messages from an AWS SQS event --
'''
The parse_event function extracts message details from an SQS event triggered
by EventBridge. It iterates through the Records array, parses each record’s
JSON body, and retrieves the detail field. These details are collected into a
list and returned for further processing.
'''
def parse_event(event):
    """
    Parses the SQS event from EventBridge to extract message details.
    """
    messages = []
    for record in event.get("Records", []):  # SQS sends records in an array
        # Parse SQS message body
        body = json.loads(record.get("body", "{}"))
        # EventBridge sends its payload as "detail" inside the body
        detail = body.get("detail", {})
        messages.append(detail)
    return messages

'''
The parse_messages function further processes the messages to find S3 objects
related to each message. It filters for events where the reason is
PutObject and extracts each message’s bucket name and object key (file ID).
'''
def parse_messages(messages):
    """
    Extracts S3 bucket and object details from EventBridge messages.
    """
    objects = []
    for message in messages:
        # EventBridge "PutObject" event details
        if message.get("reason", "") != "PutObject":
            continue

        bucket = message.get("bucket", {}).get("name")
        message_id = message.get("object", {}).get("key")

        if bucket and message_id:  # Ensure bucket and key exist
            objects.append({"bucket": bucket, "id": message_id})
    return objects

'''
The fetch_content function retrieves content from S3 using the extracted bucket name and
object key, reads and decodes the content, then adds the decoded message to each object.
'''
def fetch_content(objects):
    """
    Fetches the content of S3 objects specified in the EventBridge messages.
    """
    for s3_object in objects:
        response = s3_client.get_object(Bucket=s3_object["bucket"], Key=s3_object["id"])
        body = response.get("Body", "").read().decode("utf-8")
        s3_object["message"] = body
    return objects

# storing the analyzed results in a DynamoDB table.
def upload_to_dynamodb(messages):
    """
    Uploads classified messages to DynamoDB.
    """
    serializer = TypeSerializer()
    for message in messages:
        item = {key: serializer.serialize(value) for key, value in message.items()}
        dynamodb_client.put_item(Item=item, TableName=DYNAMODB_TABLE)
