def process(word):
    output=''
    for x in word:
        if (x.isalpha()):
            output+=x
        return output.lower()

newline=[]

f=open("C:\성공회대학교\proverbs.txt",'r')
for line in f:
    linewords=line.split()
    for word in lineword:
        newline+=process(word)

for x in newline:
    




    



        
        
