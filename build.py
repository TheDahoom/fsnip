import os
import re

dir = input("Enter the directory of files: ") or os.getcwd()
files = os.listdir(dir)

name = input("Enter original file name with extension, eg. game.exe: ")

files_filtered = {}
for i in files:
    if ".dfs" in i:
        digits = re.search(r'\d+', i)
        if digits:
            n = digits.group()
            files_filtered.update({int(n): i})
            
files_sorted = dict(sorted(files_filtered.items()))
content = b""
for i in files_sorted:
    content += open(files_sorted[i], "rb").read()

open(name, "wb").write(content)