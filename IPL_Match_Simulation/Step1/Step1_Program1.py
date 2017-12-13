list1=[]
list2=[]
f = open('player_vs_player_info.txt', 'w')
y=open('player_vs_player_wickets.txt','w')
list_ip=['980901.txt','980903.txt','980905.txt','980907.txt','980909.txt','980911.txt','980913.txt','980915.txt','980917.txt','980919.txt','980921.txt','980923.txt','980925.txt','980927.txt','980929.txt','980931.txt','980933.txt','980935.txt','980937.txt','980939.txt','980941.txt','980943.txt','980945.txt','980947.txt','980949.txt','980951.txt','980953.txt','980955.txt','980957.txt','980959.txt','980961.txt','980963.txt','980965.txt','980967.txt','980969.txt','980971.txt','980973.txt','980975.txt','980977.txt','980979.txt','980981.txt','980983.txt','980985.txt','980987.txt','980989.txt','980991.txt','980993.txt','980995.txt','980997.txt','980999.txt','981001.txt','981003.txt','981005.txt','981007.txt','981009.txt','981011.txt','981013.txt','981015.txt','981017.txt','981019.txt']

for file in list_ip:
    with open(file, 'r') as inF:
        for line in inF :
            list1=[]
            list2=[]
            list3=[]
            print(line)
            #list1=line.strip(',').split()
            list1=line.split(',')
            if list1[0]=='ball':
                print(list1)
                list2.append(list1[4])
                list2.append(list1[6])
                list2.append(list1[7])
                f.write(",".join(str(x) for x in list2))
            #f.write(str(list2))  # python will convert \n to os.linesep
                f.write('\n')
                if list1[9]!='""' :
                    list3.append(list1[4])
                    list3.append(list1[6])
                    list3.append('1')
                    y.write(",".join(str(x) for x in list3))
                    y.write('\n')

f.close()

