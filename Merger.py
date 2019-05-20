import requests
from bs4 import BeautifulSoup

# Helpful websites used in this script:
# https://stackoverflow.com/questions/11709079/parsing-html-using-python
# https://www.guru99.com/reading-and-writing-files-in-python.html
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start

with open('TFC_Character_Submissions.html') as submit:
    
#  html parsing  
    soup = BeautifulSoup(submit, 'html.parser')
 
# grabs each html link within the 'a' and 'class = "text"' tags    
    kite = soup.find_all('a', {"class":"text"})
    
    for me in kite:
        url = me['href']
        resp = requests.get(url)
        resp.encoding = "utf-8"
        data = resp.text

        f = open('all_submissions2.txt', 'a+')
# " "a" for append and plus sign means if it is not there then create it "
                
        print (data)
        
        for x in data.split('\n'):
            print(data)
            f.write(data)                
              
f.close()
        

