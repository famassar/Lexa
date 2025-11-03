import mysql.connector
from mysql.connector import Error
import configparser

def read_db_config(filename='config.ini', section='Database_GLPI'):
    parser = configparser.ConfigParser()
    parser.read(filename)
    
    db_config = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db_config[item[0]] = item[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    
    return db_config

def fetch_data_from_table(source_config, table_name):
    try:
        source_connection = mysql.connector.connect(**source_config)
        if source_connection.is_connected():
            cursor = source_connection.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM {table_name} WHERE disabled = '0' AND inserted = '0' AND deleted = '0'")
            data = cursor.fetchall()
            cursor.close()
            return data
    except Error as e:
        print(f"Error reading data from MariaDB: {e}")
    finally:
        if source_connection.is_connected():
            source_connection.close()

def insert_data_to_table(dest_config, table_name, data):
    try:
        dest_connection = mysql.connector.connect(**dest_config)
        if dest_connection.is_connected():
            cursor = dest_connection.cursor()
            if data:
                columns = ", ".join(data[0].keys())
                values_placeholder = ", ".join(["%s"] * len(data[0]))
                insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_placeholder})"
                for row in data:
                    cursor.execute(insert_query, list(row.values()))
                dest_connection.commit()
                cursor.close()
                print(f"Data successfully inserted into {table_name}")
            else:
                print("No data found in source table")
    except Error as e:
        print(f"Error inserting data into MariaDB: {e}")
    finally:
        if dest_connection.is_connected():
            dest_connection.close()

def update_source_table(source_config, table_name, primary_keys):
    try:
        source_connection = mysql.connector.connect(**source_config)
        if source_connection.is_connected():
            cursor = source_connection.cursor()
            update_query = f"UPDATE {table_name} SET inserted = '1' WHERE host_name = %s"
            for pk in primary_keys:
                cursor.execute(update_query, (pk,))
            source_connection.commit()
            cursor.close()
            print(f"Source table {table_name} successfully updated")
    except Error as e:
        print(f"Error updating source table in MariaDB: {e}")
    finally:
        if source_connection.is_connected():
            source_connection.close()

if __name__ == "__main__":
    source_table_name = 'lexa_computers'
    dest_table_name = 'alldata'
    primary_key = 'host_name'  # Sostituisci con il nome della colonna chiave primaria

    source_config = read_db_config(section='Database_GLPI')
    dest_config = read_db_config(section='Database_LEXA')

    data = fetch_data_from_table(source_config, source_table_name)
    insert_data_to_table(dest_config, dest_table_name, data)
    
    # Estrarre le chiavi primarie per aggiornare il campo "inserted"
    primary_keys = [row[primary_key] for row in data]
    update_source_table(source_config, source_table_name, primary_keys)
