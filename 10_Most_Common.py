from collections import Counter
from string import punctuation
import nltk
from nltk.corpus import stopwords

def content_text(text):
 
#Remove common stopwords including "he's" and "she's"    
    stopwords = set(nltk.corpus.stopwords.words('english'))
    stopwords.update(("He's", "She's"))

    
    with_stp = Counter()
    without_stp  = Counter()
    with open(text) as f:
        for line in f:
            spl = line.split()
            # update count off all words in the line that are in stopwrods
            with_stp.update(w.lower().rstrip(punctuation) for w in spl if w.lower() in stopwords)
               # update count off all words in the line that are not in stopwords
            without_stp.update(w.lower().rstrip(punctuation)  for w in spl if w  not in stopwords)
    # return a list with top ten most common words from each 
    return [x for x in with_stp.most_common(10)],[y for y in without_stp.most_common(10)]

wth_stop, wthout_stop = content_text("all_submissions2.txt")

print (wthout_stop)