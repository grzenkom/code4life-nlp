from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

ner = StanfordNERTagger('resources/english.all.3class.distsim.crf.ser.gz', 'resources/stanford-ner.jar')
sentence = 'Toto, I''ve a feeling we''re not in Kansas anymore - said Dorothy, looking at her friend Toto.'

tokens = word_tokenize(sentence)
entities = ner.tag(tokens)

print entities
