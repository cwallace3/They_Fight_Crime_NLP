# User documentation for They Fight crime Character NLP Analysis Assignment

### Summary 
This project contains 4 files:
1) TFC_Character_Submissions.html - contains the .html file from the discussion board webpage on Canvas. This is where the students posted their text files of the 50 male and female characters, used in the "Web Scraper" assignment, from the “theyfightcrime.org” website.  
2) Merger.py - Merges the text file, from the Canvas discussion board, into a single file. 
3) sentiment_analysis.py - finds the best and worst (postive or negative, respectively) character of each gender (based on sentiment analysis) and groups them together into the original format of the joke (He's, She's, They fight crime!).  
4) 10_Most_Common.py -  finds the 10 most common descriptions for characters *

*Stopwords from the NLTK Data package will need to be installed in order to use this script properly. For more information on downloading the full NLTK Data package, please see this [link](https://www.nltk.org/data.html).


To run these scripts, please follow the instructions below:

* Download the TFC_Character_Submissions.html to your local directory. Place in folder where the scripts will be located.
* Run the Merger.py . This will create a file of the combined text data to your working directory. The file name is 'all_submissions2.txt' .
* Next, run sentiment_analysis.py which will analyze the 'all_submissions2.txt' (in your in working directory). It will output the best and worst characters in your IDE.
* Lastly, run 10_Most_Common.py which will again analyze the 'all_submissions2.txt'. This will find the 10 most common descriptions for characters. Note that stop words (e.g., a, the, for, with, etc.) along with the manually added words of "he's" and "she's" will not be included in the results.

