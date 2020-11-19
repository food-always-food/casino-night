import sqlite3
import pandas as pd

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE stocks (date text, symbol text, third text)")
cur.execute("INSERT INTO stocks VALUES ('test','DTFY','more shit')")
cur.execute("INSERT INTO stocks VALUES ('tes2t','DTFY','another i guess')")
conn.commit()
cur.close()
conn.row_factory = dict_factory
cur = conn.cursor()
cur.execute("SELECT * FROM stocks")
# print(cur.description)
result = cur.fetchall()
print(result)
for row in result:
    print(row)

df = pd.read_sql_query("Select * From stocks", conn)

conn.close()

# print(df)

# for x in df.iterrows():
    # print(x)
