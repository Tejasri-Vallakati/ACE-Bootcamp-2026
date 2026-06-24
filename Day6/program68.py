import numpy as np
marks=np.array([
    [95,100,1,55,60],
    [25,45,63,77,68]
])
marks[(marks > 50 )& (marks <= 70)] = 4
print(marks)