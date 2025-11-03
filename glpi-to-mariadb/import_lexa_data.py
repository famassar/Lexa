import mysql.connector
import subprocess
import configparser

# Load database configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Retrieve database connection parameters
db_config = {
    'user': config['Database_GLPI']['user'],
    'password': config['Database_GLPI']['password'],
    'host': config['Database_GLPI']['host'],
    'database': config['Database_GLPI']['database']
}
# Connect to the MariaDB database
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Execute the first SQL query to update realipfield
    update_real_ip_query = """
    UPDATE glpi_plugin_fields_computerlexas 
    JOIN lexa_interfaces ON glpi_plugin_fields_computerlexas.id = lexa_interfaces.pcid 
    SET glpi_plugin_fields_computerlexas.realipfield = lexa_interfaces.ip;
    """
    
    cursor.execute(update_real_ip_query)
    connection.commit()
    print("Executed additional query to update realipfield.")

    # Execute the second SQL query to update visiblenamealiasfield
    update_visible_name_alias_query = """
    UPDATE glpi_plugin_fields_computerlexas 
    JOIN lexa_interfaces ON glpi_plugin_fields_computerlexas.id = lexa_interfaces.pcid 
    SET glpi_plugin_fields_computerlexas.visiblenamealiasfield = lexa_interfaces.hostname;
    """
    
    cursor.execute(update_visible_name_alias_query)
    connection.commit()
    print("Executed additional query to update visiblenamealiasfield.")

    # 1. Extract values from a MariaDB table field
    select_query = "select host_name  FROM lexa_computers"
    cursor.execute(select_query)
    results = cursor.fetchall()  # Fetch all rows

    if results:
        for row in results:
            extracted_value = row[0]
            print(f"Extracted Value: {extracted_value}")

            # 2. Call the system command "host" using the extracted value
            try:
                host_command = subprocess.run(['host', extracted_value], capture_output=True, text=True, check=True)
                command_output = host_command.stdout.strip()
                print(f"Host Command Output: {command_output}")

                # Use only the first field of the output
                first_field = command_output.split()[0] if command_output else None
                print(f"First Field: {first_field}")

                # 3. Update all rows in another table using the extracted values
                update_query = """
                UPDATE glpi_plugin_fields_computerlexas
                SET visiblenamealiasfield = %s, fqdnfield = %s where visiblenamealiasfield = %s"""
                cursor.execute(update_query, (extracted_value, first_field, extracted_value))
                connection.commit()
                print(f"Updated {cursor.rowcount} rows in another_table.")
                
            except subprocess.CalledProcessError as e:
                print(f"Error executing host command for {extracted_value}: {e}")

    else:
        print("No results found.")

except mysql.connector.Error as err:
    print(f"Database error: {err}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
