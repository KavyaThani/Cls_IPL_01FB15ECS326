f = open('player_vs_player_information3.txt', 'w')
inF = open('player_vs_player_information1.txt', 'r')
lines = inF.readlines()
#list4 format is [total_runs,total_balls,0's,1's,2's,3's,4's,6's,sr]
list4=[0,0,0,0,0,0,0,0,0]
for i in range(len(lines)):
    line1=lines[i]
    if i+1 <= len(lines)-1:
        line2=lines[i+1]
    #line3=lines[i+2]
    else :
        break
    #print(line1)
    #print(line2)
    #print(line3)
    list1=[]
    list2=[]
    #list3=[]
    list1=line1.split(',')
    list2=line2.split(',')
    #list3=line3.split(',')
    #print(list1)
    #print(list2)
    #print(list3)
    list1[2]=int(list1[2])
    list2[2]=int(list2[2])
    #list3[2]=int(list3[2])
    #print(list1)
    #print(list2)
    #print(list3)
    #list4.append(list1[2])
    print(list4)
    if list1[0]==list2[0]:
        if list1[1]==list2[1]:
            #list4.append(list1[2])
            if list1[2]==6:
                list4[7]=list4[7]+1
            else :
                x=int(list1[2])+2
                list4[x]=list4[x]+1
            list4[0]=list4[0]+list2[2]
            list4[1]=list4[1]+1
            list4[8]=list4[0]/list4[1]
            print(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
        else :
            #list4.append(list1[2])
            if list1[2]==6:
                list4[7]=list4[7]+1
            else :
                x=int(list1[2])
                list4[x+2]=list4[x+2]+1
            list4[0]=list4[0]+list2[2]
            list4[1]=list4[1]+1
            list4[8]=list4[0]/list4[1]
            f.write(str(list1[0])+","+str(list1[1])+","+str(list4[0])+","+str(list4[1])+","+str(list4[2])+","+str(list4[3])+","+str(list4[4])+","+str(list4[5])+","+str(list4[6])+","+str(list4[7])+","+str(list4[8])+"\n")
            list4=[0,0,0,0,0,0,0,0,0]
    else :
        #list4.append(list1[2])
        if list1[2]==6:
                list4[7]=list4[7]+1
        else :
            x=int(list1[2])
            list4[x+2]=list4[x+2]+1
        list4[0]=list4[0]+list2[2]
        list4[1]=list4[1]+1
        list4[8]=list4[0]/list4[1]
        #f.write(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
        f.write(str(list1[0])+","+str(list1[1])+","+str(list4[0])+","+str(list4[1])+","+str(list4[2])+","+str(list4[3])+","+str(list4[4])+","+str(list4[5])+","+str(list4[6])+","+str(list4[7])+","+str(list4[8])+"\n")
        list4=[0,0,0,0,0,0,0,0,0]
'''
list4.append(list2[2])
f.write(str(list2[0])+","+str(list2[1])+","+str(list4)+"\n")

print(str(list2[0])+","+str(list2[1])+","+str(list4)+"\n")
print("Hello")

'''
print(list4)
print(list2)


list3=[]
#list4.append(list2[2])
#f.write(str(list2[0])+","+str(list2[1])+","+str(list4)+"\n")
#list3.append(list2[0],list2[1],str(list4))
    #line1=lines[len(lines)-2]
line3=lines[len(lines)-1]
list3=line3.split(',')
list3[2]=int(list3[2])
print(list4)
if list3[0]==list2[0]:
    if list3[1]==list2[1]:
         #list4.append(list1[2])
        if list2[2]==6:
            list4[7]=list4[7]+1
        else :
            x=int(list2[2])+2
            list4[x]=list4[x]+1
        list4[0]=list4[0]+list2[2]
        list4[1]=list4[1]+1
        list4[8]=list4[0]/list4[1]
        print(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
    else :
            #list4.append(list1[2])
        if list2[2]==6:
            list4[7]=list4[7]+1
        else :
            x=int(list1[2])
            list4[x+2]=list4[x+2]+1
        list4[0]=list4[0]+list2[2]
        list4[1]=list4[1]+1
        list4[8]=list4[0]/list4[1]
        #f.write(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
        f.write(str(list1[0])+","+str(list1[1])+","+str(list4[0])+","+str(list4[1])+","+str(list4[2])+","+str(list4[3])+","+str(list4[4])+","+str(list4[5])+","+str(list4[6])+","+str(list4[7])+","+str(list4[8])+"\n")
        list4=[0,0,0,0,0,0,0,0,0]
else :
        #list4.append(list1[2])
        if list2[2]==6:
            list4[7]=list4[7]+1
        else :
            x=int(list2[2])
            list4[x+2]=list4[x+2]+1
        list4[0]=list4[0]+list2[2]
        list4[1]=list4[1]+1
        list4[8]=list4[0]/list4[1]
        #f.write(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
        f.write(str(list1[0])+","+str(list1[1])+","+str(list4[0])+","+str(list4[1])+","+str(list4[2])+","+str(list4[3])+","+str(list4[4])+","+str(list4[5])+","+str(list4[6])+","+str(list4[7])+","+str(list4[8])+"\n")
'''
list4.append(list3[2])
if list2[2]==6:
    list4[7]=list4[7]+1
else :
    x=int(list2[2])
    list4[x+2]=list4[x+2]+1
list4[0]=list4[0]+list2[2]
list4[1]=list4[1]+1
list4[8]=list4[0]/list4[1]
print(list4)
'''
#f.write(str(list3[0])+","+str(list3[1])+","+str(list4)+"\n")
f.write(str(list1[0])+","+str(list1[1])+","+str(list4[0])+","+str(list4[1])+","+str(list4[2])+","+str(list4[3])+","+str(list4[4])+","+str(list4[5])+","+str(list4[6])+","+str(list4[7])+","+str(list4[8])+"\n")

f.close()
inF.close()
