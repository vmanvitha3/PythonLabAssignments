#import numpy package to use N-dimensional arrays
import numpy as np

#create vector with random integers ranging between 0-20 inclusive of both start and end values
vector = np.random.randint(0,21,15)

print(vector)   #prints vector

#np.bincount() will return the count of each value in an array of non-negative integers
#it returns an array with the count at the appropriate index

#np.argmax() returns the index of the (first) maximum value in an array.
print (np.bincount(vector).argmax())