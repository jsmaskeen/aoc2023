inp = open('test.txt').read()

class Day4:
    def __init__(self,test,inp,run_test=True) -> None:
        self.test = open(test).read()
        self.input = open(inp).read()
        self.run_test = run_test
    
    def part1(self,inp=None):
        if not inp:inp=self.input

    def part2(self,inp=None):
        if not inp:inp=self.input

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
        self.part1()
        print()
        self.part2()


    


solver = Day4('test.txt','input.txt')
solver.solve()