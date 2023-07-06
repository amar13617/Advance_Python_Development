def before_nd_after(func):
    print("Before")
    print(func())
    print("After")
  
before_nd_after(lambda:5)
