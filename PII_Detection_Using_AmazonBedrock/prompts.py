PII_PROMPT_TEMPLATE = """
You are a content moderation assistant. Your task is to analyze the following log message and determine whether it contains any Personally Identifiable Information (PII), such as names, email addresses, phone numbers, Social Security Numbers, credit card numbers, or similar sensitive data.
Does the following log message contain sensitive or private information?

MESSAGE

Respond with either True or False.
"""

# Analyzing each message for spam and personal information (PII) using Amazon Bedrock.
def invoke_bedrock(prompt):
    """
    Sends a prompt to the Amazon Bedrock model and returns the response.
    """
    system = [{"text": "You are a content moderation bot that responds only with True or False."}]
    messages = [
        {"role": "user", "content": [{"text": prompt}]}
    ]
    response = bedrock_client.converse(modelId=MODEL_ID, messages=messages)
    return response["output"]["message"]["content"][0]["text"].strip()

def content_classification(messages):
    """
    Classifies the content using Amazon Bedrock for PII detection.
    """
    for message in messages:
        # PII classification
        message["pii"] = False
        prompt = PII_PROMPT_TEMPLATE.replace("MESSAGE", message["message"])
        response = invoke_bedrock(prompt)
        if "true" in response.lower():
            message["pii"] = True

    return messages
