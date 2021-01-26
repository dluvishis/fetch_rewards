from collections import Counter
import re
from flask import Flask, request, jsonify
from lists_definition import DefineCorpus as dc

app_dic=dc.app_dic
synonims=dc.synonyms
exclude=dc.exclude
punct_remove=dc.punct_remove
# create counter for unigrams, bigrams and 3-grams 
# compare same n-grams - get additional points for 3-grams and bigrams
# divide the number by number of sum of meningful words in both corpus. 
def clean_text(text):
    
    ##This funciton cleans input string by replacing words with apostorphe, removing punctuation and replacing synonyms with aliases. 
    if text is None: return ''
    text = text.lower()
    # replace common expessions with apostrophe
    #get rid of punctuation
    text = re.sub(punct_remove,"",text)
        
    for dic in app_dic:
      text = re.sub(dic,app_dic[dic],text)
    

    
    #replace synonyms with unique words
    
    text = ' ' + text + ' '
    for wrd in synonims:
      text=re.sub(' ' + wrd + ' ', ' ' + synonims[wrd]+ ' ', text)
    text=text.strip()
    
    return text
def removePopular(lst):
    ##this function removes extraneous words
    result = list(filter(lambda word: word not in exclude, lst))
    return result

def getuniquewords(string):
    
    # input is a string of words, output is a list of words from the input string excluding extraneous words
    return removePopular(clean_text(string).split())

def sets_compare(ct1, ct2):
    
    #compare 2 lists and return a score 
    
    # difference=items in lst1 not in lst2 and items in lst2 not in lst1
    # allitems= all items in lst1 or lst2
    #formula used: (# items in all words - # items in difference) divided by # items in all words
    # it shows % of items unique to either list. If all items are in both lists, difference is 0, and score=1
    # if no items are in both lists: difference=all items, and score=0
    
    #set1=set(lst1)
    #set2=set(lst2)
    ct1=Counter(ct1)
    ct2=Counter(ct2)
    st1=Counter({key: max(0 if not key in ct2 else ct2.get(key), value) for key, value in ct1.items()})
    st2=Counter({key: max(0 if not key in ct1 else ct1.get(key), value) for key, value in ct2.items()})
    
    dif=(ct2 - ct1) | (ct1 - ct2)
    allwords_common=st1&st2
    
    dif_len=sum(dif.values())
    allwords_common_len=sum(allwords_common.values())
    if (allwords_common_len + dif_len==0): return 0
    return 1.0*allwords_common_len /(allwords_common_len + dif_len)

def findScore(word1, word2):
    
    
    unique_words_one=getuniquewords(word1)
    unique_words_two=getuniquewords(word2)
    
    
    
    unigrams1=dict(Counter(unique_words_one))
    unigrams2=dict(Counter(unique_words_two))



  #find bigrams and trigrams for first string:
    trigrams_one={}
    bigrams_one={}
    if len(unique_words_one)>1:
        bigrams_one[unique_words_one[0] + ' ' + unique_words_one[1]]=1
    for i in range(2,len(unique_words_one)):
        bigram=unique_words_one[i-1] + ' ' + unique_words_one[i]
        trigram=unique_words_one[i-2] + ' ' + bigram
        if bigram in bigrams_one:
            bigrams_one[bigram] +=1
        else:
            bigrams_one[bigram] =1
        if trigram in trigrams_one:
            trigrams_one[trigram] +=1
        else:
            trigrams_one[trigram] =1
            
    #find bigrams and trigrams for second string:
    trigrams_two={}
    bigrams_two={}
    if len(unique_words_two)>1:
        bigrams_two[unique_words_two[0] + ' ' + unique_words_two[1]]=1
    for i in range(2,len(unique_words_two)):
        bigram=unique_words_two[i-1] + ' ' + unique_words_two[i]
        trigram=unique_words_two[i-2] + ' ' + bigram
        if bigram in bigrams_two:
            bigrams_two[bigram] +=1
        else:
            bigrams_two[bigram] =1
        if trigram in trigrams_two:
            trigrams_two[trigram] +=1
        else:
            trigrams_two[trigram] =1
    
    # find % of unigrams common to both strings    
    unigrams_only=sets_compare(unigrams1, unigrams2)
    # find % of bigrams common to both strings
    bigrams_only=sets_compare(bigrams_one, bigrams_two)
    # find % of trigrams common to both strings
    trigrams_only=sets_compare(trigrams_one, trigrams_two)
    
    # if strings are the same, all 3 scores will be 
    
    final_score=unigrams_only *0.5 + bigrams_only*0.33 + trigrams_only * 0.17
    #print ('same words: {}'.format(unigrams_only * 100 ))
    return ('final score: {}'.format(final_score))



app = Flask(__name__)

@app.route('/main_findScore', methods=["GET","POST"])
def main_findScore():

     word1=  request.form.get('word1')
     word2=  request.form.get('word2')
     return jsonify({'result': findScore(word1, word2), 'msg': 'success'})


if __name__ == "__main__":
    app.run(port=1234, debug=True)

