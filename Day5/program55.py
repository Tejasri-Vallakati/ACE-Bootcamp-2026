with open("/workspaces/ACE-Bootcamp-2026/images.jpeg",'rb') as f:
    content = f.read()
    with open("/workspaces/ACE-Bootcamp-2026/images1.jpeg","wb") as cf:
        cf.write(content)