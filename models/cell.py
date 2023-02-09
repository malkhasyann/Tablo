from datetime import datetime
from rich.console import Console

class Cell:
    COLOR = {
        'white':'bright_white',
        'black':'black',
        'red': 'bright_red',
        'blue': 'dark_blue',
        'green': 'green3',
        'purple': 'purple3',
        'yellow':'bright_yellow'
    }
    
    __console = Console(highlight=False)
    
    def __init__(self, value:str="", color:str="") -> None:
        self.value = value
        if color == "":
            self.color = 'white'
        else:
            self.color = color
        
    @property
    def value(self) -> str:
        return self._value
    @value.setter
    def value(self, val:str) -> None:
        if not isinstance(val, str):
            raise ValueError("Cell's value must have type: str.")
        self._value = val
        
    @property
    def color(self) -> str:
        return self._color
    @color.setter
    def color(self, color:str) -> None:
        if color not in Cell.COLOR:
            raise ValueError("Cell's color must be initialized via COLOR class attribute.")
        self._color = color
        
    def to_int(self) -> int:
        try:
            return int(self.value)
        except Exception as e:
            raise ValueError("Couldn't convert the value to the type: int.") from e
        
    def to_float(self) -> float:
        try:
            return float(self.value)
        except Exception as e:
            raise ValueError("Couldn't convert the value to the type: float.") from e
    
    def to_date(self) -> datetime:
        try:
            return datetime.strptime(self.value, '%m/%d/%Y')
        except Exception as e:
            raise ValueError("Couldn't convert the value to the type: datetime.") from e  
    
    def reset(self) -> None:
        self.value = ""
        self.color = Cell.COLOR['white']
        
    def __str__(self):
        return f'{self.value}'
    
    def print_cell(self) -> None:
        Cell.__console.print(self.value, style=Cell.COLOR[self.color])
