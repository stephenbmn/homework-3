# homework-3

wordcountdata = gutenberg_file_wc(alice_new) #this is a list of strings
def view_wc(d):
    freq = {}
    for word in wordcountdata:
        words = [x for x in freq.keys()]
        if word in words:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

print(view_wc(wordcountdata))
