import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=sample_database;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('''
		CREATE TABLE products (
			product_id int primary key,
			product_name nvarchar(50),
			price int
			)
               ''')

conn.commit()
