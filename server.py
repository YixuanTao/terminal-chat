#!/usr/bin/env python
# coding: utf-8

# In[9]:


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def parse_message():
    input_message = request.get_json()['data']['message']
    if input_message.startswith('/'):
        command, message = input_message.split(' ', 1)
        command = command[1:]
    else:
        command = None
        message = input_message
    output = {'command': command, 'message': message}
    return jsonify({'data': output})

if __name__ == '__main__':
    app.run()
