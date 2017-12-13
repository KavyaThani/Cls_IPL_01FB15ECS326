import random

def Search_Batsman(Batsman_name):
    if Batsman_name in Batlist0:
	    return 0
    if Batsman_name in Batlist1:
        return 1
    if Batsman_name in Batlist2:
        return 2
    if Batsman_name in Batlist3:
        return 3
    if Batsman_name in Batlist4:
        return 4
    if Batsman_name in Batlist5:
        return 5
    if Batsman_name in Batlist6:
        return 6
    if Batsman_name in Batlist7:
        return 7
    if Batsman_name in Batlist8:
        return 8
    if Batsman_name in Batlist9:
        return 9

def Search_Bowler(Bowler_name):
	if Bowler_name in Blist0:
		return 0
	if Bowler_name in Blist1:
		return 1
	if Bowler_name in Blist2:
		return 2
	if Bowler_name in Blist3:
		return 3
	if Bowler_name in Blist4:
		return 4
	if Bowler_name in Blist5:
		return 5
	if Bowler_name in Blist6:
		return 6
	if Bowler_name in Blist7:
		return 7
	if Bowler_name in Blist8:
		return 8
	if Bowler_name in Blist9:
		return 9

def predict_Wickets(Batsman1,Bowler,p):
    Batsmen_clus=Search_Batsman(Batsmen1)
    Bowler_clus=Search_Bowler(Bowler)
    b1=open("player_vs_player_probability_wickets4",'r')
    lines = b1.readlines()
    #print("Batsmen {0} and no = {1} : ".format(Batsmen1,Batsmen_clus))

    list6=[]
    for i in range(len(lines)):
        list6=lines[i].split(',')
        #print(list6)
        if ((Batsmen_clus==int(list6[0]))and(Bowler_clus==int(list6[1]))):
            #print("Hello ",Batsmen1)
            n=1-float(list6[2])
            wick=0
            wick=n*p
            #print(wick)
            return wick
    return 1.0

def random_pick(list, probabilities) :

	x = random.uniform(0,sum(probabilities))
	probability = 0.0
	for run, run_probability in zip(list, probabilities):
		probability += run_probability
		if x < probability: break
	return run

def predict_Runs(Batsmen1,Bowlers):
    status=0
    Runs=0
    a2=open("Data1.txt",'r')
    lines=a2.readlines()
    for i in range(len(lines)):
        list2=[]
        list2=lines[i].split(',')
        if (list2[0]==Batsmen1)and(list2[1]==Bowler):
            #print("Hello")
            status=1
            list_values=[0,1,2,3,4,6]
            list_prob=[]
            for l in range(4,10):
                list_prob.append((float(list2[l]))/float(list2[3]))
            Runs=random_pick(list_values,list_prob)

    if status==0:
        Batsmen_clus=Search_Batsman(Batsmen1)
        Bowler_clus=Search_Bowler(Bowler)
        lines=a1.readlines()
        #print("Batsmen {0} and no = {1} : ".format(Batsmen1,Batsmen_clus))
        for i in range(len(lines)):
            list2=[]
            list2=lines[i].split(',')
            if (int(list2[0])==Batsmen1)and(int(list2[1])==Bowler):
                status=1
                list_values=[0,1,2,3,4,6]
                list_prob=[]
                for l in range(2,8):
                    list_prob.append(float(list2[l]))
                Runs=random_pick(list_values,list_prob)
        if status==0:
            x=random.randrange(0,3)
            if x==5:
                x=random.randrange(0,3)
            Runs=x
    return Runs





f=open("dd_kkr.txt",'r')
f=open('Troops.txt', 'r')

#f=open('ipl7.txt','r')

x = 'BatsmenCluster11.txt'
y = 'BowlingCluster11.txt'
a1=open("player_vs_player_probability3",'r')
a2=open("player_vs_player_separate",'r')
f6=open("MatchSummary789.txt",'w')

Team1_BatsmenTroop=[]
Team2_BatsmenTroop=[]
Team1_BowlersTroop=[]
Team2_BowlersTroop=[]
for line in f:
    list1=[]
    list1=line.split(',')
    if line=='END\n':
        break
    #print(list1)
    Team1_BatsmenTroop.append(list1[0])
    Team2_BatsmenTroop.append(list1[2])
    if list1[1]!='':
        Team1_BowlersTroop.append(list1[1])
    if list1[3]!='\n':
        list1[3]=list1[3].strip()
        Team2_BowlersTroop.append(list1[3])

