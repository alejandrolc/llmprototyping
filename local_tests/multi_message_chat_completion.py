import setupenv



import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

import llmprototyping as llmp
factory = llmp.LLMChatCompletionFactory
model = factory.build('groq/llama-3.1-8b-instant', {'api_key': groq_api_key})
#model = factory.build('openai/gpt-4o-mini', {'api_key': openai_api_key})
user_msg = llmp.Message(content="Please give me a list of ten colours and some place that is related to each one.")
sys_msg = llmp.Message(content="Provide an answer in json", role="system")
resp = model.query([user_msg,sys_msg], json_response=True, temperature=0)
resp.show()