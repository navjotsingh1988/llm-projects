from utils import extract_text_from_pdf
from config import MODEL_ID, AWS_REGION
from prompts import intent_classification_prompt, answer_prompt, summarize_prompt
from langchain_aws import ChatBedrock

client = ChatBedrock(model_id = MODEL_ID, region_name = AWS_REGION)

def classify_intent(query):
    response = client.invoke(intent_classification_prompt(query))
    return response

def main():
    print("\n")
    print("Welcome to the Document Analysis & Inquiry Assistant")
    pdf_path = input("Please enter the local file path of the document you wish to analyze: ")
    pdf_text = extract_text_from_pdf(pdf_path)

    if not pdf_text:
        print("Sorry !! Failed to extract text from the document.")
        return

    print("\nGreat news! Your document is now at your fingertips.\nI've analyzed its contents and I'm ready to be your personal document expert. \nWhat would you like to uncover? Whether it's key points, specific details, or general insights, I'm here to assist.\nLet's explore your document together.\nFeel free to type 'exit' when you're ready to conclude our session.")

    while True:
        print("\n")
        user_input = input("Question: ")
        if user_input.lower() == 'exit':
            break

        intent = classify_intent(user_input)

        if intent == "summary":
            response = client.invoke(summarize_prompt(pdf_text))
            result = response.content.strip()
        else:
            response = client.invoke(answer_prompt(pdf_text, user_input))
            result = response.content.strip()

        print("Answer:", result)

if __name__ == "__main__":
    main()
