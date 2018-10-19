import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

fname = sys.argv[1]
fname = "exclude/"+fname
f = open(fname,'r')
article = f.read()
f.close()

sentences = sent_tokenize(article)
sentenceRank = dict()

article = article.lower()

stopWords = list(stopwords.words("english"))
words = word_tokenize(article)

wordFreq = dict()

for word in words:
    if word in stopWords or word.isalpha() == False:
        continue
    if word in wordFreq:
        wordFreq[word] += 1
    else:
        wordFreq[word] = 1

for sentence in sentences:
    for word in wordFreq:
        if(word in sentence.lower()):
            if(sentence in sentenceRank):
                sentenceRank[sentence] += wordFreq[word]
            else:
                sentenceRank[sentence] = wordFreq[word]

for sentence in sentenceRank:
    nWords = len(word_tokenize(sentence))
    sentenceRank[sentence] = sentenceRank[sentence]/nWords

avgRank = 0
for sentence in sentenceRank:
    avgRank += sentenceRank[sentence]

avgRank = avgRank/len(sentenceRank)

summary = ''

for sentence in sentences:
    if sentence in sentenceRank and sentenceRank[sentence]>=1*avgRank:
        summary += " " + sentence

g = open('exclude/summary.txt','w')
print(summary)
g.close()
