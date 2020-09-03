
from graph import Graph


def buildGraph(word_file):
    d = {}
    g = Graph()
    w_file = open(word_file, "r")

    for line in w_file:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:1] + "_" + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)

    return g
