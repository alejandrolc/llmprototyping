import setupenv



facts = """
Rome was founded in 753 BCE according to tradition, by Romulus and Remus.
The Roman Republic was established in 509 BCE after overthrowing the last Etruscan kings.
Julius Caesar became the perpetual dictator in 44 BCE, shortly before his assassination.
The Roman Empire officially began when Octavian received the title of Augustus in 27 BCE.
At its peak, the Roman Empire extended from Hispania to Mesopotamia.
The capital of the Empire was moved to Constantinople by Constantine I in 330.
The fall of Rome occurred in 476 CE when the last Western Roman emperor, Romulus Augustulus, was deposed.
Roman culture greatly influenced law, politics, language, and architecture in the Western world.
The expansion of Christianity as the official religion was promoted by Constantine after the Battle of the Milvian Bridge in 312.
Roman society was heavily stratified between patricians, plebeians, and slaves.
"""

question = "¿Cuáles fueron las principales contribuciones de la ingeniería romana al desarrollo urbano?"
question = "¿Cuándo se fundó el Imperio Romano?"

import sys
sys.path.append('../../my_github/llmtoolkit/src')

import os
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

import llmprototyping as llmp

import shelve
db = shelve.open('test_embeddings.db')

def get_embedding(text, computer):
    if text in db:
        json = db[text]
        return llmp.EmbeddingVector.from_json(json)

    print(f'computing embedding for {text}')
    em = computer.get_embedding(text)
    db[text] = em.to_json()

    return em

factory = llmp.EmbeddingComputerFactory
computer = factory.build('openai/text-embedding-3-small', {'api_key': openai_api_key})        

fact_text = dict()
fact_vector = dict()
i = 0

for fact in facts.split('\n'):
    fact = fact.strip()
    if not fact: continue
    em = get_embedding(fact, computer)
    fact_vector[i] = em
    fact_text[i] = fact
    i += 1

qem = get_embedding(question, computer)

vdb = llmp.FAISSDatabase(embedding_type=computer.model_name, embedding_size=computer.vector_size)
vdb.put_records(fact_vector)

print(f"query: {question}")
results = vdb.search(qem)
for dist, i in results:
    print(f"{dist} {i} {fact_text[i]}")