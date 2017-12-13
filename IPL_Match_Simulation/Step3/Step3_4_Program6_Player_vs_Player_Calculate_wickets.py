f = open('player_vs_player_Probability_wickets3.txt', 'w')
inF = open('player_vs_player_Probability_wickets2.txt', 'r')
lines = inF.readlines()
w=0
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
    
	if list1[0]==list2[0]:
		if list1[1]==list2[1]:
           
			w=w+float(list2[2])	#0
			counter=counter+1
		else :
            
			w=w+float(list2[2])	#0
			counter=counter+1
			#f.write(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
			w=float(w)/counter           
            
			f.write(str(list1[0])+","+str(list1[1])+","+str(w)+"\n")
			w=0
			counter=0
	else :
        
		w=w+float(list2[2])	#0
		counter=counter+1
		#f.write(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
            
		w=float(w)/counter         
            
		f.write(str(list1[0])+","+str(list1[1])+","+str(w)+"\n")
		w=0
		counter=0



list3=[]

line3=lines[len(lines)-1]
list3=line3.split(',')
list3[2]=float(list3[2])
#print(list4)
if list3[0]==list2[0]:
	if list3[1]==list2[1]:
        
		w=w+float(list2[2])	#0
		counter=counter+1
	else :
           
		w=w+list2[2]	#0
		counter=counter+1
		#f.write(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
            
		w=float(w)/counter
            
		f.write(str(list1[0])+","+str(list1[1])+","+str(w)+"\n")
		w=0
		counter=0
else :
       
	w=w+float(list2[2])	#0
	counter=counter+1
	#f.write(str(list1[0])+","+str(list1[1])+","+str(list4)+"\n")
            
	w=float(w)/counter            
            
	f.write(str(list1[0])+","+str(list1[1])+","+str(w)+"\n")
	w=0
	counter=0

f.write(str(list1[0])+","+str(list1[1])+","+str(w)+"\n")

f.close()
inF.close()
