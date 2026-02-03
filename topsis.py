import sys
import pandas as pd
import numpy as np

if len(sys.argv) != 5:
    print("Error: Incorrect number of parameters")
    sys.exit()

file = sys.argv[1]
weights = sys.argv[2].split(',')
impacts = sys.argv[3].split(',')
out = sys.argv[4]

try:
    df = pd.read_csv(file)
except:
    print("Error: File not found")
    sys.exit()

if df.shape[1] < 3:
    print("Error: Input file must contain three or more columns")
    sys.exit()

data = df.iloc[:, 1:]

try:
    data = data.astype(float)
except:
    print("Error: From 2nd to last columns must contain numeric values only")
    sys.exit()

if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
    print("Error: Number of weights, impacts and columns must be same")
    sys.exit()

for i in impacts:
    if i not in ['+', '-']:
        print("Error: Impacts must be either + or -")
        sys.exit()

weights = [float(i) for i in weights]

norm = (data*2).sum()*0.5
data = data / norm
data = data * weights

best = []
worst = []

for i in range(len(impacts)):
    if impacts[i] == '+':
        best.append(max(data.iloc[:, i]))
        worst.append(min(data.iloc[:, i]))
    else:
        best.append(min(data.iloc[:, i]))
        worst.append(max(data.iloc[:, i]))

best = np.array(best)
worst = np.array(worst)

d1 = ((data - best)*2).sum(axis=1)*0.5
d2 = ((data - worst)*2).sum(axis=1)*0.5

score = d2 / (d1 + d2)

df['Topsis Score'] = score
df['Rank'] = score.rank(ascending=False)

df.to_csv(out, index=False)