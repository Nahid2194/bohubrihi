"""
f = open('a.text','w')

print(f.name)
print('Is it closed??',f.closed)
print('file is this mode',f.mode)

f.write("Python is my Favourite language")
f.close()

f= open('a.text','a')
f.write(".I also love Java")

"""

f = open('a.text','r+')
print(f.read(12))
f.close()