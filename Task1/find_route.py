#NAME - DEEPTHI CHILUKA
#ID - 1002028543

import sys

#reading a file in folder
def explore(filename):
    eGraph = []
    folder = open(filename,"r")
   
    for b in folder:
        input_data = b.rstrip('\n').split(" ")
        if input_data!= ['END', 'OF', 'INPUT'] or input_data!=[""]:
            eGraph.append(input_data)
    
    return eGraph



#This is for displaying path  
        
def show(expand_nodes, generate_nodes, d1, s, end):
    
    if d1 == "infinity":
        print("nodes expanded: {}".format(expand_nodes))
        print("nodes generated: {}".format(generate_nodes))
        print("d1: {}".format(d1))
        print("path:\none")
    else:
        print("nodes expanded:{}".format(expand_nodes))
        print("nodes generated: {}".format(generate_nodes))
        print("d1: {} km".format(d1))
        find_route(s, end, d1)
   #finding the path from start to end     
def generate_route(cost, begin, finish, heuristic):
    closed_set = set()
    generate_nodes = 0
    frnge= [] 
    s = []
    expand_nodes = []
    frnge.append([begin, None, 0.0, 0, 0.0])
    s.append([begin, None, 0.0, 0, 0.0])
    generate_nodes+=1
    temp = begin
    done = False

    while not done:
        if not frnge:
            return False
        expand_nodes.append(temp)
        main_cost = float(frnge[0][4])
        prev_depth = frnge[0][3]
        frnge.pop(0)
        if str(temp) not in closed_set:
            for i in cost:
                if temp in i:
                    generate_nodes+=1
                    a =[cost.index(i),i.index(temp)]
                    if a[1] == 0:
                        generated_state = cost[cost.index(i)][1]
                        main_branch = temp
                        depth = prev_depth +1
                      
                        for j in heuristic:
                            if generated_state in j:
                                heuristic_value = float(heuristic[heuristic.index(j)][1])
                        original_cost = main_cost + float(cost[cost.index(i)][2])
                        progressive_cost = heuristic_value + main_cost + float(cost[cost.index(i)][2])
                        frnge.append([generated_state, main_branch, progressive_cost, depth, original_cost])
                        s.append([generated_state, main_branch, progressive_cost, depth, original_cost])
                    elif a[1] == 1:
                        generated_state = cost[cost.index(i)][0]
                        main_branch = temp
                        depth = prev_depth +1
                        for j in heuristic:
                            if str(generated_state) in j:
                                heuristic_value = float(heuristic[heuristic.index(j)][1])
                        original_cost = main_cost + float(cost[cost.index(i)][2])
                        progressive_cost = heuristic_value + main_cost + float(cost[cost.index(i)][2])
                        frnge.append([generated_state, main_branch, progressive_cost, depth, original_cost])
                        s.append([generated_state, main_branch, progressive_cost, depth, original_cost])
        closed_set.add(temp)
        frnge= sorted(frnge,key=lambda x: x[2])

        if not frnge:
            d1 = "infinity"
            count_expanded = len(expand_nodes)
        else:
            
            temp = str(frnge[0][0])
            d1 = frnge[0][2] 
            count_expanded= len(expand_nodes) + 1

        if temp == finish or d1 == "infinity":
            show(count_expanded,generate_nodes, d1, s, finish)
            done = True

def find_route(s, end, d1):
    path = []
    for i in s:
        if end in i and d1 in i:
            path.append(i)
    for i in range(path[0][3]-1):
        for j in s:
            if path:
                if path[-1][1] in j and path[-1][3] - 1 in j:
                    path.append(j)
    path.reverse()
    print("final path is seen as:")

    if entire_args == 4:
        for i in range(len(path)):
            if i > 0:
                print("{} to {}, {} km".format(path[i][1],path[i][0],path[i][2] - path[i-1][2]))
            else:
                print("{} to {}, {} km".format(path[i][1],path[i][0],path[i][2]))
    
    elif entire_args == 5:
        for i in range(len(path)):
            if i > 0:
                print("{} to {}, {} km".format(path[i][1],path[i][0],path[i][4] - path[i-1][4]))
            else:
                print("{} to {}, {} km".format(path[i][1],path[i][0],path[i][4]))
    return None

 
agmnts = sys.argv
cost = explore(str(agmnts[1]))
strt = str(agmnts[2])
stop = str(agmnts[3])
entire_args = len(agmnts)


if entire_args == 4:
    heuristic=[]
    city=set()
    for k, l, m in cost:
        city.add(k)
        city.add(l)
    
    for u in city:
        heuristic.append([u,0])
    generate_route(cost, strt, stop, heuristic)

elif entire_args == 5:
    heuristic = explore(str(agmnts[4]))
    generate_route(cost, strt, stop, heuristic)

elif entire_args > 5:
    print("Invalid arguments")


