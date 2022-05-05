f1 = open('file.txt','w')
f1.write("Hello,\n I am Your Name\n 3rd Yr")
f1.close()
f2 = open('file.txt','r')
text = f2.readlines()
count = 0
for line in text:
    count+=1
    print(f"line{count}:{line[::-1]}")