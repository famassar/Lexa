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

def fetch_data_from_table(source_config, table_name, field_name):
    try:
        source_connection = mysql.connector.connect(**source_config)
        if source_connection.is_connected():
            cursor = source_connection.cursor(dictionary=True)
            cursor.execute(f"SELECT {field_name} FROM {table_name} WHERE deleted = '1'")
            data = cursor.fetchall()
            cursor.close()
            return data
    except Error as e:
        print(f"Error reading data from MariaDB: {e}")
    finally:
        if source_connection.is_connected():
            source_connection.close()

def update_data_in_table(dest_config, table_name, field_name, field_values, fixed_value):
    try:
        dest_connection = mysql.connector.connect(**dest_config)
        if dest_connection.is_connected():
            cursor = dest_connection.cursor()
            update_query = f"UPDATE {table_name} SET deleted = %s WHERE {field_name} = %s"
            for value in field_values:
                cursor.execute(update_query, (fixed_value, value[field_name]))
            dest_connection.commit()
            cursor.close()
            print(f"Data successfully updated in {table_name}")
    except Error as e:
        print(f"Error updating data in MariaDB: {e}")
    finally:
        if dest_connection.is_connected():
            dest_connection.close()

if __name__ == "__main__":
    source_table_name = 'lexa_computers'
    dest_table_name = 'alldata'
    field_name = 'host_name'  # Campo da usare per la corrispondenza
    fixed_value = '1'  # Valore fisso da inserire

    source_config = read_db_config(section='Database_GLPI')
    dest_config = read_db_config(section='Database_LEXA')

    data = fetch_data_from_table(source_config, source_table_name, field_name)
    
    # Aggiornare i record nel database B
    update_data_in_table(dest_config, dest_table_name, field_name, data, fixed_value)
