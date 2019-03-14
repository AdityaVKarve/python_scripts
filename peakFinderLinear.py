#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:37:53 2019

@author: thatguy99
"""

#A peak finder in 1 dimension. A peak exists in 1D array if arr[n]>arr[n+1],arr[n-1]
#for edge cases, if arr[0]>arr[1] or arr[n]>arr[n-1]
#This code is pretty straightforward and has a complexity of O(n)
import array

def peakFindLinear(inpList):
    for x in range(size):
        if x==0:    #Edge case for the start of the list
            if inpList[0]>inpList[1]:
                print("Peak found at element #"+str(x))
                break
        if x==size-1:   #Edge case for the end of the list
            if inpList[size-1]>inpList[size-2]:
                print("Peak found at element #"+str(x))
                break
        if inpList[x]>inpList[x+1] and inpList[x]>inpList[x-1]: #Normal test case
            print("Peak found at element #"+str(x))
            break

size=int(raw_input("Enter size of array:"))
inpList=[]     #This list contains the list whose peaks we need to find
print("Enter elements:")
for x in range(size):
    inpList.append(int(raw_input("Element "+str(x)+":")))
peakFindLinear(inpList)

