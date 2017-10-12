from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

sentence = 'All those moments will be lost in time, like tears in rain.'
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)

print tags
# [('All', 'PDT'), ('those', 'DT'), ('moments', 'NNS'), ('will', 'MD'), ('be', 'VB'), ('lost', 'VBN'), ('in', 'IN'),
#  ('time', 'NN'), (',', ','), ('like', 'IN'), ('tears', 'NNS'), ('in', 'IN'), ('rain', 'NN'), ('.', '.')]
#
# Part of speech tags: https://cs.nyu.edu/grishman/jet/guide/PennPOS.html
