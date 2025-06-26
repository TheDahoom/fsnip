import os

dir = input("Enter the directory of files: ") or os.getcwd()
files = sorted(os.listdir(dir))

content = b""
for i in files:
    if ".dfs" in i:
        content += open(i, "rb").read()

open("g.blend", "wb").write(content)