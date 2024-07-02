
def count_steps(n):
    if n<=0:
        return 0
    steps =[1,2,3]
    if n<4:
        return steps[n-1]
    
    for _ in range(n-3):
        steps[0],steps[1], steps[2]=steps[1],steps[2],steps[0]+steps[1]+steps[2]
    
    return steps[2]



if __name__=="__main__":
    for i in [1,5,9,23]:
        print(count_steps(i))

      # 1 2 3 6 11   