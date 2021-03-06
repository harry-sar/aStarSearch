import cell

class aStarSearch:

    def __init__(self, grid_size):
        # f cost = g cost + h cost
        # g cost(the movement cost to move from the starting point to a given square on the grid)
        # h cost (the estimated movement cost to move from that given square on the grid to the final destination. )
        self.grid_size = grid_size
        self.graph_init = {}
        self.graph={}
        self.open_dict = {}  # cell: cost
        self.closed_dict = {}

        self.gen_grid() # graph init used only for finding neighbours
        self.gen_graph()
    def gen_graph(self):
        for x in range (self.grid_size**2):
            up, btwnUR, right, btwnRD, down, btwnLD, left, btwnLU = self.check_8_neighbours(x+1)
            self.graph[x+1]= cell.cell(up, btwnUR, right, btwnRD, down, btwnLD, left, btwnLU,"cell")

    def gen_grid(self):
        count_gen = 1
        for x in range(self.grid_size ** 2):
            if count_gen == 1:
                self.graph_init[x + 1] = "START"
            if x + 1 <= self.grid_size:
                self.graph_init[x + 1] = "TOP"
            if count_gen == self.grid_size:
                self.graph_init[x + 1] = "END"
                count_gen = 0
            elif count_gen != 1 and count_gen != self.grid_size and not x + 1 <= self.grid_size:
                self.graph_init[x + 1] = "[-]"
            count_gen += 1

    def print_grid_debug(self):
        self.printme = ""
        for k, v in self.graph_init.items():
            if k % self.grid_size == 0:
                self.printme += str(v) + "\n"
            else:
                self.printme += str(v)
        print(self.printme)

    def check_8_neighbours(self, cell):
        hasUp, hasBtwnUR, hasRight, hasBtwnRD, hasDown, hasBtwnLD, hasLeft, hasBtwnLU = None,None,None,None,None,None,None,None
        # Checking if Up cell
        try:
            if self.graph_init[cell - self.grid_size]:
                hasUp = cell - self.grid_size
        except:
            hasUp = None
        # Checking if UR cell
        try:
            if self.graph_init[cell - self.grid_size + 1] and self.graph_init[cell] not in ["TOP","END"]:
                hasBtwnUR = cell - self.grid_size + 1
        except:
            hasBtwnUR = None
        # Checking if Right cell
        try:
            if self.graph_init[cell + 1] and self.graph_init[cell] not in ["END"]:
                hasRight = cell + 1
        except:
            hasRight = None
        # Checking if RD cell
        try:
            if self.graph_init[cell + self.grid_size + 1] and self.graph_init[cell] not in ["END"]:
                hasBtwnRD = cell + self.grid_size + 1
        except:
            hasBtwnRD = None
        # Checking if Down cell
        try:
            if self.graph_init[cell + self.grid_size]:
                hasDown = cell + self.grid_size
        except:
            hasDown = None
        # Checking if LD cell
        try:
            if self.graph_init[cell + self.grid_size - 1] and self.graph_init[cell] not in ["START"] and cell!=1:
                hasBtwnLD = cell + self.grid_size - 1
        except:
            hasBtwnLD = None
        # Checking if Left cell
        try:
            if self.graph_init[cell - 1] and self.graph_init[cell] not in ["START"] and cell!=1:
                hasLeft = cell - 1
        except:
            hasLeft = None
        # Checking if LU cell
        try:
            if self.graph_init[cell - self.grid_size - 1] and self.graph_init[cell] not in ["START","TOP"]:
                hasBtwnLU = cell - self.grid_size - 1
        except:
            hasBtwnLU = None

        return hasUp,hasBtwnUR,hasRight,hasBtwnRD,hasDown,hasBtwnLD,hasLeft,hasBtwnLU

    def search(self):
        q = None
        self.open_dict[1]=self.graph[1].fcost

        while len(self.open_dict)!=0:
            q=min(self.open_dict, key=self.open_dict.get)
            self.open_dict.pop(q)



test = aStarSearch(5)
# test.print_grid_debug()
test.search()
# lol=[test.check_8_neighbours(5)]
# print(lol)