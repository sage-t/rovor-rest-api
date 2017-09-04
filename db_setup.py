# This creates and sets up a new database
import sqlite3

sqlite_file = 'db/rovor-api.sqlite'    # name of the sqlite database file
# table_name1 = 'deals'  # name of the table to be created
# table_name2 = 'alerts'  # name of the table to be created
# new_field = 'my_1st_column' # name of the column
# field_type = 'INTEGER'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE deals (' +
                                'start_airport text NOT NULL,' +
                                'end_airport text NOT NULL,' +
                                'price integer NOT NULL,' +
                                'outbound_date text NOT NULL,' +
                                'inbound_date text,' +
                                'link text NOT NULL,' +
                                'timestamp DATETIME DEFAULT CURRENT_TIMESTAMP' +
                              ')')

# Creating a new SQLite table with 1 column
# c.execute('CREATE TABLE {tn} ({nf} {ft})'\
#         .format(tn=table_name1, nf=new_field, ft=field_type))

# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
# c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
#         .format(tn=table_name2, nf=new_field, ft=field_type))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()


