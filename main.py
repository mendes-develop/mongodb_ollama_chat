from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from pymongo import MongoClient
# from mongo.connection import USER
from mongo.business import Business

import ollama
import os

import bson

load_dotenv()
app = FastAPI()

debug_mode = os.getenv("DEBUG", False)  # Default to False if not set
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# print(debug_mode, MONGO_URI, DB_NAME)

if not MONGO_URI and not DB_NAME and not MongoClient:
    raise Exception("MONGO_URI not set")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
Business_Connection = db["Business"]

@app.get("/")
def read_root():
    # names = db.list_collection_names()    
    businesses = Business_Connection.find({})
    
    # print(business)
    
    # business.name = "Ollama - Point da Jo"
    # business.save()
    
    # print(business["name"])
    
    # found_business = Business(**business)
    
    # print(found_business.__str__())
    
    # business["name"] = "Ollama - Point da Jo"
    # business.save()
    # print(business["name"])
    response = []
    for business in businesses:
        if 'name' in business:
            print(business)            
            print("Run ollama embedding here")
            
        found_business = Business(**business)
        response.append(found_business.__str__())
        
        embedding = ollama.embeddings(
        model='llama3',
        prompt=found_business.__str__(), )
        
        print(embedding['embedding'])
       
        Business_Connection.find_one_and_update(
        {"_id": bson.ObjectId(business["_id"])},
        {"$set": {"embeding": embedding['embedding']}},)
    
    
    return {"response": response}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    print(q)
    if not q:
        raise Exception(f"Query parameter 'q' is required")
    
    # embedding_response = ollama.embeddings(
    # model='llama3',
    # prompt=q)
    
    business_found = Business_Connection.aggregate([
        {
            # "$vectorSearch": {
            #     "queryVector": embedding_response['embedding'],
            #     "path": "embeding",
            #     "limit": 2,
            #     "index": "businessIndex",
            #     "numCandidates": 10,
            # },
            #  {
                "$search": {
                "index": "businessIndex",
                "text": {
                    "query": q,
                    "path": {
                    "wildcard": "*"
                    }
                }
                }
  
            
        },
        {
                "$project": {
                    "_id": 0,
                    "name": 1,
                    "description": 1,
                    "picture": 1,
                }
            }
    ])

    print(business_found)
    
    
    response = []
    for document in business_found:
        print(document['name'])
        response.append(document)
    
    print(list(business_found))
    
    context = response.__str__()
    
    response = ollama.chat(
        model='llama3',
        messages=[{
            "role": "user",
            "content": f"We are Fasto, a web POS system and we are responding answers from customers with the following context: {context} \n Question: {q}",
        }]
        # prompt=q,
        # length=100,
        # temperature=0.9,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0,
        # stop=["\n"]
    )
    
    # response = ollama.chat(model='llama3', messages=[{
    #     'role': 'user',
    #     'content': 'Why is the sky blue?',
    # }])
    print(response['message']['content'])
    
    return {"pergunta": q, "business_found": response['message']['content']}
  