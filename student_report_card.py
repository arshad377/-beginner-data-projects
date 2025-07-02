while True:
    sno=int(input("enter student roll no(20033445001-20033445100)= "))
    if sno>=20033445001 and sno<=20033445100:
        break
    print("invalid input plz try again")
sname=input("enter student name= ")

while True:
    c=int(input("enter marks obtained in c lang= "))
    if c>=0 and c<=100:
        break
    print("invalid input plz try again!!")

while True:
    cpp=int(input("enter marks obtained in c++= "))
    if cpp>=0 and cpp<=100:
        break
    print("invalid input plz try again!!")

while True:
    pyt=int(input("enter marks obtained in python= "))
    if pyt>=0 and pyt<=100:
        break
    print("invalid input plz try again!!")
ttl=c+cpp+pyt
percent=(ttl/300)*100

if c<40 or cpp<40 or pyt<40:
    grade="FAIL"
else:
    if ttl<=300 and ttl>=250:
        grade="DISTINCTION"
    elif ttl<=249 and ttl>=200:
        grade="FIRST"
    elif ttl<=199 and ttl>=150:
        grade="SECOND"
    elif ttl<=149 and ttl>=120:
        grade="THIRD"
print("="*60)
print("student roll no={}".format(sno))
print("student name={}".format(sname))
print("student marks in c lang={}".format(c))
print("student marks in c++={}".format(cpp))
print("student marks in python={}".format(pyt))
print("student total marks={}".format(ttl))
print("student percentage={}".format(round(percent,3)))
print("student result={}".format(grade))
