import pandas
import os
absolute_path = os.path.abspath(os.path.dirname('pollution_data.csv'))
fh = pandas.read_csv(absolute_path + '/pollution_data.csv')
import matplotlib.pyplot as plt
fh.plot(kind="scatter", x="x", y="y")
plt.show()