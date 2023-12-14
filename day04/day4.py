inp = open('test.txt').read()

class Day4:
    def __init__(self,test,inp,run_test=False) -> None:
        self.test = open(test).read().strip().split('\n')
        self.input = open(inp).read().strip().split('\n')
        self.run_test = run_test
    
    def part1(self,inp=None):
        if not inp:inp=self.input
        v = 0
        for j in inp:
            winners,mine = [list(map(int,i.split())) for i in j.split(':')[1].strip().split(' | ')]
            c = 0
            for i in mine:
                if i in winners:
                    c+=1
            if c!=0:
                v+=2**(c-1)

        print(f'Part1: {v}')


    def unpacl(self,inp,tt,cnum):
        j = inp[cnum-1]
        winners,mine = [list(map(int,i.split())) for i in j.split(':')[1].strip().split(' | ')]
        cnt = 0
        for i in mine:
            if i in winners:
                cnt+=1
        for k in range(cnum+1,cnum+1+cnt):
            try:
                tt[k]+=1
                self.unpacl(inp,tt,k)
            except:
                pass

    def part2(self,inp=None):
        if not inp:inp=self.input
        tt = dict.fromkeys(range(1,len(inp)+1),1)

        for j in range(1,len(inp)+1):
            self.unpacl(inp,tt,j)
            
        print(f'Part2: {sum(tt.values())}')

    def tester(self):
        print('TEST'.center(16,'#'))
        self.part1(self.test)
        print()
        self.part2(self.test)
        print('#'*16)
        print()

    def solve(self):
        if self.run_test:
            self.tester()
        else:
            self.part1()
            print()
            self.part2()


    


solver = Day4('test.txt','input.txt',False)
solver.solve()