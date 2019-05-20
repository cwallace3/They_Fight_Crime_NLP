

import pandas as pd
from textblob import TextBlob

senti_1 = pd.DataFrame()
senti_2 = pd.DataFrame()
with open("all_submissions2.txt") as f: 
    for sentence in f:
        change = sentence.replace('They fight crime!', '')
        if "He's" in sentence:
            sentence = sentence.split("He's")[1]
            senti_1 = senti_1.append({'Character': sentence, 
                                  'Polarity':TextBlob(sentence).sentiment.polarity}, ignore_index=True)
# ignore_index=True was added due to error received: Can only append a Series 
# if ignore_index=True or if the Series has a name        
    
    if "She's" in sentence:
            sentence = sentence.split("She's")[1]
            senti_2 = senti_2.append({'Character': sentence, 
                                  'Polarity':TextBlob(sentence).sentiment.polarity}, ignore_index=True)
    
senti_1 = senti_1.groupby(['Polarity'])
senti_2 = senti_2.groupby(['Polarity'])

best = "He's "+ senti_2.tail(1)['Character'].values[0].strip()+" She's "+ senti_1.tail(1)['Character'].values[0].strip() + " They fight crime!"

worst = "He's "+ senti_2.head(1)['Character'].values[0].strip()+" She's "+ senti_1.head(1)['Character'].values[0].strip() + " They fight crime!"


print ("The best character for each gender: ")
print(best)

print ("The worst character for each gender: ")
print (worst)