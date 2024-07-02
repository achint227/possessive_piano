

def solve_towers(numDisks):
    t1=list(range(numDisks,0,-1))
    t2=[]
    t3=[]


    def moveTop(source,destination):
        destination.append(source.pop())
    def move(num,source,destination,buffer):
        if num==0:
            return
        move(num-1,source,buffer,destination)
        moveTop(source,destination)
        move(num-1,buffer,destination,source)

            
    move(numDisks,t1,t3,t2)
solve_towers(7)

