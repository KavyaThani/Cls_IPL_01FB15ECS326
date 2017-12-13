f = open('player_vs_player_Probability3.txt', 'w')
inF = open('player_vs_player_Probability2.txt', 'r')
lines = inF.readlines()
#list4 format is [0's,1's,2's,3's,4's,6's,total_balls]
list4=[0,0,0,0,0,0,0]
counter=0
for i in range(len(lines)):
	line1=lines[i]
	if i+1 <= len(lines)-1:
		line2=lines[i+1]
   
	else :
		break
    
	list1=[]
	list2=[]
    
	list1=line1.split(',')
	list2=line2.split(',')
    
	list1[2]=float(list1[2])
	list2[2]=float(list2[2])
    
	#print(list4)
	if list1[0]==list2[0]:
		if list1[1]==list2[1]:
           
			list4[0]=list4[0]+float(list2[2])	#0
			list4[1]=list4[1]+float(list2[3])	#1
			list4[2]=list4[2]+float(list2[4])	#2
			list4[3]=list4[3]+float(list2[5])	#3
			list4[4]=list4[4]+float(list2[6])	#4
			list4[5]=list4[5]+float(list2[7])	#6
			list4[6]=list4[6]+float(list2[8])	#balls
			counter=counter+1
		else :
            
			list4[0]=list4[0]+float(list2[2])	#0
			list4[1]=list4[1]+float(list2[3])	#1
			list4[2]=list4[2]+float(list2[4])	#2
			list4[3]=list4[3]+float(list2[5])	#3
			list4[4]=list4[4]+float(list2[6])	#4
			list4[5]=list4[5]+float(list2[7])	#6
			list4[6]=list4[6]+float(list2[8])	#balls
			counter=counter+1
			#f.write(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
			list4[0]=float(list4[0])/counter
			list4[1]=float(list4[1])/counter
			list4[2]=float(list4[2])/counter
			list4[3]=float(list4[3])/counter
			list4[4]=float(list4[4])/counter
			list4[5]=float(list4[5])/counter
			list4[6]=int(list4[6])
            
            
			f.write(str(list1[0])+","+str(list1[1])+","+str(list4[0])+","+str(list4[1])+","+str(list4[2])+","+str(list4[3])+","+str(list4[4])+","+str(list4[5])+","+str(list4[6])+"\n")
			list4=[0,0,0,0,0,0,0]
			counter=0
	else :
        
		list4[0]=list4[0]+float(list2[2])	#0
		list4[1]=list4[1]+float(list2[3])	#1
		list4[2]=list4[2]+float(list2[4])	#2
		list4[3]=list4[3]+float(list2[5])	#3
		list4[4]=list4[4]+float(list2[6])	#4
		list4[5]=list4[5]+float(list2[7])	#6
		list4[6]=list4[6]+float(list2[8])	#balls
		counter=counter+1
		#f.write(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
            
		list4[0]=float(list4[0])/counter
		list4[1]=float(list4[1])/counter
		list4[2]=float(list4[2])/counter
		list4[3]=float(list4[3])/counter
		list4[4]=float(list4[4])/counter
		list4[5]=float(list4[5])/counter
		list4[6]=int(list4[6])
            
            
		f.write(str(list1[0])+","+str(list1[1])+","+str(list4[0])+","+str(list4[1])+","+str(list4[2])+","+str(list4[3])+","+str(list4[4])+","+str(list4[5])+","+str(list4[6])+"\n")
		list4=[0,0,0,0,0,0,0]
		counter=0

print(list4)
print(list2)


list3=[]

line3=lines[len(lines)-1]
list3=line3.split(',')
list3[2]=float(list3[2])
#print(list4)
if list3[0]==list2[0]:
	if list3[1]==list2[1]:
        
		list4[0]=list4[0]+float(list2[2])	#0
		list4[1]=list4[1]+float(list2[3])	#1
		list4[2]=list4[2]+float(list2[4])	#2
		list4[3]=list4[3]+float(list2[5])	#3
		list4[4]=list4[4]+float(list2[6])	#4
		list4[5]=list4[5]+float(list2[7])	#6
		list4[6]=list4[6]+float(list2[8])	#balls
		counter=counter+1
	else :
           
		list4[0]=list4[0]+list2[2]	#0
		list4[1]=list4[1]+list2[3]	#1
		list4[2]=list4[2]+list2[4]	#2
		list4[3]=list4[3]+list2[5]	#3
		list4[4]=list4[4]+list2[6]	#4
		list4[5]=list4[5]+list2[7]	#6
		list4[6]=list4[6]+list2[8]	#balls
		counter=counter+1
		#f.write(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
            
		list4[0]=float(list4[0])/counter
		list4[1]=float(list4[1])/counter
		list4[2]=float(list4[2])/counter
		list4[3]=float(list4[3])/counter
		list4[4]=float(list4[4])/counter
		list4[5]=float(list4[5])/counter
		list4[6]=int(list4[6])
            
            
		f.write(str(list1[0])+","+str(list1[1])+","+str(list4[0])+","+str(list4[1])+","+str(list4[2])+","+str(list4[3])+","+str(list4[4])+","+str(list4[5])+","+str(list4[6])+"\n")
		list4=[0,0,0,0,0,0,0]
		counter=0
else :
       
	list4[0]=list4[0]+float(list2[2])	#0
	list4[1]=list4[1]+float(list2[3])	#1
	list4[2]=list4[2]+float(list2[4])	#2
	list4[3]=list4[3]+float(list2[5])	#3
	list4[4]=list4[4]+float(list2[6])	#4
	list4[5]=list4[5]+float(list2[7])	#6
	list4[6]=list4[6]+float(list2[8])	#balls
	counter=counter+1
	#f.write(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
            
	list4[0]=float(list4[0])/counter
	list4[1]=float(list4[1])/counter
	list4[2]=float(list4[2])/counter
	list4[3]=float(list4[3])/counter
	list4[4]=float(list4[4])/counter
	list4[5]=float(list4[5])/counter
	list4[6]=int(list4[6])
            
            
	f.write(str(list1[0])+","+str(list1[1])+","+str(list4[0])+","+str(list4[1])+","+str(list4[2])+","+str(list4[3])+","+str(list4[4])+","+str(list4[5])+","+str(list4[6])+"\n")
	list4=[0,0,0,0,0,0,0]
	counter=0

f.write(str(list1[0])+","+str(list1[1])+","+str(list4[0])+","+str(list4[1])+","+str(list4[2])+","+str(list4[3])+","+str(list4[4])+","+str(list4[5])+","+str(list4[6])+"\n")

f.close()
inF.close()
