import requests
import csv
import json

# Zabbix API configuration
ZABBIX_URL = 'http://zabbixtest.hexgroup.net/api_jsonrpc.php'  # Replace with your Zabbix URL
BEARER_TOKEN = '97068681fa09d02ce64ede8043f873f44883c30595df39a490922f5841bcc70f'  # Replace with your Bearer token

# Function to get all hosts and their interfaces
def get_hosts_and_interfaces():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {BEARER_TOKEN}'
    }
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["hostid", "host"],
            "selectInterfaces": ["interfaceid", "ip"]  # Get interface details
        },
        "id": 1
    }
    response = requests.post(ZABBIX_URL, headers=headers, data=json.dumps(data))
    return response.json().get('result', [])

# Function to write hosts and interfaces to a CSV file
def write_hosts_to_csv(hosts, filename='hosts.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Host ID', 'Host Name', 'Interface ID', 'IP Address'])  # Write header
        for host in hosts:
            for interface in host.get('interfaces', []):
                writer.writerow([host['hostid'], host['host'], interface['interfaceid'], interface['ip']])  # Write data

def main():
    # Get all hosts and their interfaces
    hosts = get_hosts_and_interfaces()
    if not hosts:
        print("No hosts found.")
        return

    # Write hosts to CSV
    write_hosts_to_csv(hosts)
    print(f"Successfully written {len(hosts)} hosts to hosts.csv")

if __name__ == "__main__":
    main()