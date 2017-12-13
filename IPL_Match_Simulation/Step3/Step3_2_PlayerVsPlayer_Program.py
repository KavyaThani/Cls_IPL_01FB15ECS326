f = 'player_vs_player_information3.txt'
x = 'BatsmenCluster.txt'
y = 'BowlingCluster.txt'
z = open('player_vs_player_Probability1.txt', 'w')

Batlist0=[]
Batlist1=[]
Batlist2=[]
Batlist3=[]
Batlist4=[]
Batlist5=[]
Batlist6=[]
Batlist7=[]
Batlist8=[]
Batlist9=[]

Blist0=[]
Blist1=[]
Blist2=[]
Blist3=[]
Blist4=[]
Blist5=[]
Blist6=[]
Blist7=[]
Blist8=[]
Blist9=[]

def Search_Batsman(Batsman_name):
	if Batsman_name in Batlist0:
		return 0;
	if Batsman_name in Batlist1:
		return 1;
	if Batsman_name in Batlist2:
		return 2;
	if Batsman_name in Batlist3:
		return 3;
	if Batsman_name in Batlist4:
		return 4;
	if Batsman_name in Batlist5:
		return 5;
	if Batsman_name in Batlist6:
		return 6;
	if Batsman_name in Batlist7:
		return 7;
	if Batsman_name in Batlist8:
		return 8;
	if Batsman_name in Batlist9:
		return 9;

def Search_Bowler(Bowler_name):
	if Bowler_name in Blist0:
		return 0;
	if Bowler_name in Blist1:
		return 1;
	if Bowler_name in Blist2:
		return 2;
	if Bowler_name in Blist3:
		return 3;
	if Bowler_name in Blist4:
		return 4;
	if Bowler_name in Blist5:
		return 5;
	if Bowler_name in Blist6:
		return 6;
	if Bowler_name in Blist7:
		return 7;
	if Bowler_name in Blist8:
		return 8;
	if Bowler_name in Blist9:
		return 9;
	

with open(x, 'r') as inF:
	for line in inF :
		list1=[]
		list1=line.split(',')
		#print(list1)
		list1[14]=int(list1[14])
		if list1[14]==0:
			Batlist0.append(list1[0])
		if list1[14]==1:
			Batlist1.append(list1[0])
		if list1[14]==2:
			Batlist2.append(list1[0])
		if list1[14]==3:
			Batlist3.append(list1[0])
		if list1[14]==4:
			Batlist4.append(list1[0])
		if list1[14]==5:
			Batlist5.append(list1[0])
		if list1[14]==6:
			Batlist6.append(list1[0])
		if list1[14]==7:
			Batlist7.append(list1[0])
		if list1[14]==8:
			Batlist8.append(list1[0])
		if list1[14]==9:
			Batlist9.append(list1[0])

with open(y, 'r') as inF:
	for line in inF :
		list1=[]
		list1=line.split(',')
		#print(list1)
		list1[13]=int(list1[13])
		#print(list1[13])
		if list1[13]==0:
			Blist0.append(list1[0])
		if list1[13]==1:
			Blist1.append(list1[0])
		if list1[13]==2:
			Blist2.append(list1[0])
		if list1[13]==3:
			Blist3.append(list1[0])
		if list1[13]==4:
			Blist4.append(list1[0])
		if list1[13]==5:
			Blist5.append(list1[0])
		if list1[13]==6:
			Blist6.append(list1[0])
		if list1[13]==7:
			Blist7.append(list1[0])
		if list1[13]==8:
			Blist8.append(list1[0])
		if list1[13]==9:
			Blist9.append(list1[0])


with open(f, 'r') as inF:
	for line in inF :
		list1=[]
		list1=line.split(',')
		#print(list1)
		
		a=Search_Batsman(list1[0])
		print(list1[0])
		b=Search_Bowler(list1[1])
		list2=[]
		list2.append(a)
		list2.append(b)

		#0's
		list2.append(int(list1[4])/int(list1[3]))
		#1's
		list2.append(int(list1[5])/int(list1[3]))
		#2's
		list2.append(int(list1[6])/int(list1[3]))
		#3's
		list2.append(int(list1[7])/int(list1[3]))
		#4's
		list2.append(int(list1[8])/int(list1[3]))
		#6's
		list2.append(int(list1[9])/int(list1[3]))
		#Balls
		list2.append(int(list1[3]))
		z.write(",".join(str(x) for x in list2))
		z.write("\n")
	
		
          

z.close()
