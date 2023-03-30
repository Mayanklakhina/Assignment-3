#The difference between discard and remove is that remove will through an error if doesn't exist but discard
# will not do. 

# remove function(will through an error if item is not in sets)
set1 ={"mayank","lakhina","apple"}
print(set1)
set1.remove("apple")
print(set1)  # when element exist
set1.remove(1)
print(set1) # when element doesn't exist
  

#Discard function (will not through an error if item is don't exist)
set2={"mayank","lakhina","apple"}
print(set2)
set2.discard("apple")
print(set2)#when element exist
set2.discard(1)
print(set2)#when element doen't exist