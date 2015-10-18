#instantiate a new Clarifai object
from clarifai_basic import ClarifaiCustomModel
clarifai = ClarifaiCustomModel()

# Give a few positive examples and a name for the custom concept.
clarifai.positive('https://upload.wikimedia.org/wikipedia/commons/0/02/Durian.jpg', 'durian')
clarifai.positive('https://www.organicfacts.net/wp-content/uploads/2013/05/Banana21.jpg', 'banana')
clarifai.positive('http://thumbs.dreamstime.com/z/sweet-sop-2898990.jpg', 'sweetsop')
clarifai.positive('http://www.centraliowaminiclub.org/wp-content/uploads/2015/08/pie.jpg', 'pie')
clarifai.positive('http://media.mercola.com/assets/images/food-facts/lychee-nutrition-facts.jpg', 'lychee')


# Give a few negative examples and a name for the custom concept.
clarifai.negative('https://www.organicfacts.net/wp-content/uploads/2013/05/Banana21.jpg', 'durian')
clarifai.negative('https://upload.wikimedia.org/wikipedia/commons/0/02/Durian.jpg', 'banana')
clarifai.negative('http://dreamatico.com/data_images/apple/apple-7.jpg', 'sweetsop')
clarifai.negative('https://upload.wikimedia.org/wikipedia/commons/8/8f/NYC-Diner-Bacon-Cheeseburger.jpg', 'pie')
clarifai.negative('http://www.newhealthguide.org/images/10415496/image001.jpg', 'lychee')


# Train the platform to learn your custom concept.
clarifai.train('durian')
clarifai.train('pie')
clarifai.train('banana')
clarifai.train('sweetsop')
clarifai.train('lychee')
