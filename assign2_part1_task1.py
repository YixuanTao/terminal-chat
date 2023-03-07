from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    request_data = request.get_json()
    command = request_data['data']['command']
    message = request_data['data']['message']
    if command == 'shrug':
        message += '¯\_(ツ)_/¯'
    response_data = {
        'data': {
            'command': command,
            'message': message
        }
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(port=5001)
