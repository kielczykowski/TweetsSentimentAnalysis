import spacy

spacy.prefer_gpu()
nlp = spacy.load('en_core_web_sm')
doc = nlp("In hotel was good service and bad food.")
for token in doc:
    if token.head.text == "service" or token.head.text == "food":
        if token.dep_ in ["advmod", "advmod", "agent", "amod", "aux", "cop", "scubj", "det", "dobj", "goeswith", "iobj", "neg", "nn", "npadvmod", "nsubj", "nsubjpass", "num", "pobj", "poss", "preconj", "predeterminer", "prepc", "prt", "quantmod", "rcmod", "ref", "tmod", "xcomp", "xsubj"]:
            print(token.text, token.head.text)
