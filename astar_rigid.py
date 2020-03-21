import numpy as np
import matplotlib.pyplot as plt
import time
import math
import sys
blank_list = []
for entries in range(2880000):
    entries = math.inf
    blank_list.append(entries)
cost_matrix = np.array(blank_list, dtype = object).reshape(400,600,12)

blank_list1 = []
for entries in range(2880000):
    entries = 0
    blank_list1.append(entries)
visited_mat = np.array(blank_list, dtype = object).reshape(400,600,12)

blank_list2 = []
for entries in range(2880000):
    entries = 0
    blank_list2.append(entries)
cost_2_come = np.array(blank_list, dtype = object).reshape(400,600,12)


def approximation(a):
    b = math.ceil(a)
    if b - a <= 0.75 and b - a >= 0.25:
        a = b - 0.5
    elif b - a > 0.75 and b - a <= 1:
        a = math.floor(a)
    elif b - a < 0.25 and b - a >=0:
        a = b
    else:
        return a 
    return a


def angle_approximation(a):
    if (a < 30 and a >= 15) or (a >= -30 and a < -15):
        return 1
    elif a >= 0 and a < 15 or a < 0 and a >= -15 :
        return 0
    else:
        a = a/30
        b = a%math.floor(a)
        if b <= 0.5:
            a = math.floor(a)
        else:
            a = math.ceil(a)
        return a

orientation = 2                   #int(input())
k = orientation
# k = angle_approximation(k) 
d = 6

#d = int(input())

ind1 = 50  #int(input('enter x coordinate of starting node'))  # 5
ind2 = 30  #int(input('enter y coordinate of starting node'))  # 5
ind = (ind1,200 - ind2,orientation)

goal1 = 150  #int(input('enter x coordinate of goal node'))  # 295
goal2 = 150  #int(input('enter y coordinate of goal node'))  # 195 
goal = (goal1,200 - goal2)



cost_matrix[2*ind[0]][2*ind[1]][ind[2]] = 0
cost_2_come[2*ind[0]][2*ind[1]][orientation] = 0


r = 1
c = 1

b = r+c

def obstacle_here(x,y): 
    
    if (y>=(3/5)*x+25-b) and (y>=(-3/5)*x+295-b):
        return True
    
    if (y>=(3/5)*x+55+b) or (y>=(-3/5)*x+325+b):
        return False
    
    if (x-225)**2+(y-50)**2<=(25+b)**2:
        return True
    
    if (x-150)**2/(40+b)**2+(y-100)**2/(20+b)**2<=1:
        return True

    if (((x>=30.875 and x<=35.875) and (y>=((-1.71)*x+196.84-b))) or ((x>=35.875 and x<=100) and (y>=((0.53)*x+108.45-b)))):
        return True
        
    if ((x>=30.875 and x<=95) and (y>=((0.5380)*x+118.99+b))) or ((x>=95 and x<=100) and (y>=((-1.71)*x+332.45+b))):
        return False
        
    if (y>=(-7/5)*x+120 and y>=(7/5)*x-(90+b)) and (y<=(6/5)*x-10+b and y<=(-6/5)*x+170+b) :
        return True
        
    if (y<=(-7/5)*x+120) and y<=(7/5)*x-20 and y>=15-b:
        return True
        
    if y>=(7/5)*x-20 and y>=(-13)*x+340+b and y<=(-1)*x+100+b:
        return True
       
    if (y>=0 and y<=0+b):
        return True
        
    if (y<=200 and y>=(200-b)):
        return True
        
    if (x>=0 and x<=b):
        return True
        
    if (x<=300 and x>=(300-b)):
        return True
    

if obstacle_here(ind[0],ind[1]):
    print("yes1")
    sys.exit()
if obstacle_here(goal[0],goal[1]):
    print("yes2")
    sys.exit()

    

def straight(i, j, k):
    
    if obstacle_here(i,j):
        return None
    
    
    else:
        
        i1 = i + d*math.sin(math.radians(k*30))
        j1 = j + d*math.cos(math.radians(k*30))
        
        heuristic = abs(goal[0] - i1) + abs(goal[1] - j1)
        
        i1 = approximation(i1)
        j1 = approximation(j1)
        
        k2 = k*30                      # how to store value of orientation
        k1 = angle_approximation(k2)
        if k1 > 11:  ## convert more than 360 to positive
            k1 = 1
        if j1 >= 300 or i1 >= 200 or i1 <= 0 or j1 <= 0:
            return None
               
            
        cost_2_come[int(2*i1)][int(2*j1)][k1] = cost_2_come[int(2*i)][int(2*j)][k] + d
        cost = cost_2_come[int(2*i1)][int(2*j1)][k1] + heuristic
        
        
        return (i1,j1,k1), cost

