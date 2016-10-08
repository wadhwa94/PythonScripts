# coding: utf-8

import facebook
import requests
access_token = 'EAACEdEose0cBAAXlX3j0GS4TGacgGsyadWLnd0LUroNjiHkZAcWkrsqZBidQumJZCM9lYjxLYNrm9WldhdY4r1cY5xZCAWyrRysnTqytZCI7OmDCTrHpTJSmlMwWPGgxV2EBX2SJLmas6KUe6MhVtiY6qJP4vwfmgnehpZCUKPAe3SAZDZD';
#access token got from API explorer temporary
graph = facebook.GraphAPI(access_token=access_token, version='2.2')
print (graph)
friends = graph.get_connections(id='me', connection_name='friends')
#print (friends)
allfriends = []
while(True):
    try:
        for friend in friends['data']:
            allfriends.append(friend['name'].encode('utf-8'))
        # Attempt to make a request to the next page of data, if it exists.
        friends=requests.get(friends['paging']['next']).json()
        print ('inside Try')
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        print ('Inside Exception')
        break
print (allfriends)
#Only friends who installed this app are returned in API v2.0 and higher. total_count in summary represents the total number of friends, including those who haven't installed the app
