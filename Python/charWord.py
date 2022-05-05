f1 = open('file.txt','w')
f1.write("Hello, I am Yash Sankhla")
f1.close()
f2 = open('file.txt','r')
text = f2.read()
l = text.split()
lines = text.count('\n')
count = 0
for i in text:
    count+=1

print(f"Words={len(l)} lines={lines} char={count}")