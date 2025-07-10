import json
import boto3
from config import MODEL_ID, AWS_REGION
from boto3.dynamodb.types import TypeSerializer
from prompts import invoke_bedrock, content_classification
from utils import parse_event, parse_messages, fetch_content, upload_to_dynamodb

# --- AWS Clients ---
s3_client = boto3.client("s3")
bedrock_client = boto3.client("bedrock-runtime", region_name = AWS_REGION)
dynamodb_client = boto3.client("dynamodb")

def lambda_handler(event, context):
    """
    Entry point for the Lambda function.
    """
    # Step 1: Parse the event from SQS
    messages = parse_event(event)
    # Step 2: Parse S3 object information
    objects = parse_messages(messages)
    # Step 3: Fetch the content of S3 objects
    objects = fetch_content(objects)
    # Step 4: Classify the content using Amazon Bedrock
    classified_messages = content_classification(objects)
    # Step 5: Upload the results to DynamoDB
    upload_to_dynamodb(classified_messages)

    return {
        "statusCode": 200,
        "body": json.dumps(f"{len(classified_messages)} messages processed"),
    }
