f = open('batsman_rcb10.txt', 'w')
inF = open('batsman_rcb', 'r')
lines = inF.readlines()
#list4 format is [total_runs,total_balls,0's,1's,2's,3's,4's,6's,sr]
list4=0
for i in range(len(lines)):
    line1=lines[i]
    list1=[]
    list1=line1.split(' ')
    f.write(str(list1))


f.close()
inF.close()

