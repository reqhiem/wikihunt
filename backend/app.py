from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.search import search_engine

# Create a Flask app instance
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


# Define a route for the root URL
@app.route("/")
def hello_world():
    return "Hello, World!"


# Define a route for a custom endpoint
@app.route("/api/search", methods=["GET"])
def search():
    # Get the 'query' parameter from the request URL
    query = request.args.get("query", "")
    results = search_engine(query)
    data = {"status": "OK", "results": results, "length": len(results)}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
