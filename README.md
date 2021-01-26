# fetch_rewards

## Fetch Rewards Coding Exercise
### Description
ML Exercise: https://fetch-hiring.s3.amazonaws.com/ml-engineer/text-similarity.html

This challenge will focus on the similarity between two texts. The objective is to write a program that takes as inputs two texts and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0. 


### Metric use

In order to compare similarity of 2 texts we need to compare semantic meaning of text. In this solution we will implement the following scenario:

1. Cleaning
    * Punctuation
        Get Rid of Punctuation
    * Abbreviation
        Replace Abbreviation ("I've" will become "I have" etc)
    * Synonyms
        Replace Synonyms with Aliases ("cut out" is replaced with "clip" etc)
    * Extraneous words
        Remove words with no additional meaning - the, to etc
    
    Depending on the corpus the 4 lists or dictionaries can be different, which is especially true for Synonymes. For example, word "point" can be replaced with "reward" in the example provided but it won't be correct in other cases. Knowing the corpus is important to this exercise. 

2.  Lists with all unigrams, bigrams and trigrams

    _Here is more information on n-grams in NLP: https://en.wikipedia.org/wiki/N-gram_

    We are creating 3 separate lists for both texts which will include all unigrams, bigrams, trigrams.

3. Score calculation 
    Score Calculation is based on lists comparision separately for unigrams, bigrams and trigrams. 
    Comparission score between 2 lists lst1 and lst2 is calculated using this formulae:

    **Score= (Num_allitems - Num_dif)/Num_allitems**

    ##### difference=items in lst1 not in lst2 and items in lst2 not in lst1. Num_dif - number of elements unique to either lst1 and lst2
    ##### allitems= all items in lst1 or lst2. Num_allitems - number of elements in all items

    This score shows % of items unique to either list. If all items are in both lists, difference is 0, and score=1. If no items are in both lists: difference=all items, and score=0

4. Final Score 

    To add weight to word order in the text the final score is calculated using comparision score for unigrams, bigrams and trigrams. The weights chosen are 50% for unigrams, 33% for bigrams and 17% for trigrams. 

    **Final Score = 0.5 * (Unigrams Score) + 0.33 * (Bigrams Score) + 0.17 * (Trigrams Score)**

_


### Implementation

This project is implemented as a web service in Flask. 

_If you'd like to run this project on your machine, make sure that you have python and flask installed. The easiest way to achieve it would be to download Conda: https://docs.conda.io/projects/conda/en/latest/index.html_

Download the project on your machine and from command line run:
python main.py
This should start web service http://127.0.0.1:1234/main_findScore on your machine. 

To test web service in a separate command line run:
python test_request.py It contains Post request to http://127.0.0.1:1234/main_findScore with 2 variables word1 and word2
Responce will contain final score in the format: "final score: ____".

### Corpus

The lists included in Cleaning are defined in a separate file lists_definition.py.

* punct_remove: Punctuation    
* app_dic: Abbreviation    
* synonyms: Synonyms      
* exclude: Extraneous words




