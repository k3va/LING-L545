import sys
from nltk.tokenize import sent_tokenize

sent_tokenize_list = []
text = sys.stdin.readline()
while text != '':
    sent_tokenize_list.append(sent_tokenize(text))
    text = sys.stdin.readline()
print("\n".join(line[0] for line in sent_tokenize_list))   
