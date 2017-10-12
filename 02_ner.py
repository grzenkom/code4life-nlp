from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

ner = StanfordNERTagger('resources/english.all.3class.distsim.crf.ser.gz', 'resources/stanford-ner-3.4.1.jar')
sentence = 'Toto, I''ve a feeling we''re not in Kansas anymore - said Dorothy, looking at her friend Toto.'

tokens = word_tokenize(sentence)
entities = ner.tag(tokens)

print entities
# [(u'Toto', u'O'), (u',', u'O'), (u'Ive', u'O'), (u'a', u'O'), (u'feeling', u'O'), (u'were', u'O'), (u'not', u'O'),
#  (u'in', u'O'), (u'Kansas', u'LOCATION'), (u'anymore', u'O'), (u'-', u'O'), (u'said', u'O'), (u'Dorothy', u'PERSON'),
#  (u',', u'O'), (u'looking', u'O'), (u'at', u'O'), (u'her', u'O'), (u'friend', u'O'), (u'Toto', u'O'), (u'.', u'O')]
