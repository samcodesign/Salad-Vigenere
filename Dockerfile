FROM python:3.7

ADD . . 

EXPOSE 8080

CMD [ "python", "/letues_socket.py" ]
