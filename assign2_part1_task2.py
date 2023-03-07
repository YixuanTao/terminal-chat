from flask import Flask, request, jsonify

app = Flask(__name__)

registered_commands = {}

@app.route('/message', methods=['POST'])
def parse_message():
    message = request.json['message']
    command = None
    if message.startswith('/'):
        command, message = message[1:].split(' ', 1)
    return jsonify({'command': command, 'message': message})

@app.route('/register', methods=['POST'])
def register_command():
    data = request.json['data']
    command = data['command']
    server_url = data['server_url']
    registered_commands[command] = server_url
    return jsonify({'data': {'command': command, 'message': 'saved'}})

if __name__ == '__main__':
    app.run()
