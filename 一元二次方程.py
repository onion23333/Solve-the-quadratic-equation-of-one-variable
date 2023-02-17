#一元二次方程

import math as kk
'''
a=float(input('请输入二次项系数'))
b=float(input('请输入一次项系数'))
c=float(input('请输入常数项系数'))
'''
a,b,c=map(float,input('请输入三个系数,用空格分开').split())#利用map()函数同时输入三个系数

delta=b**2-4*a*c
if delta<0:
    print('无解')
elif delta==0:
    x=-b/2/a
    print('有两个相同的解:\nx1 = x2 = %f'%x)
else:
    x1=(-b+kk.sqrt(delta))/2/a
    x2=(-b-kk.sqrt(delta))/2/a
    print('有两个不同的解:\nx1 = %f\nx2 = %f'%(x1,x2))
