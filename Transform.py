import numpy as np
from functools import reduce
def WESA(strs,size,z):
    num=(size-1)//31+1
    array=[0 for i in range(num)]
    for str in strs:
        temp=[]
        for a in str:
            temp.append(ord(a)) #取 ascii 码
        temp=np.array(temp,dtype=int)
        #print(temp)
        #res=reduce(lambda x, y: x*z+y,temp)%size
        res=reduce(lambda x, y: x*z+y,temp)%size-50000
        #print(res)
        numtemp=res//31
        settemp=res%31
        array[numtemp]=array[numtemp]|1<<(settemp-1)
    return array