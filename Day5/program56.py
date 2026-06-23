with open("/workspaces/ACE-Bootcamp-2026/Day5/program52.py",'r') as f:
    content = f.readline(2000)
    with open("/workspaces/ACE-Bootcamp-2026/Day5/program52.py","wb") as cf:
        while  len(content) > 0:
            cf.write(content)
            content=f.read(2000)