#Import Libraries
import re
from itertools import islice, izip
import nltk
import unicodedata
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
import io

wordList = []
text_res = []
#To read data from a file
f = io.open("data.txt","r",encoding='utf-8')
data = unicodedata.normalize('NFKD', f.read()).encode('ascii', 'ignore')
tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(data)

#To uses lemmatizer
lemmatizer = WordNetLemmatizer()

print "\n\n*****************************************************************************"
print "                               Lemmatization"
print "*****************************************************************************"

for word in words:
    print word + ":" + lemmatizer.lemmatize(word)
    if word not in wordList:
        wordList.append(word)
    #print word+":"+ps.stem(word)

print "WordList:\n",wordList
newWords = re.findall("\w+", data)

print "\n\n*****************************************************************************"
print "                              Bigram Frequency"
print "*****************************************************************************"

#Prints all bigrams
print nltk.Counter(izip(newWords, islice(newWords, 1, None)))
print ""

print "\n\n*****************************************************************************"
print "                               Top 5 Bigrams"
print "*****************************************************************************"

#To get most common 5 bigrams
counts = nltk.Counter(izip(newWords, islice(newWords, 1, None))).most_common(5)
print counts

print "\n\n*****************************************************************************"
print "                            Summarization            "
print "*****************************************************************************"
print "            Concatenation of sentences containing Top 5 Bigrams             "
print "*****************************************************************************"

#Split .txt file into list of strings containing sentences
list = data.split('.')

#Save top5 bigrams to the list
bi_list = []
for count in counts:
    bi_list.append(count[0])

#Check for sentences containing top 5 bigrams
matching = ""
countFreq = dict()
for i in bi_list:
    for item in list:
        if i[0] in item:
            if i[1] in item:
                if item not in countFreq:
                    countFreq[item] = 1 #To avoid printing same sentence again
                    matching = matching + item.strip() +". "

#Print concatenated sentences containing most frequent bigrams
print matching

#Close file
f.close()