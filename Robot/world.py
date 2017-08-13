from pprint import pprint

def create_world(filename):
    import re
    buffer=open(filename).read()
    lines=buffer.splitlines()
    numbers=[]
    numbers+=re.findall("[-\d]+",lines[0])
    x=int(numbers[0])
    y=int(numbers[1])
    
    a2d = [ [0]*x for _ in range(y)]
    for i in range(1,len(lines)):
        wallnumbers=[]
        robotnumbers=[]
        goalnumbers=[]
        value=lines[i].strip().split()
        if value[0]=='w':
            for j in range(0,len(value)):
                wallnumbers+=re.findall("[-\d]+",value[j])
            wx=int(wallnumbers[0])
            wy=int(wallnumbers[1])
            a2d[wx][wy]=1
        if value[0]=="r2d2":
            for j in range(0,len(value)):
                robotnumbers+=re.findall("[-\d]+",value[j])
            rx=int(robotnumbers[2])
            ry=int(robotnumbers[3])
        if value[0]=="goal":
            for j in range(0,len(value)):
                goalnumbers+=re.findall("[-\d]+",value[j])
            gx=int(goalnumbers[0])
            gy=int(goalnumbers[1])
    
    e=rx #robotnumbers in x axis
    f=ry ##robotnumbers in y axis
    r2d2=a2d[e][f] #position in the axis.
    a2d[e][f]='r'
    goal=a2d[gx][gy]
    a2d[gx][gy]='g'
    return a2d  #robot position

def where_is_robot(a2d):
    l=len(a2d)
    for i in range(l):
        for j in range(l):
            if(a2d[i][j]=='r'):
                n=[i,j]
                break;
    return n
    
                            
def move_robot(x,y,a2d):
    r=where_is_robot(a2d)
    a2d[r[0]][r[1]]='p'
    a2d[x][y]='r'
    return a2d 

    
def goal_reached(a2d):

    for i in range(0,len(a2d)):
        for j in range(0,len(a2d[0])):
            if(a2d[i][j]=='g'):
                goal=[i,j]
                return False
                break
    return True        
                

     

def is_feasible(new_x,new_y,a2d):
    n = where_is_robot(a2d)
    p=len(a2d)
    q=len(a2d[0])
    
    
    if(0<=new_x<p and 0<=new_y<q):
        if((new_x==n[0] and new_y!=n[1])or(new_x!=n[0] and new_y==n[1])):
            if(a2d[new_x][new_y]==1 or a2d[new_x][new_y]=='p'):
                return False
            else:
                return True
        else:
            return False
    else:
        return False
    
def is_feasible2(new_x,new_y,a2d):
    n = where_is_robot(a2d)
    p=len(a2d)
    q=len(a2d[0])
    
    
    if(0<=new_x<p and 0<=new_y<q):
        if((new_x==n[0] and new_y!=n[1])or(new_x!=n[0] and new_y==n[1])):
            if(a2d[new_x][new_y]==1):
                return False
            else:
                return True
        else:
            return False
    else:
        return False
