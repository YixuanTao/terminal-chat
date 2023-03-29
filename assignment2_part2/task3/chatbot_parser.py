@app.route('/register', methods=['POST'])
def register_command():
    # logic to register commands
    pass

@app.route('/execute', methods=['POST'])
def execute_command():
    data = request.get_json()
    command = data['data']['command']
    if command == 'email':
        message = data['data']['message']
        email_address, subject, body = message.split(' ', 2)
        email_server_url = 'http://email_server:5001'
        response = requests.post(f'{email_server_url}/execute', json={
            'data': {
                'command': 'email',
                'message': [email_address, subject, body]
            }
        })
        return jsonify(response.json())
    else:
        # logic to execute other commands
        pass
