This is the explanation of task 3.

Steps:

1.'chatbot_parser.py':  
	add the '/email' command and its corresponding logic to parse the email address, subject, and body of the email message.  
2.'Dockerfile-email':  
	create a Dockerfile for the email server that installs the required packages and copies the 'email_server.py' file into the container.  
3.'docker-compose.yml':  
	add the email server service to the docker-compose file and link it to the postgres service.  
4.'email_server.py':  
	create a new Flask server that listens for POST requests to the '/execute' endpoint and sends an email using the SendGrid API.  
5.'requirements.txt':  
	list the required Python packages for the email server.  

