class Day2:
    def __init__(self,test,inp,run_test=False) -> None:
        self.test = open(test).read().split('\n')
        self.input = open(inp).read().split('\n')
        self.run_test = run_test
    
    def part1(self,inp=None):
        if not inp:inp=self.input
        p = 0
        for j in inp:
            o = j.split(':')
            gid = o[0].split(' ')[-1]
            possible = True
            vals = o[1].strip().split(';')
            #r,g,b
            r = 0
            g = 0
            b = 0
            for v in vals:
                args = v.split(',')
                for a in args:
                    vv = a.strip().split(' ')
                    if vv[1] == 'green':
                        g = int(vv[0])
                    if vv[1] == 'blue':
                        b = int(vv[0])
                    if vv[1] == 'red':
                        r = int(vv[0])
                    
                    if (r>12) or (g>13) or (b>14):
                        possible = False
                r,b,g = [0]*3

            if possible:
                p+=int(gid)

        print('Part1: '+ str(p))

    def part2(self,inp=None):
        if not inp:inp=self.input
        cleaned = {}
        p = 0
        for j in inp:
            o = j.split(':')
            gid = o[0].split(' ')[-1]
            vals = o[1].strip().split(';')
            #r,g,b
            r = 0
            g = 0
            b = 0
            tmp = []
            for v in vals:
                args = v.split(',')
                for a in args:
                    vv = a.strip().split(' ')
                    if vv[1] == 'green':
                        g = int(vv[0])
                    if vv[1] == 'blue':
                        b = int(vv[0])
                    if vv[1] == 'red':
                        r = int(vv[0])
                
                tmp.append([r,g,b])
                r,b,g = [0]*3

            mr,mb,mg = [0]*3
            # print(tmp)
            for i in tmp:
                r,g,b = i
                # print(r,g,b)
                mr = max(mr,r)
                mg = max(mg,g)
                mb = max(mb,b)
                # print(mr,mg,mb)

            p+= mr*mg*mb
            
            cleaned|={int(gid):tmp}

        print('Part2: '+ str(p))

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


    


solver = Day2('test.txt','input.txt',False)
solver.solve()