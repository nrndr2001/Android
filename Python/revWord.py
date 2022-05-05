class Reverse:
    def reverse(my,s):
        l = s.split()
        l.reverse()
        k = " ".join(l)
        return k
str1 = input("Enter String:-")
r = Reverse()
print(r.reverse(str1))