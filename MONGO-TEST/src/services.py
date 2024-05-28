from typing import Any, Dict, List
import tweepy
from src.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from src.constants import BRAZIL_WOE_ID
from src.constants trends_collection



def _get_trends(woe_id: int)-> List[Dict[str, Any]]:
    """ Get treending topics.
    Args:
    woe_id (int): Identifier of location.
    Return:
    List[Dict[str, Any]]: Trends list."""
    
   # Configurando a autenticação
   auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
   auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

   # Criando uma instância da API
   api = tweepy.API(auth)
   # WOEID do Brasil (esse parâmetro pode não ser necessário na API v2)
   BRAZIL_WOE_ID = 23424768

   # Obtendo as tendências (verifique o endpoint correto para a API v2)
   try:
      trends = api.get_place_trends(woe_id)
      print(trends)
   except tweepy.TweepyException as e:
      print(f"Error: {e}")
      
def get_trends_from_mongo()-> List[Dict[str, Any]]:
    trends = trends_collection.find({})
    return list(trends)

def save_trends()-> None:
    
   trends = _get_trends(woe_id=BRAZIL_WOE_ID)
   trends_collection.insert_many(trends)
   