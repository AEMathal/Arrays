from array import *

ae = array('i',[1,2,3,4,5,6,8,9])

for x in ae[-4:-1]:
    ae.pop()

print(ae)
