def fileRead(a):
    file = open(a)
    text = file.read()
    file.close()
    return text
    

def wordcount(a):
    file = open(a)
    text = file.read()
    wordList = text.split()
    file.close()
    return len(wordList)
    
print(wordcount("task6_read_me.txt"))