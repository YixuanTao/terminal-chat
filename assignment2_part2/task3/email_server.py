from flask import Flask, jsonify, request
import sendgrid
from sendgrid.helpers.mail import Mail
import os

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_email():
    data = request.get_json()
    email_address, subject, body = data['data']['message']
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    message = Mail(
        from_email='example@example.com',
        to_emails=email_address,
        subject=subject,
        plain_text_content=body
    )
    try:
        response = sg.send(message)
        return jsonify({
            'data': {
                'command': 'email',
                'message': 'Email was sent'
            }
        })
    except Exception as e:
        return jsonify({
            'data': {
                'command': 'email',
                'message': 'Error sending email'
            }
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
