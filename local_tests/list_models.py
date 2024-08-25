import setupenv



import llmprototyping as llmp

#llmp.ollama_discover(host='http://192.168.1.13:11434')

print('chat completion models:')
for model_name in llmp.LLMChatCompletionFactory.available_models:
    print(f"  {model_name}")

print('embedding models:')
for model_name in llmp.EmbeddingComputerFactory.available_models:
    print(f"  {model_name}")

