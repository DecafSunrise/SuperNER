import spacy
nlp=spacy.load('en_core_web_sm')

def NER(text):
    doc = nlp(text)

    return {idx:
                {"text": ent.text,
                 "tag": ent.label_,
                 "span": (ent.start_char, ent.end_char)} for idx, ent in enumerate(doc.ents)}
