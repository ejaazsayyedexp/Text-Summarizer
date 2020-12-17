import sys
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import networkx as nx
import random as rd
import re
import tokenizer

np.seterr(divide='ignore', invalid='ignore')

def createArticle(text):
    article_file = tokenizer.split_into_sentences(text)
    article = []
    for sentence in article_file:
        article.append(sentence)
    index = 0
    if(len(article)>1):
        if(len(article)>3):
            index = len(article)//3
    if(index-2>0):
        intnum = rd.randrange(index-2,len(article)//2)
    else:
        intnum = rd.randrange(index,len(article)//2)
    return article,intnum



stop_words = stopwords.words('english')
def remove_stopwords(item):
    if(item not in stop_words):
        return item
def sent_similarity_calculation(s1,s2):
    
#     print(s1,s2)
    s1_tokens = nltk.word_tokenize(s1)
    s2_tokens = nltk.word_tokenize(s2)
    s1 = ' '.join([w.lower() for w in s1_tokens if re.fullmatch(r'[a-zA-Z]*',w)])
    s2 = ' '.join([w.lower() for w in s2_tokens if re.fullmatch(r'[a-zA-Z]*',w)])
    
    # tokenization
    s1_tokens = list(filter(remove_stopwords,nltk.word_tokenize(s1)))
    s2_tokens = list(filter(remove_stopwords,nltk.word_tokenize(s2)))
#     print(s1_tokens,s2_tokens)
    all_words = list(set(s1_tokens+s2_tokens))
    #print(all_words)
    v1 = [0]*len(all_words)
    v2 = [0]*len(all_words)
    for x in s1_tokens:
        v1[all_words.index(x)]+=1
    for x in s2_tokens:
        v2[all_words.index(x)]+=1
    #print(v1,v2)
    return 1-cosine_distance(v1,v2)




def build_similaritymat(sentences):
    similarity_matrix = np.zeros([len(sentences),len(sentences)])
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if(i==j):
                continue
            temp = sent_similarity_calculation(sentences[i],sentences[j])
            if(np.isnan(temp)):
                similarity_matrix[i,j] = 0
            else:
                similarity_matrix[i,j] = temp
    return similarity_matrix



def generate_summary(text_list,top_n=5):
    summtext = []
    sentence_similarity = build_similaritymat(text_list)
    sen_sim_graph = nx.from_numpy_array(sentence_similarity)
    scores = nx.pagerank(sen_sim_graph)
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(text_list)),reverse = True)
    return ' '.join([ranked_sentence[i][1] for i in range(top_n)]),ranked_sentence

if __name__=='__main__':
    f = sys.argv[1]
    # #No option found other than increasing the time
    # file = open('text_input.txt','w')
    # file.write(f)
    # file.close()
    # #done writing. Should hopefully run
    article,intnum = createArticle(f)
    resu,ranked_sentence = generate_summary(article,intnum)
    print(resu)
    print(len(article),intnum,len(resu),len(ranked_sentence))
    sys.stdout.flush()