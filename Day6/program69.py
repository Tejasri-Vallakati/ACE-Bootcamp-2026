import numpy as np
arr=np.array([[1,2],[3,4]])
arr.flags.writeable=False
arr_copy=np.array(arr)
arr_copy[0]=0
print(arr_copy)