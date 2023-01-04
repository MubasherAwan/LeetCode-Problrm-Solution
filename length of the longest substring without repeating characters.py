# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:15:40 2022

@author: iammu
"""
s= "ab "
if(s!=""):
#     count=0
#     alphas = s[0]
    length = 0
    
#     for i in range(len(s)-1):
        
#         if(alphas.__contains__(s[i+1])):
#             if(len(alphas)>=length):
#                 length = len(alphas)
#             count=count+1
#             alphas = s[i+1]
#         else:
#             alphas = alphas +s[i+1]
#         print(alphas)
            
#     if(length==0):
#        length = len(s)
       
#     if(len(alphas)>=length):
#         length = len(alphas)
# print(length)
    lists=[]
    for i in range(len(s)):
        alphas = s[i]
        for j in range(i+1,len(s)):
            if(alphas.__contains__(s[j])):
                # print(alphas)
                # print(len(alphas))
                lists.append(alphas)
                break
            else:
                alphas = alphas+s[j]
                # print(alphas)
                # print(len(alphas))
                lists.append(alphas)
        if(length<len(alphas)):
            length = len(alphas)
    
    
    
    print(length)
         
