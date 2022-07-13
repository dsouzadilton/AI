from tabulate import tabulate
j1 = []
j2 = []
def pour(jug1, jug2):
    j1.append(jug1)
    j2.append(jug2)
    if jug2 == fill:
        return
    elif jug2 == max2:
        pour(0, jug1)
    elif jug1 != 0 and jug2 == 0:
        pour(0, jug1)
    elif jug1 == fill:
        pour(jug1, 0)
    elif jug1 < max1:
        pour(max1, jug2)
    elif jug1 < (max2-jug2):
        pour(0, (jug1+jug2))
    else:
        pour(jug1-(max2-jug2), (max2-jug2)+jug2)
 
max1 = int(input("Enter Jug1 Capacity: "))
max2 = int(input("Enter Jug2 Capacity: "))
fill = int(input("Enter Target: "))
pour(0, 0)
info = {
        'Jug 1': j1, 
        'Jug 2': j2
    }
table = tabulate(info, headers='keys', showindex=False, tablefmt='fancy_grid')
print(table)
