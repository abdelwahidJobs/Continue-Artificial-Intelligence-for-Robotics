


#!/usr/bin/python
sensor_right=0.7
p_move=0.8 
sensor_wrong = 1.0 - sensor_right 
p_stay = 1.0 - p_move 
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

def sense(p, colors, measurement):
    aux=[[0.0 for row in range(len(p[0]))] for col  in range(len(p))]
    s=0.0 
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit=(measurement==colors[i][j])
            aux[i][j]=p[i][j]*(hit * sensor_right +(1- hit) * sensor_wrong)
            s +=aux[i][j]

    for i in range(len(aux)):
        for j in range(len(p[i])):
            aux[i][j]/= s 
    return aux
def move(p , motion ):
    aux =[[0.0 for row in range(len(p[0]))] for col in range(len(p))]

    for i in range(len(p)):
        for x in range(len(p[i])):
            aux[i][x]= (p_move * p[(i - motion[0]) % len(p)][(x - motion[1]) % len(p[i])]) + (p_stay *p[i][x])
    return aux

#def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
 #   pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
  #  p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    # >>> Insert your code here <<<
   
    
   # return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'
    


colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]

pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
p =[[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
for x in range(len(measurements)):
    p=move(p,motions[x])
    p=sense(p,colors,measurements[x])





show(p) # displays your answer
