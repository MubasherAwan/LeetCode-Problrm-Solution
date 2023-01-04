# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 08:49:00 2022

@author: iammu
"""

# nums1 = [1,3]
# nums2 = [2]


nums1 = []
nums2 = [1,2]
n=0
num = sorted(nums1 + nums2)
l=(len(num))
if(l%2 == 1):
    print("odd")
    n1 = (l+1)/2
    n=(num[int(n1)-1])
    print(n)
    
else:
    print("even")
    n1 = l/2
    n2 = (l/2)-1
    n= (num[int(n1)]+num[int(n2)])/2
    print(n)

    
    
    
    