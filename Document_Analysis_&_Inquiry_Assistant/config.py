import os
from dotenv import load_dotenv

load_dotenv()

MODEL_ID = os.getenv("BEDROCK_MODEL_ID")
AWS_REGION = os.getenv("REGION")
