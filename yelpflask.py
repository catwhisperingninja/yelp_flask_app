from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import json
import pprint
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# function to take in one Yelp search term, one city/state, and then return the top 3 results

# def sort_by_rating(businesses_in_city):
# 	top_rated_list = []
# 	for b in businesses_in_city:
# 		if b['rating'] >= 4:
# 			top_rated_list.append(b)
# 	return top_rated_list

# print(rating_sorted_businesses)

def get_term_location(term, location):
	auth = Oauth1Authenticator(
	consumer_key=os.environ['YELP_CONSUMER_KEY'],
	consumer_secret=os.environ['YELP_CONSUMER_SECRET'],
	token=os.environ['YELP_TOKEN'],
	token_secret=os.environ['YELP_TOKEN_SECRET']
)
	client = Client(auth)
	params = {'term': term, 'lang': 'en'}
	businesses = []
	response = client.search(location, **params)
	for business in response.businesses:
		businesses.append({"name": business.name, 
			"rating": business.rating,
			"address": business.location.address
		})
	return businesses[:3]

# businesses_in_city = get_term_location("food", "Los Angeles CA")

# print(json.dumps(businesses_in_city, indent=2))






