import spacy

class Extractor():
    def __init__(self):
        pass

    def getPhrases(self, tweet_text, tweet_tag):
# tweet_text = "I love to dance."
# tweet_tag = "I"
# spacy.prefer_gpu()
        phrases = []
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(tweet_text)
        token_counter = 0
        for token in doc:
            if token.dep_ == 'ROOT' and token.text == tweet_tag:
                phrases.append(tweet_text)
                # print(tweet_text)
            elif token.head.text == tweet_tag:
                if token.dep_ in ["advmod", "advmod", "agent", "aux", "cop", "scubj", "dobj", "goeswith", "iobj", "nn", "npadvmod", "nsubjpass", "num", "pobj", "poss", "preconj", "predeterminer", "prepc", "prt", "quantmod", "rcmod", "ref", "tmod", "xcomp", "xsubj"]:
                    siblings = token.text
                    for twin_token in doc:
                        if twin_token.head.text == token.text and twin_token.dep_ == "conj":
                            siblings = twin_token.text + ' ' + siblings
                    # print(siblings, token.head.text)
                    phrases.append(siblings + token.head.text)
                elif token.dep_ == 'amod':
                    siblings = token.text
                    if token_counter != 0:
                        if doc[token_counter - 1].text == 'not':
                            siblings = 'not' + ' ' + siblings
                    twin_token_counter = 0
                    for twin_token in doc:
                        if twin_token.head.text == token.text and twin_token.dep_ == "advmod":
                            siblings = twin_token.text + ' ' + siblings
                            if twin_token_counter != 0:
                                if doc[twin_token_counter - 1].text == 'not':
                                    siblings = 'not' + ' ' + siblings
                        twin_token_counter += 1
                    for twin_token in doc:
                        if twin_token.head.text == token.text and twin_token.dep_ == "conj":
                            siblings += ' ' + twin_token.text  
                    # print(siblings, token.head.text)
                    phrases.append(siblings + token.head.text)
            elif token.text == tweet_tag and token.dep_ == 'nsubj':
                siblings = token.head.text
                for verb_description in doc:
                    if verb_description.head.text == token.head.text and verb_description.dep_ == "aux":
                        for verb_description_neg in doc:
                            if verb_description_neg.head.text == token.head.text and verb_description_neg.dep_ == "neg":
                                if verb_description_neg.text == "n't":
                                    siblings = 'not' + ' ' + siblings
                                else:
                                    siblings = verb_description_neg.text + ' ' + siblings
                        siblings = verb_description.text + ' ' + siblings
                for verb_description in doc:
                    if verb_description.head.text == token.head.text and (verb_description.dep_ == "xcomp" or verb_description.dep_ == "dobj"):
                        for twin_token_of_twin in doc:
                            is_twin_token_of_twin_added = False
                            if twin_token_of_twin.head.text == verb_description.text and twin_token_of_twin.dep_ == "cc":
                                siblings += " " + verb_description.text
                                siblings += ' ' + twin_token_of_twin.text
                                is_twin_token_of_twin_added = True
                            elif twin_token_of_twin.head.text == verb_description.text and twin_token_of_twin.dep_ == "conj":
                                siblings += " " + verb_description.text
                                siblings += ' ' + twin_token_of_twin.text
                                is_twin_token_of_twin_added = True
                            elif twin_token_of_twin.head.text == verb_description.text and twin_token_of_twin.dep_ == 'compound':
                                siblings += ' ' + twin_token_of_twin.text
                                siblings += " " + verb_description.text
                                is_twin_token_of_twin_added = True
                        if not is_twin_token_of_twin_added:
                            siblings += " " + verb_description.text
                for verb_description in doc:
                    if verb_description.head.text == token.head.text and verb_description.dep_ == "attr":
                        for atrr_description in doc:
                            if atrr_description.head.text == verb_description.text and atrr_description.dep_ == "amod":
                                siblings += ' ' + atrr_description.text                
                        siblings += " " + verb_description.text
                        for twin_token_of_twin in doc:
                            if twin_token_of_twin.head.text == verb_description.text and twin_token_of_twin.dep_ == "cc":
                                siblings += ' ' + twin_token_of_twin.text
                            if twin_token_of_twin.head.text == verb_description.text and twin_token_of_twin.dep_ == "conj":
                                siblings += ' ' + twin_token_of_twin.text
                for verb_description in doc:
                    if verb_description.head.text == token.head.text and verb_description.dep_ == "neg":
                        if verb_description.text == "n't":
                            siblings = siblings + ' ' + 'not'
                        else:
                            siblings = siblings + ' ' + verb_description.text
                for final_adj in doc:
                    if final_adj.head.text == token.head.text and final_adj.dep_ == "acomp":
                        siblings += ' ' + final_adj.text
                phrases.append(token.text + siblings)
                # print(token.text, siblings)
            token_counter += 1
        return phrases
# spacy.displacy.serve(doc, style="dep")