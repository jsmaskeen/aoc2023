from copy import deepcopy
class Day15:
    def __init__(self,test,inp,run_test=True) -> None:
        self.test = open(test).read()
        self.input = open(inp).read()
        self.run_test = run_test

    def hsh(self,inp):
        v = 0
        for i in inp:
            v+= ord(i)
            v*=17
            v%=256
        return v
    
    def part1(self,inp=None):
        if not inp:inp=self.input
        xx = inp.split(',')
        u = 0
        for inp in xx:
            v = 0
            for i in inp:
                v+= ord(i)
                v*=17
                v%=256
            u+=v
        print(f'Part1: {u}')

    def part2(self,inp=None):
        if not inp:inp=self.input
        inp = inp.split(',')
        mp = dict.fromkeys(range(0,256),[])
        for i in inp:
            if '-' in i:
                box = self.hsh(i[:-1])
                rm = False
                ls = deepcopy(mp[box])
                for j in ls:
                    if i[:-1] in j:
                        rm = j
                        break
                if rm:
                    ls.remove(rm)
                mp[box] = ls
                
            elif '=' in i:
                box = self.hsh(i[:-2])
                fc = i[-1]
                rm = False
                ls = deepcopy(mp[box])
                for j in ls:
                    if i[:-2] in j:
                        rm = j
                        break
                
                if rm:
                    ls.insert(ls.index(rm),f'[{i[:-2]} {fc}]')
                    ls.pop(ls.index(rm))
                else:
                    ls.append(f'[{i[:-2]} {fc}]')
                mp[box] = ls


            # print(i,mp)
        u = 0
        for k,v in mp.items():
            for j,c in enumerate(v,1):
                u+=(k+1)*j*int(c[-2])
                

        print(f'Part2: {u}')


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

solver = Day15('test.txt','input.txt',0)
solver.solve()