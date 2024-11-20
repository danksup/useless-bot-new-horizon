
import spacy

# Load a spaCy model
nlp = spacy.load("en_core_web_sm")

# Process text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for ent in doc.ents:
    print(ent.text, ent.label_)




