import cell


class aStarSearch:

    def __init__(self, grid_size):
        # f cost = g cost + h cost
        # g cost(the movement cost to move from the starting point to a given square on the grid)
        # h cost (the estimated movement cost to move from that given square on the grid to the final destination. )
        self.grid_size = grid_size
        self.graph_init = {}
        self.graph = {}

        for x in range(self.grid_size ** 2):
            self.graph_init[x + 1] = "[-]"

        self.open_dict = {}  # cell: cost
        self.closed_dict = {}

    def print_grid(self):
        self.printme = ""
        for k, v in self.graph_init.items():
            if k % self.grid_size == 0:
                self.printme += str(v) + "\n"
                print(self.printme)
            else:
                self.printme += str(v)

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
            if self.graph_init[cell - self.grid_size + 1]:
                hasBtwnUR = cell - self.grid_size + 1
        except:
            hasBtwnUR = None
        # Checking if Right cell
        try:
            if self.graph_init[cell + 1]:
                hasRight = cell + 1
        except:
            hasRight = None
        # Checking if RD cell
        try:
            if self.graph_init[cell + self.grid_size + 1]:
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
            if self.graph_init[cell + self.grid_size - 1] and ((cell+self.grid_size-1)%self.grid_size!=0):
                hasBtwnLD = cell + self.grid_size - 1
        except:
            hasBtwnLD = None
        # Checking if Left cell
        try:
            if self.graph_init[cell - 1]:
                hasLeft = cell - 1
        except:
            hasLeft = None
        # Checking if LU cell
        try:
            if self.graph_init[cell - self.grid_size - 1]:
                hasBtwnLU = cell - self.grid_size - 1
        except:
            hasBtwnLU = None

        return hasUp,hasBtwnUR,hasRight,hasBtwnRD,hasDown,hasBtwnLD,hasLeft,hasBtwnLU

    def search(self):
        q = None


test = aStarSearch(5)
# test.print_grid()

lol=[test.check_8_neighbours(5)]

print(lol)
