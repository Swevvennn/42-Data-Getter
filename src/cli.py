from .getter import get_ratio, get_data, get_intras, get_logtime
from .helper import writer
from .printer import print_board, print_table

class CLI:
    def level(self):
        students = get_data(get_intras())
        print_board(students, 'level')
        writer(students)

    def logtime(self):
        students = get_logtime(get_intras())
        print_board(students, 'logtime')
        writer(students)
    
    def ratio(self):
        print_board(get_ratio(get_intras()), 'ratio')
    
    def table(self):
        students = get_data(get_intras())
        print_table(students)
        writer(students)
