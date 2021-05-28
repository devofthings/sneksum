import hashlib
import sqlite3
from sqlite3 import Error

# setting md5 var
md5 = hashlib.md5();

# get filename
print("hiss, muchaho! you want me to create a sneksum for ya?")
filename = input("no problemos just enter the name of the textfile (.txt) in quotes:")

# opening and closing a file in readonly mode with the filename the user provides 
snekfile = open(filename,"r")
content = snekfile.read()
snekfile.close()

# generate & print checksum
md5.update(content)
print("thiss is your checksum:")
print(md5.hexdigest())


#fun with databses
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_sneksumentry(conn, entry):
    """
    Create a new checksum into the sneksum table
    :param conn:
    :param entry:
    :return: entry id
    """
    sql = ''' INSERT INTO sneksums(filename,checksum)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, entry)
    conn.commit()

def main():
    database = r"sneksum.db"

    sql_create_sneksums_table = """ CREATE TABLE IF NOT EXISTS sneksums (
                                        id integer PRIMARY KEY,
                                        filename text NOT NULL,
                                        checksum NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create sneksums table
        create_table(conn, sql_create_sneksums_table)
    else:
        print("Error! cannot create the database connection.")

    with conn:
        # create a new entry
        sneksum_entry = (filename, md5.hexdigest())
        create_sneksumentry(conn, sneksum_entry)

if __name__ == '__main__':
    main()

print("thanksss and see ya soon matey!")