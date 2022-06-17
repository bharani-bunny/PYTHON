"""
Write a program to copy the contents of one file to another file.
"""

with open("input.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)
f=open("input.txt")
f1=f.read()
f=open("out.txt")
f2=f.read()
print(f1)
print(f2)

"""
output:
hii this is bharani
hii this is bharani
"""