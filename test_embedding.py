import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

model_name = "text-embedding-ada-002"

 
client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = "2024-02-01",
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT") 
)

response = client.embeddings.create(
    input = "Your text string goes here",
    model= model_name
)

print(response.model_dump_json(indent=2))
