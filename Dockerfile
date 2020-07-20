FROM python:3.8-slim-buster
# copy requirements into container and install them
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
# create a directory for the model-server and set it to the workdir
RUN mkdir /model-service
WORKDIR /model-service
# copy application code into the container
COPY ./src ./src
COPY ./app.py ./app.py
# copy entrypoint script and make it executable
COPY ./scripts/start.sh ./start.sh
RUN chmod +x ./start.sh
# set the entrypoint as gunicorn, using the wsgi
ENTRYPOINT [ "./start.sh" ]
