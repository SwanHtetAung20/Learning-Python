
def my_function(child3, child2, child1):
    print("Child 1:", child1)
    print("Child 2:", child2)
    print("Child 3:", child3)

my_function(child1 = "halo", child2 = "hello", child3 = "hoho")

def my_function(*args):
    for arg in args:
        print(arg)

my_function("Hello", "World", 123, True)        

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key + " : ", value)

my_function(fname = "Ko Kyaw", lname = "Gyi")

def my_function():
    pass

my_function()


# ** can have only positional arguments not keyword arguments
def my_function(x, /):
  print(x)

my_function(3)

# ** can have only keyword arguments not positional arguments
def my_function(*, x):
  print(x)

my_function(x = 3)