def upfirst(i,j,k):
    
    if obstacle_here(i,j):
        return None
    
    
    else:
        
        i1 = i + d*math.sin(math.radians(30 + k*30))
        j1 = j + d*math.cos(math.radians(30 + k*30))
        
        heuristic = abs(goal[0] - i1) + abs(goal[1] - j1)
        
        i1 = approximation(i1)
        j1 = approximation(j1)
        
        k2 = k*30 + 30                     # how to store value of orientation
        k1 = angle_approximation(k2)
        if k1 > 11:  ## convert more than 360 to positive
            k1 = 0
        if j1 >= 300 or i1 >= 200 or i1 <= 0 or j1 <= 0:
            return None
           
        
        cost_2_come[int(2*i1)][int(2*j1)][k1] = cost_2_come[int(2*i)][int(2*j)][k] + d
        cost = cost_2_come[int(2*i1)][int(2*j1)][k1] + heuristic
        
        
        return (i1,j1,k1), cost



def upsecond(i, j, k): 
    
    if obstacle_here(i,j):
        return None
    
    
    else:
        
        i1 = i + d*math.sin(math.radians(60 + k*30))
        j1 = j + d*math.cos(math.radians(60 + k*30))
        
        heuristic = abs(goal[0] - i1) + abs(goal[1] - j1)
        
        i1 = approximation(i1)
        j1 = approximation(j1)
        
        k2 = k*30 + 60                     # how to store value of orientation
        k1 = angle_approximation(k2)
        if k1 > 11:  ## convert more than 360 to positive
            k1 = 1
        if j1 >= 300 or i1 >= 200 or i1 <= 0 or j1 <= 0:
            return None
           
        
        cost_2_come[int(2*i1)][int(2*j1)][k1] = cost_2_come[int(2*i)][int(2*j)][k] + d
        cost = cost_2_come[int(2*i1)][int(2*j1)][k1] + heuristic
        
        
        return (i1,j1,k1), cost


def downfirst(i,j,k):
    if obstacle_here(i,j):
        return None
    
    
    else:
        
        i1 = i + d*math.sin(-math.radians(30) + math.radians(k*30))
        j1 = j + d*math.cos(-math.radians(30) + math.radians(k*30))
        
        heuristic = abs(goal[0] - i1) + abs(goal[1] - j1)
        
        i1 = approximation(i1)
        j1 = approximation(j1)
        
        k2 = k*30 + 330
        k1 = angle_approximation(k2)
        if k1 > 11:  ## convert more than 360 to positive
            k1 = 0
        if j1 >= 300 or i1 >= 200 or i1 <= 0 or j1 <= 0:
            return None
           
        
        cost_2_come[int(2*i1)][int(2*j1)][k1] = cost_2_come[int(2*i)][int(2*j)][k] + d
        cost = cost_2_come[int(2*i1)][int(2*j1)][k1] + heuristic
        
        
        return (i1,j1,k1), cost

def downsecond(i,j,k):
    
    if obstacle_here(i,j):
        return None
    
    
    else:
        
        i1 = i + d*math.sin(-math.radians(60) + math.radians(k*30))
        j1 = j + d*math.cos(-math.radians(60) + math.radians(k*30))
        
        heuristic = abs(goal[0] - i1) + abs(goal[1] - j1)
        
        i1 = approximation(i1)
        j1 = approximation(j1)
        i = approximation(i)
        j = approximation(j)
        
        k2 = k*30 + 300                     # store value of orientation
        k1 = angle_approximation(k2)
        if k1 > 11:  ## convert more than 360 to positive
            k1 = 1
        if j1 >= 300 or i1 >= 200 or i1 <= 0 or j1 <= 0:
            return None
           
        
        cost_2_come[int(2*i1)][int(2*j1)][k1] = cost_2_come[int(2*i)][int(2*j)][k] + d
        cost = cost_2_come[int(2*i1)][int(2*j1)][k1] + heuristic
        
        
        return (i1,j1,k1), cost




