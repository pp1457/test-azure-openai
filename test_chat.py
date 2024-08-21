import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

model_name = "gpt-4o-mini"
 
client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = "2024-02-01",
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT") 
)

completion = client.chat.completions.create(
    model=model_name,
    messages=[{"role": "user",
        "content": "What is AI?",
    },],
)

print(completion.choices[0].message.content)



