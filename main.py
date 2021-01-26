from collections import Counter
import re
dict_to_ignore=[]

#get rid of punctuation
#ignore words in dict_to_ignore
#replace words in sinonyms
# create counter for unigrams, bigrams and 3-grams 
# compare same n-grams - get additional points for 3-grams and bigrams
# divide the number by number of sum of meningful words in both corpus. 
def clean_text(text):
    text = text.lower()
    #foction de replacement
    app_dic={"i am": "i'm", "you'll": "you will","don't":"do not", "we'll":"we will", "can't":"cannot"}
    
    for dic in app_dic:
      text = re.sub(dic,app_dic[dic],text)
    text = re.sub(r"[-()\"#/@;:<>{}=~|.?,]","",text)
    synonims={'cut out': 'clip', 'products': 'items', 'easiest':'best'}
    text = ' ' + text + ' '
    for wrd in synonims:
      text=re.sub(' ' + wrd + ' ', ' ' + synonims[wrd]+ ' ', text)
    text=text.strip()
    

    return text
def removePopular(lst):
  exclude=['the', 'to', 'you', 'any', 'will','do','just', 'and','we', 'a', 'have', 'for', 'is']
  result = list(filter(lambda word: word not in exclude, lst))
  return result

def getuniquewords(string):
  return removePopular(clean_text(string).split())
def sets_compare(lst1, lst2):
  set1=set(lst1)
  set2=set(lst2)
  dif=(set1 - set2) | (set2 - set1)
  allwords=set1 | set2
  return 1.0*(len(allwords) - len(dif)) /len(allwords)
def main(word1, word2):
    
  unique_words_one=getuniquewords(word1)
  unique_words_two=getuniquewords(word2)



  unigrams1=dict(Counter(unique_words_one))
  unigrams2=dict(Counter(unique_words_two))



  #find bigrams and trigrams:
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

  unigrams_only=sets_compare(unigrams1, unigrams2)
  bigrams_only=sets_compare(bigrams_one, bigrams_two)
  trigrams_only=sets_compare(trigrams_one, trigrams_two)
  
  final_score=unigrams_only *0.5 + bigrams_only*0.33 + trigrams_only * 0.17
  #print ('same words: {}'.format(unigrams_only * 100 ))
  print ('final score: {}'.format(final_score))






if __name__ == "__main__":

    # execute only if run as a script
  word1="The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
  word2="We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."
  #word2=word1
  main(word1, word2)

