#!/bin/python

import sys


n = int(raw_input().strip())
if n%2!=0:
    print 'Weird'
if n==2 or n==4:
    print 'Not Weird'
if n%2==0 and n>=6 and n<=20:
    print 'Weird'
if n%2==0 and n>20:
    print 'Not Weird'

