import os

# file_name = str(input("Enter file name or directory, eg: game.exe : "))
file_name = "f.blend"

try:
    mb = int(input("Enter size to cut in MB: "))
    file_size = mb * 1000000
except ValueError:
    file_size = 24999999

while True:
    try:
        size = os.path.getsize(file_name)
    except FileNotFoundError:
        file_name = str(input("File not found, please enter the correct path: "))
        continue
    break

if size > file_size:
    x = 0
    points = [0]
    while x <= file_size:
        x += file_size
        points.append(file_size)
    
    print(points)

file = open(file_name, "rb")
new_file = open("file1.dfs", "wb")
new_file.write(file.read(49999 - 24999))
# print(file.read(49999 - 24999))
