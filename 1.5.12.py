class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False
class Gamepole:
    def __init__(self,N,M):
        cl = 0
        self.pole =[cl for i in range(N) for j in range(N) ]
    def show(self) :
        pole_output=self.pole[:]
        for x in pole_output :
            for y in x:
                if y.fl_open == False:
                    y.fl_open = '#'
                elif y.fl_open == True and y.mine = = True:
                    y.fl_open = '*'
        for x in pole_output:
            print(*x)




d = [[1,0,0],[0,1,0],[0,0,1]]
for x in d:
    print(*x)
