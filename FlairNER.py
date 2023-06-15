from flair.nn import Classifier
from flair.data import Sentence

tagger = Classifier.load('ner-fast')


def NER(text):
    sentence = Sentence(text)
    tagger.predict(sentence)

    return {idx:
                {"text": entity.text,
                 "tag": entity.tag,
                 "span": (entity.start_position, entity.end_position),
                 "Confidence": entity.score} for idx, entity in enumerate(sentence.get_spans('ner'))}
