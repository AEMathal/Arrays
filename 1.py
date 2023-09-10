import array
# Declray the array 
ae = array.array('i',[1,2,3,4,5,6,7])

# Display the content
print(ae[0])
try:
    print(ae[8])
except:
    print("error")

