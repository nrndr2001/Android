f1 = open('file.txt','w')
f1.write("Hello, I am Yash Sankhla")
f1.close()
f2 = open('file.txt','r')
text = f2.read()
k = set(text)
dict1 = {}
for i in k:
    dict1[i] = text.count(i)
print(dict1)
if '#' in text and '{' in text and ';' in text and 'c' in text:
    print("C file")
elif '()' in text or '=' in text:
    print("Python File")
else:
    print("Text File")
f2.close()