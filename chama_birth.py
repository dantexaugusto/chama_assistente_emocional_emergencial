from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("behaviour_prompt.txt", "r") as bPrompt:
    behaviour_prompt = bPrompt.read()

user_prompt = input("Digite o prompt: \n",)

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "developer",
            "content": behaviour_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]
)

print(response.output_text)


