import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from pandas.plotting import parallel_coordinates
import seaborn as sns

df = pd.read_excel('oprd_param_comparison.xlsx',sheet_name='pr3_opr3_uts')
df.sort_values('Vbur_Boltz_OPR3',inplace=True)
#Dumbbell plot (https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#19.-Dumbbell-Plot)

my_range=range(1,len(df.index)+1)
plt.figure(figsize=(10.75,4.8))
plt.hlines(y=my_range, xmin=df['Vbur_Boltz_OPR3'], xmax=df['Vbur_Boltz_PR3'], color='grey', alpha=0.4)
plt.scatter(df['Vbur_Boltz_OPR3'], my_range, marker="v", color='#BCE0F0', alpha=1, label='Phosphine Oxide',edgecolors="black")
plt.scatter(df['Vbur_Boltz_PR3'], my_range, color='#5A7593', alpha=1 , label='Phosphine',edgecolors="black")
plt.legend()

plt.yticks(my_range, df['ligand'])
plt.title("Phosphine Oxide and Phosphine Parameter Comparison", loc='left')
plt.xlabel('Percent Buried Volume (Boltzmann averaged)')
plt.ylabel('Ligand')
plt.show()

df.sort_values('vmin_Boltz_OPR3',inplace=True)
my_range=range(1,len(df.index)+1)
plt.figure(figsize=(10.75,4.8))
plt.hlines(y=my_range, xmin=df['vmin_Boltz_OPR3'], xmax=df['vmin_Boltz_PR3'], color='grey', alpha=0.4)
plt.scatter(df['vmin_Boltz_OPR3'], my_range, marker="v", color='#BCE0F0', alpha=1, label='Phosphine Oxide',edgecolors="black")
plt.scatter(df['vmin_Boltz_PR3'], my_range, color='#5A7593', alpha=1 , label='Phosphine',edgecolors="black")
plt.legend()

plt.yticks(my_range, df['ligand'])
plt.title("Phosphine Oxide and Phosphine Parameter Comparison", loc='left')
plt.xlabel('vmin (Boltzmann averaged)')
plt.ylabel('Ligand')
plt.show()

df.sort_values('pyr_Boltz_OPR3',inplace=True)
my_range=range(1,len(df.index)+1)
plt.figure(figsize=(10.75,4.8))
plt.hlines(y=my_range, xmin=df['pyr_Boltz_OPR3'], xmax=df['pyr_Boltz_PR3'], color='grey', alpha=0.4)
plt.scatter(df['pyr_Boltz_OPR3'], my_range, marker="v", color='#BCE0F0', alpha=1, label='Phosphine Oxide',edgecolors="black")
plt.scatter(df['pyr_Boltz_PR3'], my_range, color='#5A7593', alpha=1 , label='Phosphine',edgecolors="black")
plt.legend()

plt.yticks(my_range, df['ligand'])
plt.title("Phosphine Oxide and Phosphine Parameter Comparison", loc='left')
plt.xlabel('Pyramidalization (Boltzmann averaged)')
plt.ylabel('Ligand')
plt.show()

#Slope chart (https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#18.-Slope-Chart)
# parallel_coordinates(df,'ligand',colormap='ocean',cols=['vmin_Boltz_OPR3','Vmin_LP(P)_Boltz_PR3'])
# plt.show()

# def newline(p1, p2, color='black'):
#     ax = plt.gca()
#     l = mlines.Line2D([p1[0],p2[0]], [p1[1],p2[1]], color='red' if p1[1]-p2[1] > 0 else 'green', marker='o', markersize=6)
#     ax.add_line(l)
#     return l

# left_label = [str(c) + ', '+ str(round(y)) for c, y in zip(df.ligand, df['Vbur_Boltz_OPR3'])]
# right_label = [str(c) + ', '+ str(round(y)) for c, y in zip(df.ligand, df['Vbur_Boltz_PR3'])]
# klass = ['red' if (y1-y2) < 0 else 'green' for y1, y2 in zip(df['Vbur_Boltz_OPR3'], df['Vbur_Boltz_PR3'])]

# fig, ax = plt.subplots(1,1,figsize=(20,20), dpi= 80)

# ax.vlines(x=1,ymin=25,ymax=75,color='black', alpha=0.7, linewidth=1, linestyles='dotted')
# ax.vlines(x=3,ymin=25,ymax=75,color='black', alpha=0.7, linewidth=1, linestyles='dotted')

# # Points
# ax.scatter(y=df['Vbur_Boltz_OPR3'], x=np.repeat(1, df.shape[0]), s=10, color='black', alpha=0.7)
# ax.scatter(y=df['Vbur_Boltz_PR3'], x=np.repeat(3, df.shape[0]), s=10, color='black', alpha=0.7)

# # Line Segmentsand Annotation
# for p1, p2, c in zip(df['Vbur_Boltz_OPR3'], df['Vbur_Boltz_PR3'], df['ligand']):
#     newline([1,p1], [3,p2])
#     ax.text(1-0.05, p1, c + ', ' + str(round(p1)), horizontalalignment='right', verticalalignment='center', fontdict={'size':14})
#     ax.text(3+0.05, p2, c + ', ' + str(round(p2)), horizontalalignment='left', verticalalignment='center', fontdict={'size':14})

# # 'Before' and 'After' Annotations
# ax.text(1-0.05, 100, 'OPR3', horizontalalignment='right', verticalalignment='center', fontdict={'size':18, 'weight':700})
# ax.text(3+0.05, 100, 'PR3', horizontalalignment='left', verticalalignment='center', fontdict={'size':18, 'weight':700})

# # Decoration
# #ax.set_title("Slopechart: Comparing GDP Per Capita between 1952 vs 1957", fontdict={'size':22})
# ax.set(xlim=(0,4), ylim=(0,100), ylabel='Percent buried volume')
# ax.set_xticks([1,3])
# ax.set_xticklabels(["Vbur_Boltz_OPR3", "Vbur_Boltz_PR3"])
# plt.yticks(np.arange(25, 100, 5), fontsize=12)

# # Lighten borders
# plt.gca().spines["top"].set_alpha(.0)
# plt.gca().spines["bottom"].set_alpha(.0)
# plt.gca().spines["right"].set_alpha(.0)
# plt.gca().spines["left"].set_alpha(.0)
# plt.show()

