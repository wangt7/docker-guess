#Use Python as base image
FROM python:3.9

#Set working directory
WORKDIR /app

#Install SQLite
RUN apt-get update && apt-get install -y sqlite3

#Copy local files
COPY app.py /app/
COPY test_game.py /app/

#install pytest
RUN pip install pytest

#Install SQLite database volumn
VOLUME /app/data

#run app.py using python
CMD [ "python", "app.py" ]


