# open file and make list of words in file
#tallying number of time word found in file
#end up with dict. of keys = word and value = number times occurs

word_count = {}
split_document = []
document = open("test.txt")

for line in document:
    stripped_line = line.rstrip() #stripping extra
    split_document.extend(stripped_line.split(" ")) #adding words in line to external list
    
for word in split_document: #adding words in line to dictionary
    word_count[word] = 0


for word in split_document:
    word_count[word] = word_count[word] + 1

for word, count in word_count.iteritems():
    print '%s %d' % (word, count) 


