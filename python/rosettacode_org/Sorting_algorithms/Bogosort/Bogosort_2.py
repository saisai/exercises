import random
def bogosort(lst):
   random.shuffle(lst)  # must shuffle it first or it's a bug if lst was pre-sorted! :)
   print(lst)
   while lst != sorted(lst):
       random.shuffle(lst)
   return lst

testset = [100, 10, 2, 99, 5, 6, 11]
print(bogosort(testset))