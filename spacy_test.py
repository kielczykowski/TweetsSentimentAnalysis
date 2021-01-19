import spacy

tweet_text = "I bought big and sweet watermelons."
tweet_tags = ["watermelons"]

spacy.prefer_gpu()
nlp = spacy.load('en_core_web_sm')
doc = nlp(tweet_text)
for token in doc:
    if token.head.text in tweet_tags:
        if token.dep_ in ["advmod", "advmod", "agent", "amod", "aux", "cop", "scubj", "det", "dobj", "goeswith", "iobj", "neg", "nn", "npadvmod", "nsubj", "nsubjpass", "num", "pobj", "poss", "preconj", "predeterminer", "prepc", "prt", "quantmod", "rcmod", "ref", "tmod", "xcomp", "xsubj"]:
            siblings = ""
            for twin_token in doc:
                if twin_token.head.text == token.text and twin_token.dep_ == "conj":
                    siblings += " " + twin_token.text
            if len(siblings) != 0:
                siblings = siblings[1:len(siblings)]
            print(token.text, siblings, token.head.text)
