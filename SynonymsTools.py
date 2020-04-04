from nltk.corpus import wordnet as guru
from nltk.corpus import wordnet


def get_synonyms(word):
    syns = wordnet.synsets(word)
    return [word.name().split(".")[0] for word in syns]


def check_syns_inside(word, sentence):
    '''
    Check if the word or any of its synonyms are contained inside a sentence
    '''
    test_list = [word]
    for syns in get_synonyms(word):
        test_list.append(syns)
    return len([ele for ele in test_list if (ele in sentence)]) >= 1


def check_multi_syns_inside(word_list, sentence):
    answers = []
    for word in word_list:
        answers.append(check_syns_inside(word, sentence))
    print(answers)
    return any(answers)