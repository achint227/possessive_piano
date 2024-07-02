class UnionFind:
    def __init__(self,n) -> None:
        self.members=[-1]*n
    def find(self,m):
        parent=m
        while self.members[parent]>=0:
            self.members[parent] = self.find(self.members[parent])
            parent = self.members[parent]
        return parent
    def union(self,a,b):
        pa,pb = self.find(a),self.find(b)
        if pa==pb:
            return
        if self.members[pa]<self.members[pb] or (self.members[pa]==self.members[pb] and pa<pb):
            self.members[pa]+=self.members[pb]
            self.members[pb]=pa
        else:
            self.members[pb]+=self.members[pa]
            self.members[pa]=pb
    def get_other_group_members(self,m):
        res=[]
        p=self.find(m)
        for i in range(len(self.members)):
            if self.find(i)==p:
                res.append(i)
        return res

def findAllPeople(n: int, meetings, firstPerson: int):
    uf=UnionFind(n)
    uf.union(0,firstPerson)
    meetings.sort(key=lambda x: x[2])

    for p1, p2, _ in meetings:
        uf.union(p1, p2)

    
    return uf.get_other_group_members(0)


def main():
    n = 4
    meetings = [[3, 1, 3], [1, 2, 2], [0, 3, 3]]
    firstPerson = 3

    result = findAllPeople(n, meetings, firstPerson)
    print(result)


if __name__ == "__main__":
    # main()
    uf = UnionFind(5)
    uf.union(4,3)
    uf.union(3,2)
    uf.union(1,0)
    print(uf.get_other_group_members(0))
