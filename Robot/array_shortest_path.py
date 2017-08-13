
from world import *
from array_stack import *
from world import *
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
        print("You have reached!!")
        print(current_path.get_stack())
        print(current_path.get_length())
        return(current_path.get_length())
    else:
        print("Not reached!! Try again")
        print(current_path.get_stack())
    
    if(is_feasible(n[0]+1,n[1],world) or is_feasible(n[0]-1,n[1],world) or is_feasible(n[0],n[1]+1,world) or is_feasible(n[0],n[1]-1,world)):
        if(is_feasible(n[0]+1,n[1],world)):
            move_robot(n[0]+1,n[1],world)
            pprint(world)
            return find_path(world,current_path.pushing("South"),n[0]+1,n[1],goal1,goal2)
        if(is_feasible(n[0]-1,n[1],world)):
            move_robot(n[0]-1,n[1],world)
            pprint(world)
            return find_path(world,current_path.pushing("North"),n[0]-1,n[1],goal1,goal2)
        if(is_feasible(n[0],n[1]+1,world)):
            move_robot(n[0],n[1]+1,world)
            pprint(world)
            return find_path(world,current_path.pushing("East"),n[0],n[1]+1,goal1,goal2)
        if(is_feasible(n[0],n[1]-1,world)):
            move_robot(n[0],n[1]-1,world)
            pprint(world)
            return find_path(world,current_path.pushing("West"),n[0],n[1]-1,goal1,goal2)
    else:
        if(current_path.get_top()=="South" and is_feasible2(n[0]-1,n[1],world)):
            move_robot(n[0]-1,n[1],world)
            pprint(world)
            return find_path(world,current_path.poping(),n[0]-1,n[1],goal1,goal2)
        if(current_path.get_top()=="North" and is_feasible2(n[0]+1,n[1],world)):
            move_robot(n[0]+1,n[1],world)
            pprint(world)
            return find_path(world,current_path.poping(),n[0]+1,n[1],goal1,goal2)
        if(current_path.get_top()=="East" and is_feasible2(n[0],n[1]-1,world)):
            move_robot(n[0],n[1]-1,world)
            pprint(world)
            return find_path(world,current_path.poping(),n[0],n[1]-1,goal1,goal2)
        if(current_path.get_top()=="West" and is_feasible2(n[0],n[1]+1,world)):
            move_robot(n[0],n[1]+1,world)
            pprint(world)
            return find_path(world,current_path.poping(),n[0],n[1]+1,goal1,goal2)
    
if(is_feasible(n[0]+1,n[1],world) or is_feasible(n[0]-1,n[1],world) or is_feasible(n[0],n[1]+1,world) or is_feasible(n[0],n[1]-1,world)):
        if(is_feasible(n[0]+1,n[1],world)):
            world=move_robot(n[0]+1,n[1],world)
            pprint(world)
            find_path(world,current_path.pushing("South"),n[0]+1,n[1],goal1,goal2)
        if(is_feasible(n[0]-1,n[1],world)):
            move_robot(n[0]-1,n[1],world)
            pprint(world)
            find_path(world,current_path.pushing("North"),n[0]-1,n[1],goal1,goal2)
        if(is_feasible(n[0],n[1]+1,world)):
            move_robot(n[0],n[1]+1,world)
            pprint(world)
            find_path(world,current_path.pushing("East"),n[0],n[1]+1,goal1,goal2)
        if(is_feasible(n[0],n[1]-1,world)):
            move_robot(n[0],n[1]-1,world)
            pprint(world)
            find_path(world,current_path.pushing("West"),n[0],n[1]-1,goal1,goal2)