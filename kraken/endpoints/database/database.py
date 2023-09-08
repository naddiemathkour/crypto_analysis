import psycopg2

from .config import config

def connect(records):
    connection = None
    params = config()

    try:
        print('Connecting to database ...')

        #create connection
        connection = psycopg2.connect(**params)

        #create cursor
        cursor = connection.cursor()

        #wireframe SQL statement
        postgres_statement = "INSERT INTO kraken_data VALUES('{txid}', '{userref}', '{timestamp}', '{pair}', '{order_type}', '{order}', '{status}', '{tok_price}', '{volume}', '{fee}', '{total_cost}')"
        
        #insert all rows in insert_records
        for row in records:
            cursor.execute(postgres_statement.format(**row))
        
        #commit inserts
        connection.commit()

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