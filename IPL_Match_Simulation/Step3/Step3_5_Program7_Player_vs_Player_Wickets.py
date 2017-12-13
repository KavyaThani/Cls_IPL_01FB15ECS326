import operator;
list1=[]
list2=[]
x ='player_vs_player_Probability3.txt'
y=open('player_vs_player_Probability_wickets4.txt','w')
list_ip=[x]
list2=[]
counter=0
for file in list_ip:
	with open(file, 'r') as inF:
		for line in inF :
			list1=[]
			list1=line.split(',')
			list2.append(list1[8])


with open('player_vs_player_Probability_wickets3.txt') as f:
	for line in f:
		list1=[]
		list1=line.split(',')
		list1[2]=float(list1[2])/float(list2[counter])
		counter=counter+1

		y.write(str(list1[0])+","+str(list1[1])+","+str(list1[2])+"\n")
y.close()