def get_neighbours(i,j,k):
    neighbours_cost = []
    index = []
    action_straight = straight(i,j,k)
    if action_straight is not None:
        neighbours_cost.append(action_straight[1])
        index.append(action_straight[0])
    action_down = upfirst(i,j,k)
    if action_down is not None:
        neighbours_cost.append(action_down[1])
        index.append(action_down[0]) 
    action_left = upsecond(i,j,k)
    if action_left is not None:
        neighbours_cost.append(action_left[1])
        index.append(action_left[0])
    action_right = downfirst(i,j,k)
    if action_right is not None:
        neighbours_cost.append(action_right[1])
        index.append(action_right[0])    
    action_upright = downsecond(i,j,k)
    if action_upright is not None:
        neighbours_cost.append(action_upright[1])
        index.append(action_upright[0])
      
               
    return neighbours_cost, index

'''def get_current_value(i,j):
    current_value = cost_matrix[i][j]
    return current_value'''

'''def locate_value_index(mat):
    i,j = np.where(mat == node)
    i = int(i)
    j = int(j)
    return (i,j)'''


def sort_list1(list_a,list_b):
    list_b = [i[1] for i in sorted(zip(list_a, list_b))]
    
def sort_list2(list_a):
    list_a.sort()
    

node_cost = 0
cost_matrix[int(2*ind[0])][int(2*ind[1])][ind[2]] = 0

explore_queue = []  
index_queue = []
index_queue.append(ind)
explore_queue.append(node_cost)

breakwhile = False

start_time = time.clock()

visited_list = []
parent_map = {}
parent_map[ind] = None

while len(index_queue) != 0 and not breakwhile:
    node = index_queue[0]
    visited_mat[int(2*node[0])][int(2*node[1])][node[2]] = 1
    visited_list.append(node)

    print(index_queue[0], explore_queue[0])
    index_queue.pop(0)
    explore_queue.pop(0)
    pair = get_neighbours(node[0],node[1],node[2])
    #print('pair',pair)
    neighbours_cost = pair[0]
    index = pair[1]
    #print(index)
    #print(neighbours_cost)
    
    #######
    if math.sqrt((goal[0] - node[0])**2 + (goal[1] - node[1])**2) <= 1.5:
        print("goal reached")
        goal_ind = node
        breakwhile = True
    
    #######

    
    for i in range(len(index)):
        if not visited_mat[int(2*((index[i])[0]))][int(2*(index[i])[1])][index[i][2]] == 1:    
                                        
            old_cost = cost_matrix[int(2*(index[i])[0])][int(2*(index[i])[1])][index[i][2]]
            if neighbours_cost[i] < old_cost:
                cost_matrix[int(2*(index[i])[0])][int(2*(index[i])[1])][index[i][2]] = neighbours_cost[i]
                #if old_cost != math.inf:
                    #ind_node = index_queue.index((index[i][0], index[i][1]))
                    #index_queue.pop(ind_node)
                    #explore_queue.pop(ind_node)
                    
                index_queue.append(index[i])
                explore_queue.append(cost_matrix[int(2*(index[i])[0])][int(2*(index[i])[1])][index[i][2]])  # cost_matrix getting updated
                parent_map[index[i]] = node


       
            
    sort_list1(explore_queue,index_queue)
    sort_list2(explore_queue)
    visited_mat[int(2*node[0])][int(2*node[1])][node[2]] == 1
   

end_time = time.clock()
print(end_time - start_time)
 
path_list = []
parent = parent_map[goal_ind]
path_list.append(goal_ind)
while parent is not None:
    path_list.append(parent)
    parent = parent_map[parent]

#path_list.reverse()
print(path_list)
path_final = np.asarray(path_list)


plt.figure() # Create a new figure window
xlist = np.linspace(0, 300, 100) # Create 1-D arrays for x,y dimensions
ylist = np.linspace(0, 200, 100) 
x,y = np.meshgrid(xlist, ylist) # Create 2-D grid xlist,ylist values

#fig, (ax1) = plt.subplots()

F = (x-225)**2+(y-150)**2 - (25)**2  #  'Circle Equation
M = (x-150)**2/(40)**2+(y-100)**2/(20)**2 - 1
#C =  -13*y + 340 -x
#D =  x - 15 
#E =  x - 0.7*y + 65 
#G =  -0.83*y + 58.5 - x
#H =  0.83*y + 8.5 - x
#J =  -y + 100 - x

#L = (y>=(3/5)*x+55+b) 
plt.contour(x, y, F, [0], colors = 'k', linestyles = 'solid')
plt.contour(x, y, M, [0], colors = 'k', linestyles = 'solid')



x_coord = path_final[:,0]
y_coord = path_final[:,1]

#plt.scatter(x_coord, y_coord)
plt.plot(x_coord, y_coord)
plt.show()
