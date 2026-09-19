import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ADANIPORTS.csv', parse_dates=True)

df.head()

df['H-L'] = df.High - df.Low
df['100MA'] = df['Close'].rolling(100).mean()

ax = plt.axes(projection='3d')
ax.scatter(df.index, df['H-L'], df['100MA'])
ax.set_xlabel('Index')
ax.set_ylabel('H-L')
ax.set_zlabel('100MA')
plt.show()
