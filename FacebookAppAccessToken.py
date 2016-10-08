import facebook
import requests

#facebook_graph = facebook.GraphAPI(oauth_access_token)

payload = {'grant_type': 'client_credentials', 'client_id': '1776695622588995', 'client_secret': 'acb46fc76c6eab0b907c62c2ca8ff66d'}

file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
access_token = file.text.split("=")[1]
print (access_token)
graph = facebook.GraphAPI(access_token=access_token, version='2.2')
print (graph)
