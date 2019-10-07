import pprint
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords as nltk_stopwords

class Index:


    ## TODO: Parser to read through documents passed by Main
    ## TODO: Remove Print statements and Save Index as Multiple Json files
    ## TODO: Check for Performance with Sample Size and Estimate Performance with Complete Data

    tokenizer = RegexpTokenizer(r'\w+')
    def __init__(self):
        self._index = {}
        self._inverted_index = {}

    @staticmethod
    def clean(tags):
        tokens = Index.tokenizer.tokenize(tags)
        tokens = [i for i in tokens if i not in nltk_stopwords.words()]
        return tokens

    @staticmethod
    def increment_key(d, k):
        try:
            d[k] += 1
        except KeyError:
            d[k] = 1
        return d


    def index(self, photo_id, tags):
        histogram = {}  # Empty if already exists
        tokens = Index.clean(tags)
        token_count = len(tokens)
        for token in tokens:
            histogram = Index.increment_key(histogram, token)
        token_set = set(tokens)
        for token in token_set:
            t_c = tokens.count(token)
            if token not in self._inverted_index:
                self._inverted_index[token] = {
                    'count': 0,
                    'frequency': {}
                }
            self._inverted_index[token]['frequency'][photo_id] = t_c
            self._inverted_index[token]['count'] += t_c
            self._index[photo_id] = {
                'count': token_count,
                'frequency': histogram
            }

    def doc_count(self):
        return len(self._index)

    def print(self, indent_size=2, width=10):
        printer = pprint.PrettyPrinter(indent=indent_size, width=width)
        print('\n\n\nTotal Count of Images and Tags Read: %s' % self.doc_count())
        print('\n\n\nInverted Index:')
        printer.pprint(self._inverted_index)
