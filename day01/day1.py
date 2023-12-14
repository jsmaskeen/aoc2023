class Day1:
    def __init__(self,test,inp,run_test=True) -> None:
        self.test1,self.test2 = open(test).read().split('\n\n')
        self.input = open(inp).read()
        self.run_test = run_test
    
    def part1(self,inp=None):
        if not inp:inp=self.input

        v = 0

        for i in inp.split('\n'):
            d = None
            f = ''
            for j in i:
                if j.isdigit():
                    d = j
                    if not f:
                        f+=j
            f+=d
            v+= int(f)

        print(f'Part1: {v}')

        

    def part2(self,inp=None):
        if not inp:inp=self.input
        v = inp.split('\n')
        u = 0
        s = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']
        for i in v:
            tmp = []
            for j in range(len(i)):
                for k in range(j+1,len(i)+1):
                    v2 = i[j:k]
                    # print(v2)
                    if k-j == 1 and v2.isdigit():
                        tmp.append(v2)
                    if v2 in s:
                        tmp.append(v2)

            tt = ''
            if tmp[0].isdigit():
                tt+= tmp[0]
            else:
                tt+= str(s.index(tmp[0])+1)
            
            if tmp[-1].isdigit():
                tt+= tmp[-1]
            else:
                tt+= str(s.index(tmp[-1])+1)
            u+= int(tt)


        print(f'Part2: {u}')



    def tester(self):
        print('TEST'.center(16,'#'))
        self.part1(self.test1)
        print()
        self.part2(self.test2)
        print('#'*16)
        print()

    def solve(self):
        if self.run_test:
            self.tester()

        self.part1()
        print()
        self.part2()


    


solver = Day1('test.txt','input.txt')
solver.solve()
