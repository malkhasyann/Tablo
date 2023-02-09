""" World Chess Champions List."""
from models.spreadsheet import SpreadSheet

sheet = SpreadSheet(16, 2)
sheet.set_cell_at(0,0, 'Wilhelm Steinitz')
sheet.set_cell_at(1,0, 'Emanuel Lasker')
sheet.set_cell_at(2,0, 'Jose Raul Capablanca')
sheet.set_cell_at(3,0, 'Alexander Alekhine')
sheet.set_cell_at(4,0, 'Max Euwe')
sheet.set_cell_at(5,0, 'Mikhail Botvinnik')
sheet.set_cell_at(6,0, 'Vasily Smyslov')
sheet.set_cell_at(7,0, 'Mikhail Tal')
sheet.set_cell_at(8,0, 'Tigran Petrosian')
sheet.set_cell_at(9,0, 'Boris Spassky')
sheet.set_cell_at(10,0, 'Bobby Fischer')
sheet.set_cell_at(11,0, 'Anatoly Karpov')
sheet.set_cell_at(12,0, 'Garry Kasparov')
sheet.set_cell_at(13,0, 'Vladimir Kramnik')
sheet.set_cell_at(14,0, 'Vishwanathan Anand')
sheet.set_cell_at(15,0, 'Magnus Carlsen')

sheet.get_cell_at(0,0).color = 'green'
sheet.get_cell_at(1,0).color = 'green'
sheet.get_cell_at(2,0).color = 'green'
sheet.get_cell_at(3,0).color = 'green'
sheet.get_cell_at(4,0).color = 'green'
sheet.get_cell_at(5,0).color = 'green'
sheet.get_cell_at(6,0).color = 'green'
sheet.get_cell_at(7,0).color = 'green'
sheet.get_cell_at(8,0).color = 'green'
sheet.get_cell_at(9,0).color = 'green'
sheet.get_cell_at(10,0).color = 'green'
sheet.get_cell_at(11,0).color = 'green'
sheet.get_cell_at(12,0).color = 'green'
sheet.get_cell_at(13,0).color = 'green'
sheet.get_cell_at(14,0).color = 'green'
sheet.get_cell_at(15,0).color = 'green'

sheet.set_cell_at(0,1, '1886')
sheet.set_cell_at(1,1, '1894')
sheet.set_cell_at(2,1, '1921')
sheet.set_cell_at(3,1, '1927')
sheet.set_cell_at(4,1, '1935')
sheet.set_cell_at(5,1, '1948')
sheet.set_cell_at(6,1, '1957')
sheet.set_cell_at(7,1, '1960')
sheet.set_cell_at(8,1, '1963')
sheet.set_cell_at(9,1, '1969')
sheet.set_cell_at(10,1, '1972')
sheet.set_cell_at(11,1, '1975')
sheet.set_cell_at(12,1, '1985')
sheet.set_cell_at(13,1, '2000')
sheet.set_cell_at(14,1, '2007')
sheet.set_cell_at(15,1, '2013')

sheet.get_cell_at(0,1).color = 'yellow'
sheet.get_cell_at(1,1).color = 'yellow'
sheet.get_cell_at(2,1).color = 'yellow'
sheet.get_cell_at(3,1).color = 'yellow'
sheet.get_cell_at(4,1).color = 'yellow'
sheet.get_cell_at(5,1).color = 'yellow'
sheet.get_cell_at(6,1).color = 'yellow'
sheet.get_cell_at(7,1).color = 'yellow'
sheet.get_cell_at(8,1).color = 'yellow'
sheet.get_cell_at(9,1).color = 'yellow'
sheet.get_cell_at(10,1).color = 'yellow'
sheet.get_cell_at(11,1).color = 'yellow'
sheet.get_cell_at(12,1).color = 'yellow'
sheet.get_cell_at(13,1).color = 'yellow'
sheet.get_cell_at(14,1).color = 'yellow'
sheet.get_cell_at(15,1).color = 'yellow'

sheet.add_column(2)

sheet.set_cell_at(0,2, 'Austria-Hungary')
sheet.set_cell_at(1,2, 'Germany')
sheet.set_cell_at(2,2, 'Cuba')
sheet.set_cell_at(3,2, 'Russia')
sheet.set_cell_at(4,2, 'Netherlands')
sheet.set_cell_at(5,2, 'USSR')
sheet.set_cell_at(6,2, 'USSR')
sheet.set_cell_at(7,2, 'USSR')
sheet.set_cell_at(8,2, 'USSR')
sheet.set_cell_at(9,2, 'USSR')
sheet.set_cell_at(10,2, 'USA')
sheet.set_cell_at(11,2, 'USSR')
sheet.set_cell_at(12,2, 'USSR')
sheet.set_cell_at(13,2, 'Russia')
sheet.set_cell_at(14,2, 'India')
sheet.set_cell_at(15,2, 'Norway')

sheet.get_cell_at(0,2).color = 'red'
sheet.get_cell_at(1,2).color = 'red'
sheet.get_cell_at(2,2).color = 'red'
sheet.get_cell_at(3,2).color = 'red'
sheet.get_cell_at(4,2).color = 'red'
sheet.get_cell_at(5,2).color = 'red'
sheet.get_cell_at(6,2).color = 'red'
sheet.get_cell_at(7,2).color = 'red'
sheet.get_cell_at(8,2).color = 'red'
sheet.get_cell_at(9,2).color = 'red'
sheet.get_cell_at(10,2).color = 'red'
sheet.get_cell_at(11,2).color = 'red'
sheet.get_cell_at(12,2).color = 'red'
sheet.get_cell_at(13,2).color = 'red'
sheet.get_cell_at(14,2).color = 'red'
sheet.get_cell_at(15,2).color = 'red'

sheet.print_sheet()
