import tweepy

# Importando as chaves de acesso do arquivo secrets
from secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET

# Configurando a autenticação
auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Criando uma instância da API
api = tweepy.API(auth)
# WOEID do Brasil (esse parâmetro pode não ser necessário na API v2)
BRAZIL_WOE_ID = 23424768

# Obtendo as tendências (verifique o endpoint correto para a API v2)
try:
    trends = api.get_place_trends(BRAZIL_WOE_ID)
    print(trends)
except tweepy.TweepyException as e:
    print(f"Error: {e}")

