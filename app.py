
from flask import Flask
from flask import render_template
from flask import request
from clarifai.client import ClarifaiApi
import unirest
import requests, json
print 'training'
import test

app = Flask(__name__)
app = Flask(__name__, static_folder='/Users/linyufeng/Desktop/dubhacksworkshop/templates/images')
#Put code below here

def predict(url):
	result = test.clarifai.predict_all(url)
	predictions = result['urls'][0]['predictions']
	highest = ''
	highestscore = 0
	for i in range(len(predictions)):
		if predictions[i]['score'] > highestscore:
			highestscore = predictions[i]['score']
			highest = predictions[i]['cname']

	return highest

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/yoda')
def yoda():
	sentence = request.args.get('sentence')
	if sentence == "":
		translated = "You.."
	else:
		translated = translate_to_yoda(sentence)
	return render_template('yoda.html', translated = translated)

def searchRecipe(app_id, app_key, query):
	url = "https://edamam-recipe-search-and-diet-v1.p.mashape.com/search"
	payload = {"_app_id" : app_id, "_app_key" : app_key, "q" : query}
	headers = {"X-Mashape-Key" : "dRkKa9kDdHmshxbr3E7uJPGXfwHop1wYONnjsncUrpespt4zGC", "Accept" : "application/json"}
	r = requests.get(url, params=payload, headers=headers)
	response = r.json()
	recipies = []
	numRecipes = 5
	print 'lenght', len(response['hits'])
	if(len(response['hits']) < 5):
		numRecipes = len(response['hits'])
	for i in range(numRecipes):
		print 'response', response
		recipe = response['hits'][i]['recipe']
		recipies.append({'url' : recipe['shareAs'], 'label' : recipe['label'], 'image': recipe['image']})
	return recipies


def translate_to_yoda(sentence):
	clarifai_api = ClarifaiApi()
	response = test.clarifai.predict_all(sentence)#clarifai_api.tag_image_urls(sentence),

	# result = response[0]['results'][0]['result']['tag']['classes'][0]
	result = predict(sentence)
	res = searchRecipe("","", result)
	return res

@app.route('/about')
def about():
	return 'THis is a about about '

# Put code above here
if __name__ == '__main__':
    app.run(debug=True)
