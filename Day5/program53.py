f=open("/workspaces/ACE-Bootcamp-2026/Day5/program52.py","w")
f.write("a=123\nprint(a)")
print("File Name is :",f.name)
print(f.tell())
f.close()
print(f.closed)

with open("/workspaces/ACE-Bootcamp-2026/Day5/program52.py","r") as f:
    print(f.read())
print(f.closed)