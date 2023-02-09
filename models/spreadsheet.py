from models.cell import Cell
from typing import Union
from rich.console import Console
from rich.table import Table
from rich.text import Text

class SpreadSheet:
    
    __console = Console(highlight=False)
    
    def __init__(self, rows:int, columns:int) -> None:
        self.rows = rows
        self.columns = columns
        self._table = [[Cell() for _ in range(columns)] for _ in range(rows)]
                
    @property
    def rows(self) -> int:
        return self._rows
    @rows.setter
    def rows(self, value:int) ->None:
        if not isinstance(value, int):
            raise ValueError("Spreadsheet row number must have type: int.")
        if value <= 0:
            raise ValueError("Spreadsheet row number must be greater than 0.")
        self._rows = value
        
    @property
    def columns(self) -> int:
        return self._columns
    @columns.setter
    def columns(self, value:int) -> None:
        if not isinstance(value, int):
            raise ValueError("Spreadsheet column number must have type: int.")
        if value <= 0:
            raise ValueError("Spreadsheet column number must be greater than 0.")
        self._columns = value
        
    def set_cell_at(self, i:int, j:int, cell:Union[Cell, str]) -> None:
        if not ((0 <= i < self.rows) and (0 <= j < self.columns)):
            raise ValueError(f"Index out of range 'set_cell_at({i}, {j})'.")
        if isinstance(cell, str):
            new_cell = Cell(value=cell)
            self._table[i][j] = new_cell
        if isinstance(cell, Cell):
            new_cell = Cell(cell.value, cell.color)
            self._table[i][j] = new_cell

    def get_cell_at(self, i:int, j:int) -> Cell:
        if not ((0 <= i < self.rows) and (0 <= j < self.columns)):
            raise ValueError(f"Index out of range 'get_cell_at({i}, {j})'.")
        return self._table[i][j]
    
    def add_row(self, i:int) -> None:
        if not (0 <= i <= self.rows):
            raise ValueError(f"Index out of range 'add_row({i})'.")
        self._table.insert(i, [Cell() for _ in range(self.columns)])
        self.rows += 1
        
    def add_column(self, i:int) -> None:
        if not (0 <= i <= self.columns):
            raise ValueError(f"Index out of range 'add_column({i})'.")
        for j in range(self.rows):
            self._table[j].insert(i, Cell())
        self.columns += 1
        
    def remove_row(self, i:int) -> None:
        if not (0 <= i < self.rows):
            raise ValueError(f"Index out of range 'remove_row({i})'.")
        del self._table[i]
        self.rows -= 1
        
    def remove_column(self, i:int) -> None:
        if not (0 <= i <= self.columns):
            raise ValueError(f"Index out of range 'remove_columns({i})'.")
        for j in range(self.rows):
            del self._table[j][i]
        self.columns -= 1
        
    def swap_rows(self, i:int, j:int) -> None:
        if not ((0 <= i < self.rows) and (0 <= j < self.rows)):
            raise ValueError(f"Index out of range 'swap_rows({i}, {j})'.")
        self._table[i], self._table[j] = self._table[j], self._table[i]
        
    def swap_columns(self, i:int, j:int) -> None:
        if not ((0 <= i < self.columns) and (0 <= j < self.columns)):
            raise ValueError(f"Index out of range 'swap_columns({i}, {j})'.")
        for k in range(self.rows):
            self._table[k][i], self._table[k][j] = self._table[k][j], self._table[k][i]
        
    def print_sheet(self):
        print()
        header = Text('Tablo', style='bold bright_white')
        table = Table(title=header, expand=True, show_lines=True)
        table.add_column(justify='left')
        for j in range(self.columns):
            table.add_column(f'{j}', justify='center')
            
        for i in range(self.rows):
            row = [f'{i}']
            for j in range(self.columns):
                row.append(Text(self._table[i][j].value, style=self._table[i][j].color))
            table.add_row(*row)
            
        SpreadSheet.__console.print(table)
    