import operator;
with open('player_vs_player_Probability_wickets1.txt') as f:
    lines = [line.split(',') for line in f]
output = open("player_vs_player_Probability_wickets2.txt", 'w')

for line in sorted(lines):
    #output.write(' '.join(line), key=operator.itemgetter(0))
#for line in sorted(lines, key=lambda line: line.split()[0]):
    output.write(",".join(str(x) for x in line))
    #output.write('\n')

output.close()
