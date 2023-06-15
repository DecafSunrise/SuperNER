FROM python:3.9-slim

EXPOSE 5000
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN python3 -m spacy download en_core_web_sm

COPY . ./
CMD flask run -h 0.0.0.0 -p 5000