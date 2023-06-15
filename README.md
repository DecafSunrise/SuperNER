# SuperNER
![image](https://github.com/DecafSunrise/SuperNER/assets/36832027/da945878-5534-4be6-a2b8-133a63947e70)

Named Entity Recognition (NER) is a super powerful, cool NLP technique to identiy **People, Places, and Things** in free text. The downside is that these models aren't always perfect. To get around that, we can set up an *ensemble* of weak predictors to create a stronger predictor.  

More specifically, I've created API endpoints for SpaCy NER and Flair NER that you can easily bash raw text against, to start building a more structured corpus of data.

## Build the Dockerfile
In a terminal,
1. Clone this repo
2. Type `docker build -t superner:0.1 .`
3. Wait for it to finish (go get some coffee)

## Running your dockerized NER solution:
In that same terminal, type `docker run -p 5000:5000 superner:0.1`
- Flair will download it's `ner-fast` model after the container starts for the first time. It's about 250mb, and should take under a minute on a fast connection.

## Using the server
Fire off a request at `<ip>:5000/<method>`. The `ip` will be the IP of your machine running the docker container (probably `127.0.0.1`), and the `method` can be `spacy` or `flair`.
- SpaCy is faster, but does not include a confidence score for NER hits
- Flair is slower, but returns a confidence score
- Each NER variant has different tags for types of entities. Most of them are simple (Person, Location, etc), but there are some edge cases. SpaCy grabs dates and numbers; Flair seems to have more modern training data (thus tagging COVID-19, etc)

## Python Example
Necessery imports:
```
import requests
import json
```
Set up some text to pitch at the API:
```
sample_text = "Are you, by any chance, wondering about giving yourself wings? You should listen to [Liz McFarland] sharing her experience building a Wonder Woman suit, and not just any – the Golden Eagle suit from Wonder Woman 1984, adorned with a giant pair of wings."
```

Define your API endpoint. Swap the "spacy" below for "flair" for different processing:
```
url = "http://127.0.0.1:5000/spacy"
```
Handle the requests:
```
x = requests.get(url, json = {'data':sample_text})
print(x.status_code)
if x.status_code == 200:
    response = json.loads(x.text)
    print(response)
```

Expected SpaCy output:
```
200
{'0': {'span': [85, 98], 'tag': 'PERSON', 'text': 'Liz McFarland'}, '1': {'span': [134, 146], 'tag': 'ORG', 'text': 'Wonder Woman'}, '2': {'span': [199, 211], 'tag': 'ORG', 'text': 'Wonder Woman'}, '3': {'span': [212, 216], 'tag': 'DATE', 'text': '1984'}}
```

Expected Flair output:
```
200
{'0': {'confidence': 0.9323325157165527, 'span': [85, 98], 'tag': 'PER', 'text': 'Liz McFarland'}, '1': {'confidence': 0.7368820607662201, 'span': [134, 146], 'tag': 'MISC', 'text': 'Wonder Woman'}, '2': {'confidence': 0.7811878621578217, 'span': [176, 188], 'tag': 'MISC', 'text': 'Golden Eagle'}, '3': {'confidence': 0.665399432182312, 'span': [199, 211], 'tag': 'MISC', 'text': 'Wonder Woman'}}
```
