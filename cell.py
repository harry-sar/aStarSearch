class cell:

    def __init__(self,up,btwnUR,right,btwnRD,down,btwnLD,left,btwnLU,cell_type):
        self.left=left
        self.right=right
        self.up=up
        self.down=down
        self.btwnUR = btwnUR
        self.btwnRD=btwnRD
        self.btwnLD=btwnLD
        self.btwnLU=btwnLU

        self.cell_type=cell_type
        self.hcost=0
        self.gcost=0
        self.fcost=self.hcost+self.gcost