print(Team1_BatsmenTroop)
print(Team1_BowlersTroop)
print(Team2_BatsmenTroop)
print(Team2_BowlersTroop)
f.close()

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


with open(x, 'r') as inF:
    for line in inF :
        list1=[]
        list1=line.split(',')
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

Ballsfaced_Team1=0
TotalRuns_Team1=0
Runs_Team1=[]
BatsmenNum_Team1=0
BowlerNum_Team1=0
Batsmen1=Team1_BatsmenTroop[BatsmenNum_Team1]
Batsmen2=Team1_BatsmenTroop[BatsmenNum_Team1+1]
Bowler=Team2_BowlersTroop[BowlerNum_Team1]
Wickets_Team1=0
wickets_status_Team1=[]

for i in range(len(Team1_BatsmenTroop)):
    wickets_status_Team1.append(1.0)
while Ballsfaced_Team1<120:

    z=Team1_BatsmenTroop.index(Batsmen1)
    z1=wickets_status_Team1[z]
    Wickets1=1.0
    Wickets1=predict_Wickets(Batsmen1,Bowler,z1)
    wickets_status_Team1[z]=Wickets1
    if Wickets1<0.5:
        Wickets_Team1=Wickets_Team1+1
        BatsmenNum_Team1=BatsmenNum_Team1+1
        Batsmen1=Team1_BatsmenTroop[BatsmenNum_Team1]
    Ballsfaced_Team1=Ballsfaced_Team1+1
    run=1
    run=predict_Runs(Batsmen1,Bowler)
    Runs_Team1.append(run)
    TotalRuns_Team1=TotalRuns_Team1+run
    print("---------------------------------------------------------")
    print("Balls : ",Ballsfaced_Team1)
    print("Batsmen on strike : ",Batsmen1)
    print("Bowlers : ",Bowler)
    print("Runs Hit : ",run)
    print("Wickets : ",Wickets_Team1)
    print("Total Runs : ",TotalRuns_Team1)
    print("----------------------------------------------------------")
    f6.write("\n-----------------------------------------------------------------------------------------------------\n")
    f6.write("Balls : {0}".format(Ballsfaced_Team1)),
    f6.write(", Batsmen On strike : {0}".format(Batsmen1)),
    f6.write(", Batsmen off strike : {0}".format(Batsmen2)),
    f6.write(", Bowler : {0}".format(Bowler)),
    f6.write(", Runs hit : {0}".format(run)),
    f6.write(", Wickets : {0}".format(Wickets_Team1)),
    f6.write(", Total Runs : {0}".format(TotalRuns_Team1))

    if Ballsfaced_Team1%6==0:
        Batsmen1,Batsmen2=Batsmen2,Batsmen1
        BowlerNum_Team1=(BowlerNum_Team1+1)%len(Team2_BowlersTroop)
        Bowler=Team2_BowlersTroop[BowlerNum_Team1]

    if run==3 | run==1:
        Batsmen1,Batsmen2=Batsmen2,Batsmen1

    if Wickets_Team1==10:
        break

print("---------------------------------------------")
print("Innings 1 OVER")
print("The Total Runs of Team 1 is : ",TotalRuns_Team1)
print("Wickets : ",Wickets_Team1)
print("Total Balls Faced : ",Ballsfaced_Team1)
print("Target for Team 2 : ",TotalRuns_Team1+1)
print("----------------------------------------------")
f6.write("\n\n______________________________________________________________________________________________________________")
f6.write("\n-----INNINGS 1 OVER-----------\n")
f6.write("Total Runs : {0}, Wickets : {1}, Balls faced : {2}\n".format(TotalRuns_Team1,Wickets_Team1,Ballsfaced_Team1))
f6.write("Target for Team 2 : {0}".format(TotalRuns_Team1+1))
f6.write("\n______________________________________________________________________________________________________________\n\n")



Target_Score=TotalRuns_Team1+1

