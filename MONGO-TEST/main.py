import tweepy
import uvicorn
from typing import Any, Dict, List
from fastapi import FastAPI

from src.services import get_trends

from pydantic import BaseModel

from pymongo import MongoClient

cliente = MongoClient("mongodb://dio:dio@localhost:27017/")
#criando documento no pymongo
db = client.my_test

tweets_collection = db.tweets


print(list(tweets))

class TrendItem(BaseModel):
   name:str
   url:str

BRAZIL_WOE_ID = 23424768
      
app = FastAPI()

@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
   
   trends = tweets_collection.find({})
   
   return trends[0]["trends"]

if __name__ == "__main__":
   
   trends = get_trends(woe_id=BRAZIL_WOE_ID)
   
   tweets_collection.insert_many(trends)
   
   uvicorn.run(app,host="0.0.0.0", port=8000)
   

