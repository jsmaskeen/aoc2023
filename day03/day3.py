class Day3:
    def __init__(self,test,inp,run_test=False) -> None:
        self.test = open(test).read().split('\n')
        self.input = open(inp).read().split('\n')
        self.run_test = run_test

    def get_num(self,strn,pos):
        rside = ''
        for j in range(pos+1,len(strn)):
            if strn[j].isdigit():
                rside +=strn[j]
            else:
                break
        sr = strn[::-1]
        lside = ''
        for j in range(len(strn)-pos,len(strn)):
            if sr[j].isdigit():
                lside +=sr[j]
            else:
                break
        return int(lside[::-1] + strn[pos] + rside)

    
    def part1(self,inp=None):
        if not inp:inp=self.input
        y = len(inp)
        x = len(inp[0])
        a = 0
        p = 0
        for j in range(y):
            for i in range(x):
                c = inp[j][i]
                if not (c.isdigit() or c == '.'):
                    gear = True
                    vds = []
                    # lft,rght,only_bottom,only_top,tr,tl,br,bl = [False]*8
                    if inp[j][i-1].isdigit():
                        # lft = True
                        a+= self.get_num(inp[j],i-1)
                        if gear:
                            vds.append(self.get_num(inp[j],i-1))
                    if inp[j][i+1].isdigit():
                        # rght = True
                        a+= self.get_num(inp[j],i+1)
                        if gear:
                            vds.append(self.get_num(inp[j],i+1))

                    if not inp[j-1][i].isdigit():
                        if inp[j-1][i-1].isdigit():
                            a+= self.get_num(inp[j-1],i-1)
                            if gear:
                                vds.append(self.get_num(inp[j-1],i-1))
                            # tl = True
                        if inp[j-1][i+1].isdigit():
                            # tr = True
                            a+= self.get_num(inp[j-1],i+1)
                            if gear:
                                vds.append(self.get_num(inp[j-1],i+1))
                    else:
                        # only_top = True
                        a+= self.get_num(inp[j-1],i)
                        if gear:
                            vds.append(self.get_num(inp[j-1],i))
                    
                    if not inp[j+1][i].isdigit():
                        if inp[j+1][i-1].isdigit():
                            # bl = True
                            a+= self.get_num(inp[j+1],i-1)
                            if gear:
                                vds.append(self.get_num(inp[j+1],i-1))
                        if inp[j+1][i+1].isdigit():
                            # br = True
                            a+= self.get_num(inp[j+1],i+1)
                            if gear:
                                vds.append(self.get_num(inp[j+1],i+1))
                    else:
                        # only_bottom = True
                        a+= self.get_num(inp[j+1],i)
                        if gear:
                            vds.append(self.get_num(inp[j+1],i))

                    p+= sum(vds)
                    
        print('Part1: ' + str(p))

    def part2(self,inp=None):
        if not inp:inp=self.input  
        y = len(inp)
        x = len(inp[0])
        a = 0
        p = 0
        for j in range(y):
            for i in range(x):
                c = inp[j][i]
                if not (c.isdigit() or c == '.'):
                    gear = c == '*'
                    vds = []
                    # lft,rght,only_bottom,only_top,tr,tl,br,bl = [False]*8
                    if inp[j][i-1].isdigit():
                        # lft = True
                        a+= self.get_num(inp[j],i-1)
                        if gear:
                            vds.append(self.get_num(inp[j],i-1))
                    if inp[j][i+1].isdigit():
                        # rght = True
                        a+= self.get_num(inp[j],i+1)
                        if gear:
                            vds.append(self.get_num(inp[j],i+1))

                    if not inp[j-1][i].isdigit():
                        if inp[j-1][i-1].isdigit():
                            a+= self.get_num(inp[j-1],i-1)
                            if gear:
                                vds.append(self.get_num(inp[j-1],i-1))
                            # tl = True
                        if inp[j-1][i+1].isdigit():
                            # tr = True
                            a+= self.get_num(inp[j-1],i+1)
                            if gear:
                                vds.append(self.get_num(inp[j-1],i+1))
                    else:
                        # only_top = True
                        a+= self.get_num(inp[j-1],i)
                        if gear:
                            vds.append(self.get_num(inp[j-1],i))
                    
                    if not inp[j+1][i].isdigit():
                        if inp[j+1][i-1].isdigit():
                            # bl = True
                            a+= self.get_num(inp[j+1],i-1)
                            if gear:
                                vds.append(self.get_num(inp[j+1],i-1))
                        if inp[j+1][i+1].isdigit():
                            # br = True
                            a+= self.get_num(inp[j+1],i+1)
                            if gear:
                                vds.append(self.get_num(inp[j+1],i+1))
                    else:
                        # only_bottom = True
                        a+= self.get_num(inp[j+1],i)
                        if gear:
                            vds.append(self.get_num(inp[j+1],i))

                    if len(vds) == 2:
                        fm = 1
                        for fsd in vds:
                            fm*=fsd
                        p+= fm
                    
        print('Part2: ' + str(p))

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



solver = Day3('test.txt','input.txt')
solver.solve()