#   /\_/\     ##      ##    #######     ########     #     #
#  (= ._.)    # ##  ## #    #           #            #     #
#  / >  \>    #   ##   #    #######     #   ####     #######
# /      \    #        #    #           #      #     #     #
              #        #    #######     ########     #     #


import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque
from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip()
I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
from queue import PriorityQueue

def square_root(x):
    l = 0
    h = x
    answer = 0
    while l<=h:
        mid = l + (h-l)//2
        if mid*mid > x:
            h=mid-1
        else:
            answer=mid
            l = mid+1
    return answer

def perf_sq(x):
    precision = 0.000001
    low = 0
    upper = x
    if x == 1:
        return 1.000
    while low <= upper:
        mid = low + (upper-low)/2
        a1 = "{:.6f}".format(mid*mid)
        a2 = "{:.6f}".format(x)
        if a1[:7] == a2[:7]:
            return float("{:.3f}".format(mid))
        elif mid*mid > x:
            upper = mid - precision
        elif mid*mid < x:
            low = mid + precision
    return 0

def sieve(target):
    arr = [i for i in range(2,target+1)]
    for i in range(len(arr)):
        if arr[i] != False:
            for j in range(arr[i]**2-2,len(arr),arr[i]):
                arr[j] = False
    answer = []
    for i in arr:
        if i!=False:
            answer.append(i)
    return answer

def compute_lps(pattern):
    lps = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    return lps

def kmp_search(text, pattern):
    if not text or not pattern:
        return []

    lps = compute_lps(pattern)
    matches = []

    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches
