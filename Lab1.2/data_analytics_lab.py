from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
def getvalue(x): return x.value

year = list(map(getvalue, sheet['A'][1:]))
temp = list(map(getvalue, sheet['C'][1:]))
sun = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(year, temp, label='Температура, С', color='red')
pyplot.plot(year, sun, label='Активность Солнца', color='green')
pyplot.grid(True)
pyplot.title('График зависимости изменения температуры от активности Солнца')
pyplot.show()

