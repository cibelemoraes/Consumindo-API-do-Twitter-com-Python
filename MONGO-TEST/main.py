import tweepy
import uvicorn

from fastapi import FastAPI

from src.services import get_trends

from pydantic import BaseModel

class TrendItem(BaseModel):
   name:str
   url:str

BRAZIL_WOE_ID = 23424768
      
app = FastAPI()

@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
   
   trends = get_trends(woe_id=BRAZIL_WOE_ID)
   
   return trends

if __name__ == "__main__":
   uvicorn.run(app,host="0.0.0.0", port=8000)
   

