# https://www.python-graph-gallery.com/connected-scatter-plot/
# https://www.geeksforgeeks.org/reading-excel-file-using-python/


import matplotlib.pyplot as plt
import pandas as pd
import openpyxl

from_xl = pd.read_excel('ten.xlsx', sheet_name='Sheet2')
print(from_xl.head(4)) # see if ok


# data

df = pd.DataFrame({
    'x_axis': from_xl['a(%)'],
    'y_axis': from_xl['b(Pa)']
})

# plot
plt.plot('x_axis', 'y_axis', data=df, linestyle='-')
plt.title('b(Pa) vs a(%)')
plt.xlabel('a(%)')
plt.ylabel('b(Pa)')
plt.show()


