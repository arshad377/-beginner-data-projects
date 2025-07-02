n=input("Enter word = ")
n=n.upper()
a=len(n)
i=0
while i<a:
    if n[i] in ['a','e','i','o','u','A','E','I','O','U']:
       print(n[i])
    i+=1
