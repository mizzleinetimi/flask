import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True



#store inventory
shop_inventory = [{'id':0,'item': 'bread',
'price':50,
'quantity':400,
}, {'id':1, 'item':'tea' , 'price':100, 'quantity':100},{'id':2,'item':'rice' , 'price': 50, 'quantity': 100}]


@app.route('/', methods=['GET'])
def home():
    return "<h1>shop inventory app</h1><p>This site is a prototype API for a shop inventory.</p>"


# a route to shop inventory entries
@app.route('/api/v1/resources/shop_inventory/all', methods=['GET'])
def api_all():
    return jsonify(shop_inventory)    



@app.route('/api/v1/resources/shop_inventory', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for item in shop_inventory:
        if item['id'] == id:
            results.append(item)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)



   

app.run()
