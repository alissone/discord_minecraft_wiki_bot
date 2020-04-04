import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from fuzzywuzzy import fuzz


def remove_stopwords(text):
    clean_text = []
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text)
    for word in tokens:
        if word not in stop_words:
            clean_text.append(word)
    return ' '.join(clean_text)


def get_tag_words(text, tag):
    words = []
    tokens = word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    for token in tagged_tokens:
        if token[1] == tag:
            words.append(token[0])
    return words


def get_verbs(text):
    return get_tag_words(text, 'VB')


def get_nouns(text):
    return get_tag_words(text, 'NN')


def sort_by_dist(distance_dict):
    return sorted(distance_dict, key=lambda d: d['dist'], reverse=True)


def compute_distances(query, vocabulary, sort=False):
    distances = []
    for word in vocabulary:
        distances.append({
            'key': word,
            'dist': fuzz.partial_ratio(query, word)
        })
    if sort:
        return sort_by_dist(distances)
    else:
        return distances


def valid_distance(distance_dict, thresh=65):
    nearest_word = sort_by_dist(distance_dict)[0]
    if nearest_word['dist'] > thresh:
        return nearest_word['key']