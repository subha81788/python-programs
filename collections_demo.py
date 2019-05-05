myTupple = ("cat","dog","rabbit","pigeon", "gold fish", "parrot")
print(myTupple)
myList = [1,2,3,4,5]
print(myList)
myList.append(6)
print(myList)
myList.insert(0,0)
myList.insert(1,7)
print(myList)
myList.append(7)
print(myList)
myList.remove(7)
print(myList)
#print("Trying to delete 8 which is not in list")
#myList.remove(8)

myDict = {"Apple":150,"Guava":120,"Mango":250,"Lichi":400,"Pineapple":100,"Banana":50,"Grape":200,"Cucumber":30,"Watermelon":80}
for k,v in myDict.items():
    print("Fruit: {0:20s}Price: {1}".format(k,v))

print("\nDictionary sorted with fruit name in alphabetical order")
for k1 in sorted(myDict):
    print("Fruit: {0:20s}Price: {1}".format(k1,myDict[k1]))
