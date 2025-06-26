# file_name = str(input("Enter file name or directory, eg: game.exe : "))

file_name="f.blend"

try:
    file_size = int(input("Enter size to cut in MB: "))
except ValueError:
    file_size = 24999

file = open(file_name, "r")
print(file.read())