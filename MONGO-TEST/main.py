import tweepy
import uvicorn
from typing import Any, Dict, List
from fastapi import FastAPI

from src.services import get_trends
from src.services import TrendItem, get_trends_from_mongo, save_trends

from pydantic import BaseModel

from pymongo import MongoClient



print(list(tweets))

      
app = FastAPI()

@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
    return get_trends_from_mongo

if __name__ == "__main__":
   save_trends()

   uvicorn.run(app,host="0.0.0.0", port=8000)
   

