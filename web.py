from flask import Flask, render_template, request
import yelpflask
import os
app = Flask(__name__)
# app = Flask()

#Github link for this project: https://github.com/catwhisperingninja/yelp_flask_app
#Heroku link for this project: https://quiet-peak-64273.herokuapp.com/

@app.route("/")
def index():
	term = request.values.get('term')
	address = request.values.get('address') # returns dict with any params passed to it (? in url)
	businesses = None # this fixes the server error you'll get by not defining forecast 1st
	if term and address:
		businesses = yelpflask.get_term_location(term, address) # add the filename.function to call an import
	return render_template('index.html', businesses=businesses)

# @app.route('/about')
# def about():
# 	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)