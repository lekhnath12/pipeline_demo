FROM python:3.7-alpine 
RUN pip3 install flask
COPY app.py /
COPY index.html /
CMD [ "python", "./app.py" ]
