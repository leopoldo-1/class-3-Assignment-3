from flask import Flask
import json
from mock_data import mock_catalog

#server. its the name
app = Flask('server')

@app.route("/home") #decorator
def home():
    return "Hello there!!"

@app.route("/") #decorator
def root():
    return "Welcome to the online store server"

########################################################
###################  API  CATALOG  #####################
########################################################

@app.route("/api/about", methods=["POST"])
def about():
  me = {
    "first_name": "Leo",
    "last_name": "Miranda"
  }

  return json.dumps(me)
# -------------------------------

@app.route("/api/catalog")
def get_catalog():
  return json.dumps(mock_catalog)
# -------------------------------

@app.route("/api/catalog/cheapest")
def get_cheapest():
  cheapest = mock_catalog[0]

  for product in mock_catalog:
    if(product["price"] < cheapest["price"]):
      cheapest = product

  return json.dumps(cheapest)
  # return(f"The cheapest product is: {cheapest['title']} - Price: ${cheapest['price']}")

@app.route("/api/catalog/sum")
def get_sum_all_products():

  total = 0

  for product in mock_catalog:
    total += product["price"]

  return (f"the total is: {total} ")

#start the server
app.run(debug=True)