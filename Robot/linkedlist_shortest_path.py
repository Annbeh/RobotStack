from world import *
from linked_list import *
from linkedlist_stack import *

from pprint import pprint

world=create_world("world1.txt")
for i in range(0,len(world)):
        for j in range(0,len(world[0])):
            if(world[i][j]=='g'):
                goal=[i,j]
                break
goal1=goal[0]
goal2=goal[1]    
n=where_is_robot(world)
robot1=n[0]
robot2=n[1]    
current_path=stack(5000)

def find_path(world,path,robot1,robot2,goal1,goal2):
    n=where_is_robot(world)
    if(goal_reached(world)):
        print("You have reached, the shortest path is :")
        print(current_path)
        return(current_path)
    else:
        print("Not reached!! ")
        print(current_path)
    
    if(is_feasible(n[0]+1,n[1],world) or is_feasible(n[0]-1,n[1],world) or is_feasible(n[0],n[1]+1,world) or is_feasible(n[0],n[1]-1,world)):
        if(is_feasible(n[0]+1,n[1],world)):
            move_robot(n[0]+1,n[1],world)
            pprint(world)
            return find_path(world,current_path.pushing(Node("South")),n[0]+1,n[1],goal1,goal2)
        if(is_feasible(n[0]-1,n[1],world)):
            move_robot(n[0]-1,n[1],world)
            pprint(world)
            return find_path(world,current_path.pushing(Node("North")),n[0]-1,n[1],goal1,goal2)
        if(is_feasible(n[0],n[1]+1,world)):
            move_robot(n[0],n[1]+1,world)
            pprint(world)
            return find_path(world,current_path.pushing(Node("East")),n[0],n[1]+1,goal1,goal2)
        if(is_feasible(n[0],n[1]-1,world)):
            move_robot(n[0],n[1]-1,world)
            pprint(world)
            return find_path(world,current_path.pushing(Node("West")),n[0],n[1]-1,goal1,goal2)
    else:
        print(current_path.get_top())
        if(str(current_path.get_top())=="node: South" and is_feasible2(n[0]-1,n[1],world)):
            move_robot(n[0]-1,n[1],world)
            pprint(world)
            return find_path(world,current_path.popping(),n[0]-1,n[1],goal1,goal2)
        if(str(current_path.get_top())=="node: North" and is_feasible2(n[0]+1,n[1],world)):
            move_robot(n[0]+1,n[1],world)
            pprint(world)
            return find_path(world,current_path.popping(),n[0]+1,n[1],goal1,goal2)
        if(str(current_path.get_top())=="node: East" and is_feasible2(n[0],n[1]-1,world)):
            move_robot(n[0],n[1]-1,world)
            pprint(world)
            return find_path(world,current_path.popping(),n[0],n[1]-1,goal1,goal2)
        if(str(current_path.get_top())=="node: West" and is_feasible2(n[0],n[1]+1,world)):
            move_robot(n[0],n[1]+1,world)
            pprint(world)
            return find_path(world,current_path.popping(),n[0],n[1]+1,goal1,goal2)
    
if(is_feasible(n[0]+1,n[1],world) or is_feasible(n[0]-1,n[1],world) or is_feasible(n[0],n[1]+1,world) or is_feasible(n[0],n[1]-1,world)):
        if(is_feasible(n[0]+1,n[1],world)):
            world=move_robot(n[0]+1,n[1],world)
            pprint(world)
            find_path(world,current_path.pushing(Node("South")),n[0]+1,n[1],goal1,goal2)
        if(is_feasible(n[0]-1,n[1],world)):
            move_robot(n[0]-1,n[1],world)
            pprint(world)
            find_path(world,current_path.pushing(Node("North")),n[0]-1,n[1],goal1,goal2)
        if(is_feasible(n[0],n[1]+1,world)):
            move_robot(n[0],n[1]+1,world)
            pprint(world)
            find_path(world,current_path.pushing(Node("East")),n[0],n[1]+1,goal1,goal2)
        if(is_feasible(n[0],n[1]-1,world)):
            move_robot(n[0],n[1]-1,world)
            pprint(world)
            find_path(world,current_path.pushing(Node("West")),n[0],n[1]-1,goal1,goal2)