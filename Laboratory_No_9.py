import pyodbc


try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                 r'DBQ=C:\Users\parwizforogh\Documents\msdatabase.accdb;'
    conn = pyodbc.connect(con_string)

    cursor = conn.cursor()

    myuser = (

        (6, 'data', 'data@gmail.com'),
        (7, 'python', 'python@gnail.com'),
        (8, 'java', 'java@gmail.com'),

    )

    cursor.executemany('INSERT INTO users VALUES (?,?,?)', myuser)
    conn.commit()
    print('Data Inserted')


except pyodbc.Error as e:
    print("Error in connection", e)