#Maxmatch algorithm: returns word sequence
def maxMatch(sentence, dict):
    if len(sentence) == 0:
        return []
    for i in range(len(sentence), 0, -1):
        firstword = sentence[:i]
        remainder = sentence[i:]
        #print(firstword +" "+ remainder)
        #if word is found
        if firstword in dict:
            word_seq.append(firstword)
            return word_seq.append(maxMatch(remainder, dict))
        
    #if no word is found, make a one-character word
    firstword = sentence[0]
    remainder = sentence[1:]
    word_seq.append(firstword)
    return word_seq.append(maxMatch(remainder, dict))

import sys

#run maxMatch on arguments from command line
sentences = open(sys.argv[1]).read().split('\n')
dictionary = open(sys.argv[2]).read()
word_seq = []
for sentence in sentences:
    tokens = maxMatch(sentence, dictionary)
word_seq = [word for word in word_seq if word != None]
word_seq = [word for word in word_seq if word != []]
print(word_seq)




