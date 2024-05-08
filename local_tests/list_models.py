import setupenv



import llmprototyping as llmp

print('chat completion models:')
for model_name in llmp.LLMChatCompletionFactory.available_models:
    print(f"  {model_name}")

print('embedding models:')
for model_name in llmp.EmbeddingComputerFactory.available_models:
    print(f"  {model_name}")