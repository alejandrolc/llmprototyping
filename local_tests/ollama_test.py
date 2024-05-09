import setupenv



import os
from dotenv import load_dotenv
load_dotenv()

ollama_host = os.getenv('OLLAMA_HOST')

import llmprototyping as llmp

llmp.ollama_discover(host=ollama_host)
llmp.ollama_pull_model(host=ollama_host, model_name='phi3')

print('chat completion models:')
for model_name in llmp.LLMChatCompletionFactory.available_models:
    print(f"  {model_name}")
print('embedding models:')
for model_name in llmp.EmbeddingComputerFactory.available_models:
    print(f"  {model_name}")
print()

factory = llmp.LLMChatCompletionFactory
model = factory.build('ollama/phi3')
user_msg = llmp.Message(content="Please give me a list of ten colours and some place that is related to each one.")
sys_msg = llmp.Message(content="Provide an answer in json", role="system")
resp = model.query([user_msg,sys_msg], json_response=True, temperature=0)

resp.show_header()
print(resp.message.content)
