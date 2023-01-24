import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv(r'path_to_the_file')

X = [str(i) for i in data['first_column']]
Y = data['second_column']


plt.bar(X, Y, color='blue')
plt.xticks(rotation=50)
plt.grid(axis='y', linewidth=0.5)
plt.title("title")
plt.tight_layout()


plt.savefig('name_of_the_file.png', format='png')
