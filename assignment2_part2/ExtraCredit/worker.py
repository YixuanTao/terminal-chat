import os
import time
import json
import redis
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = os.environ.get("REDIS_PORT", 6379)
redis_db = os.environ.get("REDIS_DB", 0)
redis_password = os.environ.get("REDIS_PASSWORD", None)

redis_conn = redis.Redis(
    host=redis_host, port=redis_port, db=redis_db, password=redis_password
)

while True:
    # Get message from Redis queue
    _, message = redis_conn.blpop("email_queue")

    # Parse message
    message = json.loads(message)

    # Send email
    to_email, subject, body = message["data"]["message"]
    message = Mail(from_email="example@example.com", to_emails=to_email, subject=subject, plain_text_content=body)
    sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)

    # Print confirmation message
    print(f"Sent email to {to_email} with subject {subject} and body {body}")

    # Sleep for a second to avoid overloading the Redis queue
    time.sleep(1)
