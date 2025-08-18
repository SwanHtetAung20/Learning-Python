import os

f = open('./files/names.txt')
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line.strip())

f.close()

try:
    f = open('./files/names.txt')
    print(f.read())
except FileNotFoundError as e:
    print(f"Error: {e}")  
finally:
    f.close()      

f = open("./files/context.txt","a")
f.write("\nKYAWGYI")    
f.close()


f = open("./files/context.txt")
print(f.read())    
f.close()

f = open("./files/names.txt","w")
f.write("I deleted all the names.!")
f.close()

f = open("./files/names.txt")
print(f.read())
f.close()

f = open("./files/haha.txt", "w")
f.close()

if not os.path.exists("./files/hoho.txt"):
   f = open("./files/hoho.txt", "x")
   f.close()    

if os.path.exists("./files/hoho.txt"):
    os.remove("./files/hoho.txt")
else:
    print("The file does not exist")     

with open("./files/context.txt") as f:
    content = f.read()

with open("./files/haha.txt", "w") as f:  
    f.write(content)
    print("Content copied to haha.txt")