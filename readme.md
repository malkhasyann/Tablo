# <b>Tablo</b>
<b>Picsart Academy Homework</b>: Simulate Excel Spreadsheet in terminal.<br><br><br>

## Installation
1. <b>Create a virtual environment: </b> `python3 -m venv venv`
2. <b>Activate the virtual environment: </b> `source venv/bin/activate`
3. <b>Install requirements: </b> `pip3 install -r requirements.txt`
<br><br><br>

## Usage

```python
from models.cell import Cell
from models.spreadsheet import SpreadSheet


c1 = Cell('1', 'yellow')
c2 = Cell('2')
c2.color = 'green'
c3 = Cell()
c3.value = 3
c3.color = 'red'
c4 = Cell('4', 'blue')

print(c4.to_int()) # returns integer 4

sheet = SpreadSheet(2, 2)
sheet.set_cell_at(0, 0, c1)
sheet.set_cell_at(1, 1, c4)

sheet.swap_rows(0, 1)
sheet.swap_columns(0, 1)

sheet.remove_row(0)
```
<br><br><br>
### Main
<b>World Chess Champions</b><br>

![Screenshot from 2023-02-10 01-38-03](https://user-images.githubusercontent.com/99897064/217945554-0d8feae6-75e5-40ce-a785-74cc2fbfb8ac.png)
