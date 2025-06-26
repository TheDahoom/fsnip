import os

file_name = str(input("Enter file name or directory, or just drag the file here: "))

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
    points = []
    while x < size:
        points.append(x) 
        x += file_size

file = open(file_name, "rb")
for i, v in enumerate(points):
    name = "file" + str(i+1) + ".dfs"
    if i == 0:
        open(name, "wb").write(file.read(points[1] - points[0]))
    else:
        num = i-1
        open(name, "wb").write(file.read(points[i] - points[i-1]))

# TODO add a system to remember file name and extension