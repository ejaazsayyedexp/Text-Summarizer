import sys
import numpy as np
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import networkx as nx
import os


def readFileArticle(f):
    filep = open(f,"r")
    filedat = filep.readlines()
    article = filedat[0].split(".")
    sentences = []
    for sentence in article:
        sentences.append(sentence.replace("[^a-zA-Z]"," ").split(" "))
    print(sentences)
    return sentences


def sentence_similarity(s1,s2,stopwords = None):
    if(stopwords is None):
        stopwords = []
    s1 = [w.lower() for w in s1]
    s2 = [w.lower() for w in s2]
    
    allwords = list(set(s1+s2))
    
    v1 = [0]*len(allwords)
    v2 = [0]*len(allwords)
    
    for x in s1:
        if x in stopwords:
            continue
        v1[allwords.index(x)]+=1
    
    for x in s2:
        if x in stopwords:
            continue
        v2[allwords.index(x)]+=1
    return 1-cosine_distance(v1,v2)



def build_similaritymat(sentences,stop_words):
    similarity_matrix = np.zeros([len(sentences),len(sentences)])
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if(i==j):
                continue
            similarity_matrix[i][j] = sentence_similarity(sentences[i],sentences[j],stop_words)
    return similarity_matrix



def generate_summary(filename,top_n=5):
    stop_words = stopwords.words('english')
    summtext = []
    sentences = readFileArticle(filename)
    sentence_similarity = build_similaritymat(sentences,stop_words)
    sen_sim_graph = nx.from_numpy_array(sentence_similarity)
    scores = nx.pagerank(sen_sim_graph)
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)),reverse = True)
    for i in range(top_n):
        summtext.append(" ".join(ranked_sentence[i][1]))
    return summtext



if(__name__ == '__main__'):
    f = "writethenread.txt"
    l1 = generate_summary(f,7)
    fnew = open('summary.txt',"w")
    fnew.write(". ".join(l1))
    print(". ".join(l1))
    sys.stdout.flush()
