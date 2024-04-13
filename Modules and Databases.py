#!/usr/bin/env python
# coding: utf-8

# 11.1 Create a file called zoo.py. In it, define a function called hours() that prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.

# In[11]:


get_ipython().run_cell_magic('writefile', 'zoo.py', "\ndef hours():\n    print('Open 9-5 daily')\n")


# import the zoo module and call its hours() function.

# In[12]:


import zoo
zoo.hours()


# 11.2 In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

# In[13]:


import zoo as menagerie

menagerie.hours()


# 16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 16.4. As in 16.6, select and print the title column from the book table in alphabetical order.

# In[15]:


import csv

data = [
    ['title', 'author', 'year'],
    ['The Weirdstone of Brisingamen', 'Alan Garner', 1960],
    ['Perdido Street Station', 'China Miéville', 2000],
    ['Thud!', 'Terry Pratchett', 2005],
    ['The Spellman Files', 'Lisa Lutz', 2007],
    ['Small Gods', 'Terry Pratchett', 1992]
]

with open('books2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)


# In[16]:


import sqlite3

conn = sqlite3.connect('books.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    title TEXT,
                    author TEXT,
                    year INTEGER
                  )''')

conn.commit()
conn.close()


# In[17]:


import csv
import sqlite3

conn = sqlite3.connect('books.db')

cursor = conn.cursor()

with open('books2.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  
    for row in csvreader:
        cursor.execute('INSERT INTO books VALUES (?, ?, ?)', row)

conn.commit()
conn.close()


# In[18]:


import sqlite3

conn = sqlite3.connect('books.db')

cursor = conn.cursor()

cursor.execute('SELECT title FROM books ORDER BY title')
print("Titles in alphabetical order:")
for row in cursor.fetchall():
    print(row[0])

conn.close()


# In[19]:


import sqlite3

conn = sqlite3.connect('books.db')

cursor = conn.cursor()

cursor.execute('SELECT * FROM books ORDER BY year')
print("\nBooks ordered by publication year:")
for row in cursor.fetchall():
    print(row)

conn.close()


# In[24]:


from sqlalchemy import create_engine, Table, MetaData, select

engine = create_engine('sqlite:///books.db')

metadata = MetaData()
metadata.reflect(engine)
books_table = metadata.tables['books']

with engine.connect() as conn:
    stmt = select(books_table.columns.title).order_by(books_table.columns.title)
    result = conn.execute(stmt)
    print("\nTitles in alphabetical order (using SQLAlchemy):")
    for row in result:
        print(row[0])


# In[ ]:




