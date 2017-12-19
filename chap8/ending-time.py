'''
This program takes two lines of input. The first line is a "starting time" expressed in a 24-hour clock with leading zeroes, like 08:30 or 14:07. 
The second line is a duration D in minutes. 
Print out what time it will be D minutes after the starting time. For example, for input:
12:30
47
the correct output would be 13:17. 
All times should be formatted as numbers between 00:00 and 23:59, but the time period may go over midnight. 
For example, on input
23:59
13
the correct output is 00:12.
'''

HM = input()
D = int(input())
h=int(HM[0:2])
M=int(HM[3:5])
m = (M+D)%60
hh = (M+D)//60
h=(h+hh)%24
   
if len(str(m))==1:
   m='0'+str(m)
if len(str(h))==1:
   h='0'+str(h)
print(str(h) + ':' + str(m))
