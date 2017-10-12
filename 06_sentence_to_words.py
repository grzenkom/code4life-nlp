import langdetect

from nltk import WordNetLemmatizer

from nltk.corpus import stopwords
from nltk.corpus import wordnet as wd
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize


def main():
    sentence = 'To boldly go where no man has gone before'
    sentence = sentence.lower()

    print langdetect.detect_langs(sentence)
    # [en:0.999996148824]

    tokens = word_tokenize(sentence)
    tags = pos_tag(tokens)
    print tags
    # [('to', 'TO'), ('boldly', 'RB'), ('go', 'VB'), ('where', 'WRB'), ('no', 'DT'), ('man', 'NN'), ('has', 'VBZ'),
    #  ('gone', 'VBN'), ('before', 'IN')]

    sw = stopwords.words('english')
    tags_no_sw = filter(lambda t: t[0] not in sw, tags)
    print tags_no_sw
    # [('boldly', 'RB'), ('go', 'VB'), ('man', 'NN'), ('gone', 'VBN')]

    lemmas = map(lambda t: lemmatize_tag(t), tags_no_sw)
    print lemmas
    # ['boldly', 'go', 'man', 'go']


def lemmatize_tag(tag):
    l = WordNetLemmatizer()
    return l.lemmatize(tag[0], get_nltk_pos(tag[1]))


def get_nltk_pos(tag):
    if tag.startswith('J'):
        return wd.ADJ
    elif tag.startswith('V'):
        return wd.VERB
    elif tag.startswith('N'):
        return wd.NOUN
    elif tag.startswith('R'):
        return wd.ADV
    else:
        return None


if __name__ == '__main__':
    main()
