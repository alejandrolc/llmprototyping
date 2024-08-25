# Changelog

## 0.1.0.dev6 2024-08-25 (wip)

Added groq llama 3.1 70b and 8b models and gemma2 9b model
Added openai gpt-4o-mini

Templates: added support for comments: "##" at the start of the line 

Anthropic llm response is a list of TypedDicts, that is not serializable directly. Fixed to return a json list.

Other bugfixes and additions

## 0.1.0.dev5 2024-05-14

LLMException renamed to LLMPException
LLMChatCompletionCache
Template, TemplateFileRepository
Response objects now Serializable
OpenAI gpt-4o (only text)
Anthropic Claude 3 models (only text)

## 0.1.0.dev4 2024-05-09

added ollama chat and embeddings

## 0.1.0.dev3 2024-05-08

standardized model names to all-lowercase
added extra examples

## 0.1.0.dev2 2024-05-08

Remove unneded file
Added changelog
Updated README.md

## 0.1.0.dev1 2024-05-08

First commit

chat completion models:
  groq/Llama3-70b-8192
  groq/Llama3-8b-8192
  groq/Mixtral-8x7b-32768
  groq/Gemma-7b-It
  openai/gpt-4-turbo
  openai/gpt-4-turbo-preview
  openai/gpt-3.5-turbo

embedding models:
  openai/text-embedding-3-small
  openai/text-embedding-3-large
  openai/text-embedding-ada-002

faiss vector db
