from operator import itemgetter
from itertools import dropwhile
from string import punctuation

# homework 1

#Alice said: "I'll do it tomorrow!"
#tokenizing is splitting the sentence into tokens, or words
#I'll could be one word, or a word and a clitic
#do and doing should be one token

##s = 'Alice said : I\'ll do this tomorrow. . .'
##s.lower()
##l= ' Alice did '
##d=l.strip() #this strips spaces, but not characters
##s.split() #splits the string into a list of items

#this puts a string in lower case, strips it of any spaces before and after, and then splits each word into
#individual elements of a list

s = 'Alice said: I\'ll do this tomorrow...'

def tokenize(s):
    words = s.lower().strip().split()
    twords = [word.strip(punctuation) for word in words] #this strips each word of punctuation marks; 'word' could be anything; this doesn't work without importing
    return twords
print(tokenize(s))

# homework 2

alice = open('alice.txt.').read()

a = alice.find("*** START OF THIS PROJECT GUTENBERG EBOOK")
z = alice.find("*** END OF THIS PROJECT GUTENBERG EBOOK")

alice_new = alice[a:z]

def  gutenberg_file_wc(filename):
    alice_tokens = tokenize(alice_new)
    return alice_tokens
print(gutenberg_file_wc(alice_new))

###classwork
###the goal should be a dictionary {'alice':1,'said',2...}
##def text_file_wc(filename): #we are defining a function for a file that will be supplied later on
##    testtext = open('pythonclass3.txt').read() #this reads the file
##    testtext_tokens = tokenize(testtext) #this applies the tokenized fucntion
##    text_file_wc = {x: testtext_tokens.count(x) for x in testtext_tokens} #the value of keys is the count of 'x' in our list of tokens
##    return text_file_wc
##print(text_file_wc('pythonclass3.txt'))

# homework 3

#This problem asks you to write a little helper function to view the
#output of gutenberg_file_wc.  The goal is to print to the screen a
#list of (word, count) pairs, sorted so that the most frequent word
#is at the top.  Requirements:
#* We want to see only words whose count is at least 10.
#* The output should be formatted so that it can be read by the
#Wordle Advanced API:
#http://www.wordle.net/advanced
#* Optional: Attach your Wordle image with your homework.
#To sort a dictionary on its value element, with the most frequent
#tuple at the top of the list, I recommend this method:
#d = {'a': 5, 'b': 10, 'c': 8}
#from operator import itemgetter
#dist = sorted(d.items(), key=itemgetter(1), reverse=True)
#Optional extra credit (0.5 points): it would nice for the threshold
#value to be something that the user can set when calling view_wc(),
#rather than having it coded as part of the function.  Modify
#view_wc so that the default is 10 but the user can set the value
#when calling the function.
#"""

wordcountdata = gutenberg_file_wc(alice_new) #this is a list of strings
def view_wc(d):
    #initialize a dictionary
    data = {}
    for word in wordcountdata:
        #counts the number of time each word comes up in a list of words
        data[word] = data.get(word, 0) + 1
    #reverses the key and values to be sorted using tuples
    wordfreq = []
    for key, value in data.items():
        wordfreq.append((value, key))
        if value < 10:
            wordfreq.pop()
    wordfreq.sort(reverse = True)
    return wordfreq

print(view_wc(wordcountdata))

# homework 4
#{abstract: {1936: 36 mentions of this word, 1960: 24 mentions 'dictionary for abstract'},
 #adhere:

#how to split into tabulations split('\t')
#comment on what the four loop does

##def googlebooks_counts_by_year(filename):
##    d = {}
##    fields = []
##    for line in open('googlebooks.txt', "r"):
##        line = line.strip()
##        line = line.split("\t")
##        frields.append(line)
##    for item in fields:
##            if item[0] not in d.keys():
##                d[item[0]] = {int(item[1]) : int(item[2])}
##            else:
##                x = d[item[0]]
##                x[int(item[1])] = int(item[2])
##    return d
##
##if __name__ == '__main__':
##
##    print(text_file_wc('hw3test.text'))
##    print(googlebooks_counts_by_year('googlebooks.txt'))
##
    
