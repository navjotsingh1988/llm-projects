import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("REGION")

# -- MODEL_ID defines the Amazon Bedrock model used for content moderation --
MODEL_ID = os.getenv("BEDROCK_MODEL_ID")

# -- TABLE specifies the name of the DynamoDB table where results will be stored --
TABLE = os.getenv("DYNAMODB_TABLE")
