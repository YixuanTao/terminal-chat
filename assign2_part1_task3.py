from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Load server mappings from serverMapping.json
with open('serverMapping.json', 'r') as f:
    server_mapping = json.load(f)

@app.route('/register', methods=['POST'])
def register():
    data = request.json['data']
    command = data['command']
    server_url = data['server_url']
    server_mapping[command] = server_url

    # Save updated server mappings to serverMapping.json
    with open('serverMapping.json', 'w') as f:
        json.dump(server_mapping, f)

    return jsonify(data={'command': command, 'message': 'saved'})

def forward_to_server(command, message):
    if command in server_mapping:
        server_url = server_mapping[command]
        payload = {'message': message}
        response = requests.post(server_url + '/execute', json=payload)
        return response.json()['data']['message']
    else:
        return message

@app.route('/message', methods=['POST'])
def message():
    data = request.json['data']
    message = data['message']
    command = message.split()[0][1:] # Extract command from message
    response_message = forward_to_server(command, message)
    return jsonify(data={'message': response_message})

if __name__ == '__main__':
    app.run(debug=True)
