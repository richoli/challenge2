from flask import Flask, request, jsonify
import requests

app = Flask()
REMOTE_API = "http://149.165.150.300"

# Local endpoint
@app.route('/api/local/data', methods=['GET'])
def local_data():
    # Process locally
    data = {"source": "local", "result": "some data"}
    return jsonify(data)

# Proxy to remote endpoint
@app.route('/api/remote', methods=['GET'])
def remote_data():
    # Forward request to remote API
    response = requests.get(f"{REMOTE_API}/data")
    return jsonify(response.json())

# You can also merge data from both sources
@app.route('/api/combined/data', methods=['GET'])
def combined_data():
    # Get local data
    local_result = {"local_value": 123}
    
    # Get remote data
    remote_response = requests.get(f"{REMOTE_API}/data")
    remote_result = remote_response.json()
    
    # Combine results
    combined = {
        "local": local_result,
        "remote": remote_result
    }
    
    return jsonify(combined)