df = pd.read_csv('HousePrices.csv', parse_dates=['date'], index_col=['date'])
df.sort_index(inplace=True)

df.head()

plt.plot(df['price'])

plt.hist(df['sqft_living'])

plt.xlabel('price')
plt.ylabel('sqft_living')
plt.title('Scatter Plot')
plt.scatter(x=df['price'], y=df['sqft_living'])

d = {'a': 10, 'b': 20, 'c': 13}

plt.bar(x=d.keys(), height=d.values())

plt.pie(x=d.values(), labels=d.keys())

plt.plot(df['price'])

plt.figure(figsize=(15, 10), dpi=100)
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Line Plot of Prices')
plt.legend()
plt.plot(df['price'])