Ballsfaced_Team2=0
TotalRuns_Team2=0
Runs_Team2=[]
BatsmenNum_Team2=0
BowlerNum_Team2=0
Batsmen1=Team2_BatsmenTroop[BatsmenNum_Team2]
Batsmen2=Team2_BatsmenTroop[BatsmenNum_Team2+1]
Bowler=Team1_BowlersTroop[BowlerNum_Team2]
Wickets_Team2=0
wickets_status_Team2=[]

for i in range(len(Team2_BatsmenTroop)):
    wickets_status_Team2.append(1.0)
while Ballsfaced_Team2<120:

    z=Team2_BatsmenTroop.index(Batsmen1)
    #print("z = ",z)
    z1=wickets_status_Team2[z]
    #print("z1 = ",z1)
    Wickets1=predict_Wickets(Batsmen1,Bowler,z1)
    #print("Wickets = ",Wickets1)
    wickets_status_Team2[z]=Wickets1
    if Wickets1<0.8:
        Wickets_Team2=Wickets_Team2+1
        BatsmenNum_Team2=BatsmenNum_Team2+1
        Batsmen1=Team2_BatsmenTroop[BatsmenNum_Team2]
    Ballsfaced_Team2=Ballsfaced_Team2+1
    run=predict_Runs(Batsmen1,Bowler)
    Runs_Team2.append(run)
    TotalRuns_Team2=TotalRuns_Team2+run
    print("---------------------------------------------------------")
    print("Balls : ",Ballsfaced_Team2)
    print("Batsmen on strike : ",Batsmen1)
    print("Bowlers : ",Bowler)
    print("Runs Hit : ",run)
    print("Wickets : {0}",Wickets_Team2)
    print("Total Runs : ",TotalRuns_Team2)
    print("----------------------------------------------------------")
    f6.write("Balls : {0}".format(Ballsfaced_Team2)),
    f6.write(", Batsmen On strike : {0}".format(Batsmen1)),
    f6.write(", Batsmen off strike : {0}".format(Batsmen2)),
    f6.write(", Bowler : {0}".format(Bowler)),
    f6.write(", Runs hit : {0}".format(run)),
    f6.write(", Wickets : {0}".format(Wickets_Team2)),
    f6.write(", Total Runs : {0}\n".format(TotalRuns_Team2))
    f6.write("----------------------------------------------------------------------------------------------------\n")

    if Ballsfaced_Team2%6==0:
        Batsmen1,Batsmen2=Batsmen2,Batsmen1
        BowlerNum_Team2=(BowlerNum_Team2+1)%len(Team1_BowlersTroop)
        Bowler=Team1_BowlersTroop[BowlerNum_Team2]

    if run==3 | run==1:
        Batsmen1,Batsmen2=Batsmen2,Batsmen1

    if Wickets_Team2==10:
        break

    if TotalRuns_Team2>=Target_Score :
        break

print("---------------------------------------------")
print("Innings 2 OVER")
print("The Total Runs of Team 2 is : ",TotalRuns_Team2)
print("Wickets : ",Wickets_Team2)
print("Total Balls Faced : ",Ballsfaced_Team2)
print("----------------------------------------------")
f6.write("\n____________________________________________________________________________________________________________")
f6.write("\n-----INNINGS 2 OVER-----------\n")
f6.write("Total Runs : {0}, Wickets : {1}, Balls faced : {2}\n".format(TotalRuns_Team2,Wickets_Team2,Ballsfaced_Team2))
f6.write("\n_____________________________________________________________________________________________________________\n\n")

print("-----------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------")
print("Match Summary")
print("Team 1 :- Total Runs : ",TotalRuns_Team1)
print("Team 2 :- Total Runs : ",TotalRuns_Team2)
if TotalRuns_Team1>TotalRuns_Team2:
    print("Team 1 Wins")
    print("Team 1 wins by ",TotalRuns_Team1-TotalRuns_Team2," Runs")
    f6.write("\n\n\nTeam 1 Wins by {0} Runs".format(TotalRuns_Team1-TotalRuns_Team2))
elif TotalRuns_Team1<TotalRuns_Team2:
    print("Team 2 Wins")
    print("Team 2 wins by ",10-Wickets_Team2," wickets")
    f6.write("\n\n\nTeam 2 wins by {0} Wickets".format(10-Wickets_Team2))
else :
    print("DRAW MATCH!!!!")
    f6.write("\n\n\nDRAW MATCH")










