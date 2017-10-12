from nltk import WordNetLemmatizer
from nltk.corpus import wordnet as wd

l = WordNetLemmatizer()

print l.lemmatize('study', pos=wd.NOUN), l.lemmatize('studies', pos=wd.NOUN), l.lemmatize('studying', pos=wd.VERB)
# study study study

print l.lemmatize('wanted', pos=wd.VERB), l.lemmatize('gone', pos=wd.VERB), l.lemmatize('bought', pos=wd.VERB)
# want go buy

print l.lemmatize('greener', pos=wd.ADJ), l.lemmatize('fastest', pos=wd.ADJ)
# green fast

print l.lemmatize('better', pos=wd.ADJ), l.lemmatize('better', pos=wd.ADV)
# good well
