import csv
from collections import Counter
from math import sqrt

UPPER = "qwertpoiuy"
MIDDLE = "asdfglkjh"
LOWER = "zxcvbnm"

def get_class_count(word_dict, _kls):
    """getting a class count"""
    keys = set(word_dict.keys())
    _kls_set = set(_kls)
    intersection = keys & _kls_set
    return sum([word_dict[key] for key in intersection])


def get_stats(word):
    """ Representign a word as a vertor [i, j, k]
        i - Number of words from upper keyboard row
        j - Number of words from middle keyboard row
        k - Number of words from lower keyboard row
    """
    stat = Counter(word)
    return [get_class_count(stat, UPPER),
            get_class_count(stat, MIDDLE),
            get_class_count(stat, LOWER)]

def distance(word1, word2):
    """ Does the vector magnitude for two stats
    """
    stat1 = get_stats(word1)
    stat2 = get_stats(word2)
    return sqrt(sum([(i-j)**2 for i, j in zip(stat1, stat2)]))

def majority(labels):
    """get the majority for label
       Since we have to filter only one optimally
       if two labels have same counts try
       removing the farthest one and
       continue it.
    """
    counts = Counter(labels)
    winner, winner_count = counts.most_common(1)[0]
    num_winners = len([count for count in counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner                     # unique winner, so return it
    else:
        return majority(labels[:-1])

def knn_classify(k, labeled, word):
    """each labeled point should be a pair (point, label)"""
    # order the labeled points from nearest to farthest
    by_distance = sorted(labeled,
                         key=lambda point: distance(point["WORDS"], word))

    # find the labels for the k closest
    k_nearest_labels = [label["label"] for label in by_distance[:k]]

    # and let them vote
    return majority(k_nearest_labels)


if __name__ == "__main__":

    reader = csv.DictReader(open("scribble_data.txt"))
    values = list(reader)
    test_scribble = ["sdjkflsd", 
                    "ivfnfin",
                    "siofuewoi",
                    "ewuroqo",
                    "weiuoro",
                    "vbfbjsad",
                    "hello",
                    "word",
                    "wouerwiuer",
                    "jupiter",
                    "simplex"]
    for data in test_scribble:
        predicted = knn_classify(2, values, data)
        print("{} is classified as {}".format(data, predicted))
