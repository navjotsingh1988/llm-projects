# AskMyPDF (LangChain + Amazon Bedrock)
```
This AI assistant helps you interact with PDF documents locally using Amazon Bedrock — without uploading them to any external server.

It supports two main use cases:
✅ Summarize PDF documents — e.g., bank statements, receipts, manuals.
🔍 Answer questions from PDFs — ask about specific content inside, like "What’s my closing balance?" or "How does this product work?"

Common real-world examples:
📄 Bank statements — Quickly summarize your monthly account summary.
📘 User manuals — Ask questions like "How do I reset the device?" without reading the whole thing.
📕 Study material — Extract key takeaways from long chapters or academic PDFs.
```

## How It Works:
```
- Classifies the user's intent using Amazon Bedrock (Summary or Q/A)
- Responds based on the user's intent using extracted PDF text
```

## Project Structure
```
  ├── main.py            # Entry point for the assistant
  ├── prompts.py         # Prompt templates for intent classification and responses
  ├── .env               # Stores environment variables
```

## Requirements:
```
  - Python3
  - AWS credentials with access to:
    - Bedrock
  - A PDF File
  - pip install the following:
    - langchain
    - PyPDF2 or any preferred PDF parser
```
### Setup Instructions
```
  1. Install dependencies
  2. Configure the `.env` file
  3. Get the pdf file path
  4. Run the assistant with `python3 main.py`
```
