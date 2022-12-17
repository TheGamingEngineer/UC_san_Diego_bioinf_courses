#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 09:43:13 2022

@author: alexanderandersen
"""


def HammingDist(test1,test2):
    count=0
    if len(test1)!=len(test2):
        exit("Sorry, but the two strings need to be of equal length!")
    for i in range(len(test1)):
        if test1[i]!=test2[i]:
            count+=1
    return count


def KmerDetect(string,list):
    result=[]
    for i in list:
        if i in string:
            result.append(i)
    return result

def patterncount(text,pattern):
    count=0
    for i in range(0,len(text)-len(pattern)):
        if text[i:i+len(pattern)]==pattern:
            count+=1
    return count



def neighbors(pattern, d): 
    assert(d <= len(pattern)) 
    if d == 0: 
        return [pattern] 
    r2 = neighbors(pattern[1:], d-1) 
    r = [c + r3 for r3 in r2 for c in pattern if c != pattern[0]] 
    if (d < len(pattern)): 
        r2 = neighbors(pattern[1:], d) 
    r += [pattern[0] + r3 for r3 in r2] 
    return r


def CGfinder(string,get="all"):
    count=0
    countlist=[]
    for i in range(len(string)):
        if string[i]=="G":
            count+=1
            countlist.append(count)
        elif string[i]=="C":
            count-=1
            countlist.append(count)
    if get.lower()=="min.val":
        return min(countlist)
    elif get.lower()=="max.val":
        return max(countlist)
    elif get.lower()=="min.pos":
        return countlist.index(min(countlist))+1
    elif get.lower()=="max.pos":
        return countlist.index(max(countlist))+1
    elif get.lower()=="all":
        return {"min.val":min(countlist),
                "max.val":max(countlist),
                "min.pos":countlist.index(min(countlist))+1,
                "max.pos":countlist.index(max(countlist))+1}
    else:
        exit("sorry, but it seems that you have entered a value for 'get' that I cannot read.")



def approxPatternCount(text,pattern,d):
    count=0
    for i in range(0,len(text)-len(pattern)):
        new_pat=text[i:i+len(pattern)]
        dif=0
        for y in range(len(new_pat)):
            if new_pat[y]!=pattern[y]:
                dif+=1
        if dif<=d:
            count+=1
    return count

