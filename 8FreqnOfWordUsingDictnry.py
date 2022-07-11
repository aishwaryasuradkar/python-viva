print("Name- Aditya Motale")
str_1 = "Never let a stumble in a road be the reason to end the journey"
l=[]
l=str_1.split()
wordFreq=[l.count(p) for p in l]

dict(zip(l,wordFreq))