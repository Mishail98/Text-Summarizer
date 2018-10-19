import sys
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

fname = sys.argv[1]
fname = "exclude/"+fname
f = open(fname,'r')
article = f.read()
f.close()

ps = PorterStemmer()
sentences = sent_tokenize(article)
sentenceRank = dict()

article = article.lower()

stopWords = list(stopwords.words("english"))
words = word_tokenize(article)
wordsStemmed = [ps.stem(word) for word in words]

wordFreq = dict()

for word in wordsStemmed:
    if word in stopWords or word.isalpha() == False:
        continue
    if word in wordFreq:
        wordFreq[word] += 1
    else:
        wordFreq[word] = 1

for sentence in sentences:
    sentWordsTokenized = [ps.stem(word.lower()) for word in word_tokenize(sentence)]
    for word in wordFreq:
        if(word in sentWordsTokenized):
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
g.write(summary)
print(summary)
g.close()
