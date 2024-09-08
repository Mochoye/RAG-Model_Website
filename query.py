import argparse
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()

CHROMA_PATH = "chroma"

# Flexible prompt template for different types of brainstorming
PROMPT_TEMPLATE = """
Based on the following context, {task}:

{context}
"""

def main():
    # Retrieve OpenAI API key from the environment variable
    openai_api_key = os.getenv("OPENAI_API_KEY")
    embedding_function = OpenAIEmbeddings(openai_api_key=openai_api_key)

    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query or brainstorming task.")
    args = parser.parse_args()
    query_text = args.query_text

    # Prepare the Chroma DB
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB for relevant context based on the query
    results = db.similarity_search_with_relevance_scores(query_text, k=1)
    if len(results) == 0 or results[0][1] < 0.7:
        print(f"Unable to find matching results.")
        return

    # Extract the context from the top results
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

    # Prompt template to format the brainstorming task
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    # Replace "{task}" with the actual query, which could be anything from generating questions to brainstorming ideas
    prompt = prompt_template.format(task=query_text, context=context_text)
    
    # Print the final prompt being sent to the model (for debugging)
    print(f"Generated Prompt: {prompt}")

    # Call the AI model (ChatOpenAI) to generate the brainstorming response
    model = ChatOpenAI()
    response_text = model.predict(prompt)

    # Display sources of information used
    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    
    # Print the response for brainstorming
    print(formatted_response)

if __name__ == "__main__":
    main()
