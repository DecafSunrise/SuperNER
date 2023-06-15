FROM python:3.9-slim

EXPOSE 5000
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt


COPY . ./
CMD flask run -h 0.0.0.0 -p 5000