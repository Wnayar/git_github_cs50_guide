print("Hello world")
# hi

def swap(a, b):
    # temp = a
    # a = b
    # b = temp
    global x
    global y
    x,y = y,x

x = 1000
y = 50

print("x is ", x)
print("y is ", y)

# swapping
swap(x, y) 

print("x is now ", x)
print("y is now ", y)
