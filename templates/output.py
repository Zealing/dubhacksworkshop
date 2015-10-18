import requests, json

def searchRecipe(app_id, app_key, query):
	url = "https://edamam-recipe-search-and-diet-v1.p.mashape.com/search"
	payload = {"_app_id" : app_id, "_app_key" : app_key, "q" : query}
	headers = {"X-Mashape-Key" : "dRkKa9kDdHmshxbr3E7uJPGXfwHop1wYONnjsncUrpespt4zGC", "Accept" : "application/json"}
	r = requests.get(url, params=payload, headers=headers)
	response = r.json()
	# first_recipe = response['hits'][0]
	# calories = 
	json.dumps(response['hits'][0], separators=(',',': '), indent=4)

searchRecipe("","", "banana")