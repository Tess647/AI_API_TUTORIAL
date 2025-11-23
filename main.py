import os
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import prompts

# load the .env variables
load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)

model = 'gpt-4.1'
temperature = 0.3
max_tokens = 500
topic = "money"

# read the PDF file
book = ""
file_path = "naval.pdf"
with open(file_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)
    start_page = 23
    end_page = total_pages - 30

    for page_num in range(start_page, end_page):
        page = reader.pages[page_num]
        book += page.extract_text() + " "

    #print(book)

# prompts
system_message = prompts.system_message
prompt = prompts.generate_prompt(book, topic)

messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]

# helper function
def generate_response():
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

print("Generating response...")
print(generate_response())