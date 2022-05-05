p = int(input("Enter Value of Principle:-"))
r = int(input("Enter Value of Rate:-"))
t = int(input("Enter Value of Time:-"))

si = (p*r*t)/100
ci = p*(pow((1+r/100),t))-p

print("Simple Interest is:",si)
print("Compound Interest is:",ci)