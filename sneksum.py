import hashlib
# setting md5 var
md5 = hashlib.md5();

# get filename
print("hiss, muchaho! you want me to create a sneksum for ya?")
filename = input("no problemos just enter the name of the textfile (.txt) in quotes:")

# opening and closing a file in readonly mode with the filename the user provides 
snekfile = open(filename,"r")
content = snekfile.read()
snekfile.close()

# generate & print checksum
md5.update(content)
print("thiss is your checksum:")
print(md5.hexdigest())

print("thanksss and see ya soon matey!")