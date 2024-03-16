#
l=[12,42,23,96,7,18,10,133]
#addition of min and max
#max-->addition
#min-->subtraction
mini=0
maxi=0
miniid=0
maxiid=0
for i in range(len(l)):
    if mini>l[i]:
        mini=l[i]
        miniid=i
    if maxi<l[i]:
        maxi=l[i]
        maxiid=i
s=mini+maxi
d=maxi-mini

l[maxiid]=s
l[miniid]=d