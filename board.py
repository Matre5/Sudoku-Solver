class Board:
    
    def __init__(self, grid) -> None:
        self.grid = grid
        self.size = 9
        
    def valid_move(self, row, column, num):
        return (
            self.valid_row(row, num)
            and 
        )