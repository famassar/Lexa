import mysql.connector
import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def get_lexa_data(cursor):
    query = "SELECT pcid, hostname, ip from lexa_rundeck where status NOT LIKE('Obsoleto') AND status NOT LIKE('Spento')"
    cursor.execute(query)
    return cursor.fetchall()

def update_glpi_data(cursor, pcid, hostname, ip):
    update_query = """
    UPDATE glpi_plugin_fields_computerlexas
    SET visiblenamealiasfield = %s, fqdnfield = %s, realipfield = %s
    WHERE items_id = %s
    """
    fqdn_value = f"{hostname}.internal.ausl.bologna.it"
    cursor.execute(update_query, (hostname, fqdn_value, ip, pcid))

def main():
    config = read_config()

    # Connect to the MariaDB database
    db_config = {
        'user': config['Database_GLPI']['user'],
        'password': config['Database_GLPI']['password'],
        'host': config['Database_GLPI']['host'],
        'database': config['Database_GLPI']['database']
    }
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        # Read data from lexa_rundeck table
        lexa_data = get_lexa_data(cursor)

        # Update glpi_plugin_fields_computerlexas table
        for pcid, hostname, ip in lexa_data:
            update_glpi_data(cursor, pcid, hostname, ip)

        # Commit the changes to the database
        conn.commit()
        print("GLPI database updated successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
