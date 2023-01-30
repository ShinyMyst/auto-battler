f = open('ascii_skull.txt')
ascii_skull = f.read()
f = open('ascii_exhume.txt')
ascii_exhume = f.read()

objects = [ascii_skull, ascii_exhume]

for obj in objects:
    print(obj)


