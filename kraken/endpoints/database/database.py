import psycopg2

from .config import config

def connect(insert_records):
    connection = None
    params = config()

    try:
        print('Connecting to database ...')

        #create connection
        connection = psycopg2.connect(**params)

        #create cursor
        cursor = connection.cursor()

        #wireframe SQL statement
        postgres_statement = 'INSERT INTO kraken_data VALUES({txid}, {userref}, {timestamp}, {pair}, {order_type}, {order}, {status}, {tok_price}, {volume}, {fee}, {total_cost})'

        for row in insert_records:
            print(postgres_statement.format(**row))
            
        
        #connection.commit()

        cursor.execute('SELECT * FROM kraken_data')
        display = cursor.fetchall()
        print(display)
        
        #close cursor
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            #close connections
            connection.close()
            print('Database connection terminated.')


if __name__ == '__main__':
    connect()