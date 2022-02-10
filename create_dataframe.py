import pandas as pd

# df = pd.read_csv("stds.csv")
student_records = {
    'sid': [101,102,103,104],
    'name': ['Abhi', 'PK', 'Aadi', 'Gaurav'],
    'address': ['Odisa', 'Rajsthan', 'Allahabad', 'Jaunpur'],
    'marks': [65,78,52,89],
}

# here we create a DataFrame
df = pd.DataFrame(student_records)
# print(df)

# here we print the shape of dataframe.
rows, columns = df.shape
print(rows, columns)

# print here head.
print(df.head())
print()
# here print only starting 2 rows data..
print(df.head(2))
print()

print(df.tail())
print()
# here print only starting 2 rows data..
print(df.tail(2))

print("After Slice")

# now here we using THE slice

print(df[2:4])
print()
print("Know about cloumns in DF")
print(df.columns)

# here we access a particular cloumns
print()
print("Access particular cloumns in DF")
print(df['name'])

# here we check a type of particular cloumns
print()
print("Access particular cloumns in DF")
print(type(df['name']))

# here we Access more than 2 cloumns
print()
print("Access particular cloumns in DF")
# print(df['name', 'address']) # KeyError: ('name', 'address')

print(df[['name', 'address']])

# print(df.describe())
print()
# here we check conditonal
print(df[df.sid>103])

# here apply check contion for particular column.
print()
print(df[['sid', 'name']][df.marks==df['marks'].max()])
