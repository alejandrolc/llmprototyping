import setupenv



import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

import llmprototyping as llmp
factory = llmp.LLMChatCompletionFactory
model = factory.build('groq/llama3-70b-8192', {'api_key': groq_api_key})
msg = llmp.Message(content="De qué color es el caballo blanco de Santiago? Responde en json.")
resp = model.query([msg], json_response=True, temperature=0)
resp.show()