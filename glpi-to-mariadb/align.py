import mysql.connector
import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def get_lexa_data(cursor):
    query = "SELECT host_name, inserted, updated FROM alldata WHERE visible_name IS NOT NULL"
    cursor.execute(query)
    return cursor.fetchall()

def update_glpi_data(cursor, host_name, inserted, updated):
    update_query = """
    UPDATE glpi_plugin_fields_computerlexas
    SET insertedinzabbixfield = %s, updatedfield = %s
    WHERE visiblenamealiasfield = %s
    """
    cursor.execute(update_query, (inserted, updated, host_name))

def main():
    config = read_config()

    # Connect to the LEXA database
    lexa_db_config = {
        'user': config['Database_LEXA']['user'],
        'password': config['Database_LEXA']['password'],
        'host': config['Database_LEXA']['host'],
        'database': config['Database_LEXA']['database']
    }
    
    lexa_conn = mysql.connector.connect(**lexa_db_config)
    lexa_cursor = lexa_conn.cursor()

    # Connect to the GLPI database
    glpi_db_config = {
        'user': config['Database_GLPI']['user'],
        'password': config['Database_GLPI']['password'],
        'host': config['Database_GLPI']['host'],
        'database': config['Database_GLPI']['database']
    }
    
    glpi_conn = mysql.connector.connect(**glpi_db_config)
    glpi_cursor = glpi_conn.cursor()

    try:
        # Read data from LEXA database
        lexa_data = get_lexa_data(lexa_cursor)

        # Update GLPI database
        for host_name, inserted, updated in lexa_data:
            update_glpi_data(glpi_cursor, host_name, inserted, updated)

        # Commit the changes to the GLPI database
        glpi_conn.commit()
        print("GLPI database updated successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        glpi_conn.rollback()

    finally:
        # Close all connections
        lexa_cursor.close()
        lexa_conn.close()
        glpi_cursor.close()
        glpi_conn.close()

if __name__ == "__main__":
    main()
