import mysql.connector
import requests
import configparser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import json

class Host:
    def __init__(self, hostid, host_name, visible_name, description, disabled):
        self.hostid=hostid
        self.host_name=host_name
        self.visible_name=visible_name
        self.description=description
        self.disabled=disabled

class If:
    def __init__(self, interfaceid, hostid, type, ip, dns, useip, port, main):
        self.interfaceid=interfaceid
        self.hostid=hostid
        self.type=type
        self.ip=ip
        self.dns=dns
        self.useip=useip
        self.port=port
        self.main=main        

class Inv:
    def __init__(self, hostid, type, type_full, name, alias, os, os_full, os_short, serialno_a, serialno_b, tag, asset_tag, macaddress_a, macaddress_b, hardware, hardware_full, software, software_full, software_app_a, software_app_b, software_app_c, software_app_d, software_app_e, contact, location, location_lat, location_lon, notes, chassis, model, hw_arch, vendor, contract_number, installer_name, deployment_status, url_a, url_b, url_c, host_networks, host_netmask, host_router, oob_ip, oob_netmask, oob_router, date_hw_purchase, date_hw_install, date_hw_expiry, date_hw_decomm, site_address_a, site_address_b, site_address_c, site_city, site_state, site_country, site_zip, site_rack, site_notes, poc_1_name, poc_1_email, poc_1_phone_a, poc_1_phone_b, poc_1_cell, poc_1_screen, poc_1_notes, poc_2_name, poc_2_email, poc_2_phone_a, poc_2_phone_b, poc_2_cell, poc_2_screen, poc_2_notes):
        self.hostid=hostid
        self.type=type
        self.type_full=type_full
        self.name=name
        self.alias=alias
        self.os=os
        self.os_full=os_full
        self.os_short=os_short
        self.serialno_a=serialno_a
        self.serialno_b=serialno_b
        self.tag=tag
        self.asset_tag=asset_tag
        self.macaddress_a=macaddress_a
        self.macaddress_b=macaddress_b
        self.hardware=hardware
        self.hardware_full=hardware_full
        self.software=software
        self.software_full=software_full
        self.software_app_a=software_app_a
        self.software_app_b=software_app_b
        self.software_app_c=software_app_c
        self.software_app_d=software_app_d
        self.software_app_e=software_app_e
        self.contact=contact
        self.location=location
        self.location_lat=location_lat
        self.location_lon=location_lon
        self.notes=notes
        self.chassis=chassis
        self.model=model
        self.hw_arch=hw_arch
        self.vendor=vendor
        self.contract_number=contract_number
        self.installer_name=installer_name
        self.deployment_status=deployment_status
        self.url_a=url_a
        self.url_b=url_b
        self.url_c=url_c
        self.host_networks=host_networks
        self.host_netmask=host_netmask
        self.host_router=host_router
        self.oob_ip=oob_ip
        self.oob_netmask=oob_netmask
        self.oob_router=oob_router
        self.date_hw_purchase=date_hw_purchase
        self.date_hw_install=date_hw_install
        self.date_hw_expiry=date_hw_expiry
        self.date_hw_decomm=date_hw_decomm
        self.site_address_a=site_address_a
        self.site_address_b=site_address_b
        self.site_address_c=site_address_c
        self.site_city=site_city
        self.site_state=site_state
        self.site_country=site_country
        self.site_zip=site_zip
        self.site_rack=site_rack
        self.site_notes=site_notes
        self.poc_1_name=poc_1_name
        self.poc_1_email=poc_1_email
        self.poc_1_phone_a=poc_1_phone_a
        self.poc_1_phone_b=poc_1_phone_b
        self.poc_1_cell=poc_1_cell
        self.poc_1_screen=poc_1_screen
        self.poc_1_notes=poc_1_notes
        self.poc_2_name=poc_2_name
        self.poc_2_email=poc_2_email
        self.poc_2_phone_a=poc_2_phone_a
        self.poc_2_phone_b=poc_2_phone_b
        self.poc_2_cell=poc_2_cell
        self.poc_2_screen=poc_2_screen
        self.poc_2_notes=poc_2_notes

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Database'], config['Zabbix'], config ['Email']

def get_hosts_from_zabbix(zabbix_config):

    bearer = f"{zabbix_config['ZABBIX_TOKEN']}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + bearer
        }
    
    api_url = f"{zabbix_config['ZABBIX_URL']}/api_jsonrpc.php"
    
    # Creazione della richiesta JSON per ottenere gli host da Zabbix
    payload = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
           "tags": [
            {
                "tag": "Lexa",
                "operator": 1
            }
        ],
       "output": ["hostid", "host", "name", "description", "status"]
    },
    "id": 1
}

    # Invio della richiesta HTTP
    response = requests.post(api_url, headers=headers, json=payload)

    # Gestione della risposta
    if response.status_code == 200:
        result = response.json().get('result')
        if result:
            return [Host(host['hostid'], host['host'], host['name'], host['description'], host['status']) for host in result]
    else:
        print(f"Failed to get hosts from Zabbix: {response.text}")

    return []

def insert_hosts_into_database(db_config, hosts):
    connection = mysql.connector.connect(
        host=db_config['DB_HOST'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        database=db_config['DB_NAME'],
        port=db_config['DB_PORT']
    )

    cursor = connection.cursor()

    # Pulizia della tabella nel database
    
    truncate_table_query = ("TRUNCATE datacheck")

    cursor.execute(truncate_table_query)

    # Inserisci nuovi host nella tabella
    for host in hosts:
        insert_query = "INSERT INTO datacheck (hostid, host_name, visible_name, description, disabled, interface_type, interface_ip_address, interface_dns, interface_use_ip, interface_port, interface_default, inserted, updated, deleted, `type`, type_full, name, alias, os, os_full, os_short, serialno_a, serialno_b, tag, asset_tag, macaddress_a, macaddress_b, hardware, hardware_full, software, software_full, software_app_a, software_app_b, software_app_c, software_app_d, software_app_e, contact, location, location_lat, location_lon, notes, chassis, model, hw_arch, vendor, contract_number, installer_name, deployment_status, url_a, url_b, url_c, host_networks, host_netmask, host_router, oob_ip, oob_netmask, oob_router, date_hw_purchase, date_hw_install, date_hw_expiry, date_hw_decomm, site_address_a, site_address_b, site_address_c, site_city, site_state, site_country, site_zip, site_rack, site_notes, poc_1_name, poc_1_email, poc_1_phone_a, poc_1_phone_b, poc_1_cell, poc_1_screen, poc_1_notes, poc_2_name, poc_2_email, poc_2_phone_a, poc_2_phone_b, poc_2_cell, poc_2_screen, poc_2_notes) VALUES(%s, %s, %s, %s, %s, 1, NULL, NULL, NULL, NULL, 1, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)"

        data = (host.hostid, host.host_name, host.visible_name, host.description, host.disabled)
        cursor.execute(insert_query, data)

    connection.commit()

    cursor.close()
    connection.close()

def get_if_from_zabbix(zabbix_config):

    bearer = f"{zabbix_config['ZABBIX_TOKEN']}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + bearer
        }
    
    api_url = f"{zabbix_config['ZABBIX_URL']}/api_jsonrpc.php"
    
    # Creazione della richiesta JSON per ottenere gli host da Zabbix
    payload = {
    "jsonrpc": "2.0",
    "method": "hostinterface.get",
    "params": { 
			"output": ["interfaceid", "hostid", "type", "ip", "dns", "useip", "port", "main"]
							},
    "id": 1
    }

    # Invio della richiesta HTTP
    response = requests.post(api_url, headers=headers, json=payload)

    # Gestione della risposta
    if response.status_code == 200:
        result = response.json().get('result')
        if result:
            return [If(iface['interfaceid'], iface['hostid'], iface['type'], iface['ip'], iface['dns'], iface['useip'], iface['port'], iface['main']) for iface in result]
    else:
        print(f"Failed to get hosts from Zabbix: {response.text}")

    return []

def insert_if_into_database(db_config, ifaces):
    connection = mysql.connector.connect(
        host=db_config['DB_HOST'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        database=db_config['DB_NAME'],
        port=db_config['DB_PORT']
    )

    cursor = connection.cursor()

    # Inserisci nuovi host nella tabella
    for iface in ifaces:
        update_query = "UPDATE datacheck SET interface_type=" + iface.type + ", interface_ip_address='" + iface.ip + "', interface_dns='" + iface.dns + "', interface_use_ip=" + iface.useip + ", interface_port='" + iface.port + "', interface_default=" + iface.main + " WHERE datacheck.hostid=" + iface.hostid
        cursor.execute(update_query)

    connection.commit()

    cursor.close()
    connection.close()

def get_inv_from_zabbix(zabbix_config):

    bearer = f"{zabbix_config['ZABBIX_TOKEN']}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + bearer
        }
    
    api_url = f"{zabbix_config['ZABBIX_URL']}/api_jsonrpc.php"
    
    # Creazione della richiesta JSON per ottenere gli host da Zabbix
    payload = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "selectTags": "extend",
        "evaltype": 0,
        "tags": [
            {
                "tag": "Lexa",
                "operator": 1
            }
        ],
        "output": ["host"],
        "selectInventory": [
                "type",
				"type_full",
				"name",
				"alias",
				"os",
				"os_full",
				"os_short",
				"serialno_a",
				"serialno_b",
				"tag",
				"asset_tag",
				"macaddress_a",
				"macaddress_b",
				"hardware",
				"hardware_full",
				"software",
				"software_full",
				"software_app_a",
				"software_app_b",
				"software_app_c",
				"software_app_d",
				"software_app_e",
				"contact",
				"location",
				"location_lat",
				"location_lon",
				"notes",
				"chassis",
				"model",
				"hw_arch",
				"vendor",
				"contract_number",
				"installer_name",
				"deployment_status",
				"url_a",
				"url_b",
				"url_c",
				"host_networks",
				"host_netmask",
				"host_router",
				"oob_ip",
				"oob_netmask",
				"oob_router",
				"date_hw_purchase",
				"date_hw_install",
				"date_hw_expiry",
				"date_hw_decomm",
				"site_address_a",
				"site_address_b",
				"site_address_c",
				"site_city",
				"site_state",
				"site_country",
				"site_zip",
				"site_rack",
				"site_notes",
				"poc_1_name",
				"poc_1_email",
				"poc_1_phone_a",
				"poc_1_phone_b",
				"poc_1_cell",
				"poc_1_screen",
				"poc_1_notes",
				"poc_2_name",
				"poc_2_email",
				"poc_2_phone_a",
				"poc_2_phone_b",
				"poc_2_cell",
				"poc_2_screen",
				"poc_2_notes"
        ]
    },
    "id": 1
}

    # Invio della richiesta HTTP
    response = requests.post(api_url, headers=headers, json=payload)

    # Gestione della risposta
    if response.status_code == 200:
        result = response.json().get('result')
        if result:
            return [Inv(elem['hostid'], elem['inventory']['type'], elem['inventory']['type_full'], elem['inventory']['name'], elem['inventory']['alias'], elem['inventory']['os'], elem['inventory']['os_full'], elem['inventory']['os_short'], elem['inventory']['serialno_a'], elem['inventory']['serialno_b'], elem['inventory']['tag'], elem['inventory']['asset_tag'], elem['inventory']['macaddress_a'], elem['inventory']['macaddress_b'], elem['inventory']['hardware'], elem['inventory']['hardware_full'], elem['inventory']['software'], elem['inventory']['software_full'], elem['inventory']['software_app_a'], elem['inventory']['software_app_b'], elem['inventory']['software_app_c'], elem['inventory']['software_app_d'], elem['inventory']['software_app_e'], elem['inventory']['contact'], elem['inventory']['location'], elem['inventory']['location_lat'], elem['inventory']['location_lon'], elem['inventory']['notes'], elem['inventory']['chassis'], elem['inventory']['model'], elem['inventory']['hw_arch'], elem['inventory']['vendor'], elem['inventory']['contract_number'], elem['inventory']['installer_name'], elem['inventory']['deployment_status'], elem['inventory']['url_a'], elem['inventory']['url_b'], elem['inventory']['url_c'], elem['inventory']['host_networks'], elem['inventory']['host_netmask'], elem['inventory']['host_router'], elem['inventory']['oob_ip'], elem['inventory']['oob_netmask'], elem['inventory']['oob_router'], elem['inventory']['date_hw_purchase'], elem['inventory']['date_hw_install'], elem['inventory']['date_hw_expiry'], elem['inventory']['date_hw_decomm'], elem['inventory']['site_address_a'], elem['inventory']['site_address_b'], elem['inventory']['site_address_c'], elem['inventory']['site_city'], elem['inventory']['site_state'], elem['inventory']['site_country'], elem['inventory']['site_zip'], elem['inventory']['site_rack'], elem['inventory']['site_notes'], elem['inventory']['poc_1_name'], elem['inventory']['poc_1_email'], elem['inventory']['poc_1_phone_a'], elem['inventory']['poc_1_phone_b'], elem['inventory']['poc_1_cell'], elem['inventory']['poc_1_screen'], elem['inventory']['poc_1_notes'], elem['inventory']['poc_2_name'], elem['inventory']['poc_2_email'], elem['inventory']['poc_2_phone_a'], elem['inventory']['poc_2_phone_b'], elem['inventory']['poc_2_cell'], elem['inventory']['poc_2_screen'], elem['inventory']['poc_2_notes']) for elem in result]
    else:
        print(f"Failed to get hosts from Zabbix: {response.text}")

    return []

def insert_inv_into_database(db_config, invs):
    connection = mysql.connector.connect(
        host=db_config['DB_HOST'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        database=db_config['DB_NAME'],
        port=db_config['DB_PORT']
    )

    cursor = connection.cursor()

    # Inserisci nuovi host nella tabella
    for inv in invs:
        update_query = "UPDATE datacheck SET type='" + inv.type + "',type_full='" + inv.type_full + "',name='" + inv.name + "',alias='" + inv.alias + "',os='" + inv.os + "',os_full='" + inv.os_full + "',os_short='" + inv.os_short + "',serialno_a='" + inv.serialno_a + "',serialno_b='" + inv.serialno_b + "',tag='" + inv.tag + "',asset_tag='" + inv.asset_tag + "',macaddress_a='" + inv.macaddress_a + "',macaddress_b='" + inv.macaddress_b + "',hardware='" + inv.hardware + "',hardware_full='" + inv.hardware_full + "',software='" + inv.software + "',software_full='" + inv.software_full + "',software_app_a='" + inv.software_app_a + "',software_app_b='" + inv.software_app_b + "',software_app_c='" + inv.software_app_c + "',software_app_d='" + inv.software_app_d + "',software_app_e='" + inv.software_app_e + "',contact='" + inv.contact + "',location='" + inv.location + "',location_lat='" + inv.location_lat + "',location_lon='" + inv.location_lon + "',notes='" + inv.notes + "',chassis='" + inv.chassis + "',model='" + inv.model + "',hw_arch='" + inv.hw_arch + "',vendor='" + inv.vendor + "',contract_number='" + inv.contract_number + "',installer_name='" + inv.installer_name + "',deployment_status='" + inv.deployment_status + "',url_a='" + inv.url_a + "',url_b='" + inv.url_b + "',url_c='" + inv.url_c + "',host_networks='" + inv.host_networks + "',host_netmask='" + inv.host_netmask + "',host_router='" + inv.host_router + "',oob_ip='" + inv.oob_ip + "',oob_netmask='" + inv.oob_netmask + "',oob_router='" + inv.oob_router + "',date_hw_purchase='" + inv.date_hw_purchase + "',date_hw_install='" + inv.date_hw_install + "',date_hw_expiry='" + inv.date_hw_expiry + "',date_hw_decomm='" + inv.date_hw_decomm + "',site_address_a='" + inv.site_address_a + "',site_address_b='" + inv.site_address_b + "',site_address_c='" + inv.site_address_c + "',site_city='" + inv.site_city + "',site_state='" + inv.site_state + "',site_country='" + inv.site_country + "',site_zip='" + inv.site_zip + "',site_rack='" + inv.site_rack + "',site_notes='" + inv.site_notes + "',poc_1_name='" + inv.poc_1_name + "',poc_1_email='" + inv.poc_1_email + "',poc_1_phone_a='" + inv.poc_1_phone_a + "',poc_1_phone_b='" + inv.poc_1_phone_b + "',poc_1_cell='" + inv.poc_1_cell + "',poc_1_screen='" + inv.poc_1_screen + "',poc_1_notes='" + inv.poc_1_notes + "',poc_2_name='" + inv.poc_2_name + "',poc_2_email='" + inv.poc_2_email + "',poc_2_phone_a='" + inv.poc_2_phone_a + "',poc_2_phone_b='" + inv.poc_2_phone_b + "',poc_2_cell='" + inv.poc_2_cell + "',poc_2_screen='" + inv.poc_2_screen + "',poc_2_notes='" + inv.poc_2_notes  + "' WHERE datacheck.hostid=" + inv.hostid

        cursor.execute(update_query)

    connection.commit()

    cursor.close()
    connection.close()

def check_record_deleted(db_config):
    connection = mysql.connector.connect(
        host=db_config['DB_HOST'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        database=db_config['DB_NAME'],
        port=db_config['DB_PORT']
    )

    cursor = connection.cursor()

    check_query = "SELECT * FROM v_deleted" 
    cursor.execute (check_query)

    result = cursor.fetchall()

    connection.close()

    return result

def check_record_updated(db_config):
    connection = mysql.connector.connect(
        host=db_config['DB_HOST'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        database=db_config['DB_NAME'],
        port=db_config['DB_PORT']
    )

    cursor = connection.cursor()

    check_query = "SELECT * FROM v_differences" 

    cursor.execute (check_query)
    
    result = cursor.fetchall()
    
    connection.close()

    return result

def check_record_inserted(db_config):
    connection = mysql.connector.connect(
        host=db_config['DB_HOST'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        database=db_config['DB_NAME'],
        port=db_config['DB_PORT']
    )

    cursor = connection.cursor()

    check_query = "SELECT * FROM v_inserted" 
    cursor.execute (check_query)

    result = cursor.fetchall()

    connection.close()

    return result

def update_record_updated(db_config):
    connection = mysql.connector.connect(
        host=db_config['DB_HOST'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        database=db_config['DB_NAME'],
        port=db_config['DB_PORT']
    )

    cursor = connection.cursor()

    update_query = "UPDATE alldata SET updated = 1 WHERE hostid IN (SELECT hostid FROM v_differences);" 

    cursor.execute (update_query)

    connection.commit()
    
    connection.close()

def update_record_deleted(db_config):
    connection = mysql.connector.connect(
        host=db_config['DB_HOST'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        database=db_config['DB_NAME'],
        port=db_config['DB_PORT']
    )

    cursor = connection.cursor()

    update_query = "UPDATE alldata SET inserted = 0 WHERE hostid IN (SELECT hostid FROM v_deleted);" 

    cursor.execute (update_query)

    connection.commit()
    
    connection.close()

def update_record_inserted(zabbix_config,db_config):
    connection = mysql.connector.connect(
        host=db_config['DB_HOST'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        database=db_config['DB_NAME'],
        port=db_config['DB_PORT']
    )
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT hostid, host_name, visible_name, description, disabled FROM v_inserted;")
    hosts = [Host(**row) for row in cursor.fetchall()]
    cursor.close()
    connection.close()

    bearer = f"{zabbix_config['ZABBIX_TOKEN']}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + bearer
        }
    api_url = f"{zabbix_config['ZABBIX_URL']}/api_jsonrpc.php"
    
    for host in hosts:
        
        # Creazione della richiesta JSON per la cancellazione dell'host su Zabbix
        payload ={
            "jsonrpc": "2.0",
            "method": "host.delete",
            "params": [
            host.hostid
            ],
            "id": 1
        }
        
        requests.post(api_url, headers=headers, data=json.dumps(payload))

def invia_email_deleted(result, email_config):
    msg = MIMEMultipart()
    msg['From'] = email_config['sender_email']
    msg['To'] = email_config['receiver_email']
    msg['Subject'] = 'Host presenti nel DB di configurazione e non in Zabbix'

    body = "<h2>Host presenti nel DB di configurazione e non in Zabbix:</h2>"

    body += "<br>Gli host elencati sono presenti nel DB di configurazione ma non su Zabbix<br>Potrebbero esser stati cancellati per errore e sono stati inseriti nuovamente<br>Effettuare le modifiche all anagrafica solo sul CMDB e non su Zabbix"
    body += "<table border='1'><tr><th>Hostid</th><th>Host name</th><th>Visible name</th><th>Description</th><th>Status</th><th>Interface Type</th><th>IP</th><th>FQDN</th><th>Use IP</th><th>Port</th><th>Interface Main</th><th>Type</th><th>Type Full</th><th>Name</th><th>Alias</th><th>OS</th><th>OS Full</th><th>OS Short</th><th>Serial A</th><th>Serial B</th><th>Tag</th><th>Asset Tag</th><th>MAC A</th><th>MAC B</th><th>Hardware</th><th>Hardware Full</th><th>Software</th><th>Software Full</th><th>Software App A</th><th>Software App B</th><th>Software App C</th><th>Software App D</th><th>Software App E</th><th>Contact</th><th>Location</th><th>Location Lat</th><th>Location Lon</th><th>Notes</th><th>Chassis</th><th>Model</th><th>HW Arch</th><th>Vendor</th><th>Contact Number</th><th>Installer Name</th><th>Deployement Status</th><th>URL A</th><th>URL B</th><th>URL C</th><th>Host networks</th><th>Host subnet mask</th><th>Host gateway</th><th>OOB IP address</th><th>OOB subnet mask</th><th>OOB router</th><th>Date HW purchased</th><th>Date HW installed</th><th>Date HW maintenance expires</th><th>Date HW decommissioned</th><th>Site address A</th><th>Site address B</th><th>Site address C</th><th>Site city</th><th>Site state province</th><th>Site country</th><th>Site ZIP postal</th><th>Site rack location</th><th>Site notes</th><th>Primary POC name</th><th>Primary POC email</th><th>Primary POC phone A</th><th>Primary POC phone B</th><th>Primary POC cell</th><th>Primary POC screen name</th><th>Primary POC notes</th><th>Secondary POC name</th><th>Secondary POC email</th><th>Secondary POC phone A</th><th>Secondary POC phone B</th><th>Secondary POC cell</th><th>Secondary POC screen name</th><th>Secondary POC notes</th>"
    for row in result:
        body += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td><td>{row[7]}</td><td>{row[8]}</td><td>{row[9]}</td><td>{row[10]}</td><td>{row[11]}</td><td>{row[12]}</td><td>{row[13]}</td><td>{row[14]}</td><td>{row[15]}</td><td>{row[16]}</td><td>{row[17]}</td><td>{row[18]}</td><td>{row[19]}</td><td>{row[20]}</td><td>{row[21]}</td><td>{row[22]}</td><td>{row[23]}</td><td>{row[24]}</td><td>{row[25]}</td><td>{row[26]}</td><td>{row[27]}</td><td>{row[28]}</td><td>{row[29]}</td><td>{row[30]}</td><td>{row[31]}</td><td>{row[32]}</td><td>{row[33]}</td><td>{row[34]}</td><td>{row[35]}</td><td>{row[36]}</td><td>{row[37]}</td><td>{row[38]}</td><td>{row[39]}</td><td>{row[40]}</td><td>{row[41]}</td><td>{row[42]}</td><td>{row[43]}</td><td>{row[44]}</td><td>{row[45]}</td><td>{row[46]}</td><td>{row[47]}</td><td>{row[48]}</td><td>{row[49]}</td><td>{row[50]}</td><td>{row[51]}</td><td>{row[52]}</td><td>{row[53]}</td><td>{row[54]}</td><td>{row[55]}</td><td>{row[56]}</td><td>{row[57]}</td><td>{row[58]}</td><td>{row[59]}</td><td>{row[60]}</td><td>{row[61]}</td><td>{row[62]}</td><td>{row[63]}</td><td>{row[64]}</td><td>{row[65]}</td><td>{row[66]}</td><td>{row[67]}</td><td>{row[68]}</td><td>{row[69]}</td><td>{row[70]}</td><td>{row[71]}</td><td>{row[72]}</td><td>{row[73]}</td><td>{row[74]}</td><td>{row[75]}</td><td>{row[76]}</td><td>{row[77]}</td><td>{row[78]}</td><td>{row[79]}</td><td>{row[80]}</td>"
    body += "</table>"

    msg.attach(MIMEText(body, 'html'))

    with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
        server.starttls()
        server.login(email_config['sender_email'], email_config['sender_password'])
        server.sendmail(email_config['sender_email'], email_config['receiver_email'], msg.as_string())      
        
def invia_email_updated(result, email_config):
    msg = MIMEMultipart()
    msg['From'] = email_config['sender_email']
    msg['To'] = email_config['receiver_email']
    msg['Subject'] = 'Host differenti tra il DB di configurazione e Zabbix'

    body = "<h2>Host differenti tra il DB di configurazione e Zabbix:</h2>"
    body += "<br>I seguenti host presentavano delle modifiche in Zabbix rispetto alla configurazione originale e sono stati riallineati ad essa<br>Effettuare le modifiche all'anagrafica solo sul CMDB e non su Zabbix"
    body += "<table border='1'><tr><th>Hostid</th><th>Host name</th><th>Visible name</th><th>Description</th><th>Status</th><th>Interface Type</th><th>IP</th><th>FQDN</th><th>Use IP</th><th>Port</th><th>Interface Main</th><th>Type</th><th>Type Full</th><th>Name</th><th>Alias</th><th>OS</th><th>OS Full</th><th>OS Short</th><th>Serial A</th><th>Serial B</th><th>Tag</th><th>Asset Tag</th><th>MAC A</th><th>MAC B</th><th>Hardware</th><th>Hardware Full</th><th>Software</th><th>Software Full</th><th>Software App A</th><th>Software App B</th><th>Software App C</th><th>Software App D</th><th>Software App E</th><th>Contact</th><th>Location</th><th>Location Lat</th><th>Location Lon</th><th>Notes</th><th>Chassis</th><th>Model</th><th>HW Arch</th><th>Vendor</th><th>Contact Number</th><th>Installer Name</th><th>Deployement Status</th><th>URL A</th><th>URL B</th><th>URL C</th><th>Host networks</th><th>Host subnet mask</th><th>Host gateway</th><th>OOB IP address</th><th>OOB subnet mask</th><th>OOB router</th><th>Date HW purchased</th><th>Date HW installed</th><th>Date HW maintenance expires</th><th>Date HW decommissioned</th><th>Site address A</th><th>Site address B</th><th>Site address C</th><th>Site city</th><th>Site state province</th><th>Site country</th><th>Site ZIP postal</th><th>Site rack location</th><th>Site notes</th><th>Primary POC name</th><th>Primary POC email</th><th>Primary POC phone A</th><th>Primary POC phone B</th><th>Primary POC cell</th><th>Primary POC screen name</th><th>Primary POC notes</th><th>Secondary POC name</th><th>Secondary POC email</th><th>Secondary POC phone A</th><th>Secondary POC phone B</th><th>Secondary POC cell</th><th>Secondary POC screen name</th><th>Secondary POC notes</th>"
    for row in result:
        body += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td><td>{row[7]}</td><td>{row[8]}</td><td>{row[9]}</td><td>{row[10]}</td><td>{row[11]}</td><td>{row[12]}</td><td>{row[13]}</td><td>{row[14]}</td><td>{row[15]}</td><td>{row[16]}</td><td>{row[17]}</td><td>{row[18]}</td><td>{row[19]}</td><td>{row[20]}</td><td>{row[21]}</td><td>{row[22]}</td><td>{row[23]}</td><td>{row[24]}</td><td>{row[25]}</td><td>{row[26]}</td><td>{row[27]}</td><td>{row[28]}</td><td>{row[29]}</td><td>{row[30]}</td><td>{row[31]}</td><td>{row[32]}</td><td>{row[33]}</td><td>{row[34]}</td><td>{row[35]}</td><td>{row[36]}</td><td>{row[37]}</td><td>{row[38]}</td><td>{row[39]}</td><td>{row[40]}</td><td>{row[41]}</td><td>{row[42]}</td><td>{row[43]}</td><td>{row[44]}</td><td>{row[45]}</td><td>{row[46]}</td><td>{row[47]}</td><td>{row[48]}</td><td>{row[49]}</td><td>{row[50]}</td><td>{row[51]}</td><td>{row[52]}</td><td>{row[53]}</td><td>{row[54]}</td><td>{row[55]}</td><td>{row[56]}</td><td>{row[57]}</td><td>{row[58]}</td><td>{row[59]}</td><td>{row[60]}</td><td>{row[61]}</td><td>{row[62]}</td><td>{row[63]}</td><td>{row[64]}</td><td>{row[65]}</td><td>{row[66]}</td><td>{row[67]}</td><td>{row[68]}</td><td>{row[69]}</td><td>{row[70]}</td><td>{row[71]}</td><td>{row[72]}</td><td>{row[73]}</td><td>{row[74]}</td><td>{row[75]}</td><td>{row[76]}</td><td>{row[77]}</td><td>{row[78]}</td><td>{row[79]}</td><td>{row[80]}</td>"
    body += "</table>"

    msg.attach(MIMEText(body, 'html'))

    with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
        server.starttls()
        server.login(email_config['sender_email'], email_config['sender_password'])
        server.sendmail(email_config['sender_email'], email_config['receiver_email'], msg.as_string())        

def invia_email_inserted(result, email_config):
    msg = MIMEMultipart()
    msg['From'] = email_config['sender_email']
    msg['To'] = email_config['receiver_email']
    msg['Subject'] = 'Host presenti in Zabbix e non nel DB di configurazione'

    body = "<h2>Host presenti in Zabbix e non nel DB di configurazione:</h2>"

    body += "<br>Gli host elencati sono presenti su Zabbix ma non nel DB di configurazione.<br> Potrebbero esser stati inseriti per errore e saranno quindi rimossi"
    body += "<table border='1'><tr><th>Hostid</th><th>Host name</th><th>Visible name</th><th>Description</th><th>Status</th><th>Interface Type</th><th>IP</th><th>FQDN</th><th>Use IP</th><th>Port</th><th>Interface Main</th><th>Type</th><th>Type Full</th><th>Name</th><th>Alias</th><th>OS</th><th>OS Full</th><th>OS Short</th><th>Serial A</th><th>Serial B</th><th>Tag</th><th>Asset Tag</th><th>MAC A</th><th>MAC B</th><th>Hardware</th><th>Hardware Full</th><th>Software</th><th>Software Full</th><th>Software App A</th><th>Software App B</th><th>Software App C</th><th>Software App D</th><th>Software App E</th><th>Contact</th><th>Location</th><th>Location Lat</th><th>Location Lon</th><th>Notes</th><th>Chassis</th><th>Model</th><th>HW Arch</th><th>Vendor</th><th>Contact Number</th><th>Installer Name</th><th>Deployement Status</th><th>URL A</th><th>URL B</th><th>URL C</th><th>Host networks</th><th>Host subnet mask</th><th>Host gateway</th><th>OOB IP address</th><th>OOB subnet mask</th><th>OOB router</th><th>Date HW purchased</th><th>Date HW installed</th><th>Date HW maintenance expires</th><th>Date HW decommissioned</th><th>Site address A</th><th>Site address B</th><th>Site address C</th><th>Site city</th><th>Site state province</th><th>Site country</th><th>Site ZIP postal</th><th>Site rack location</th><th>Site notes</th><th>Primary POC name</th><th>Primary POC email</th><th>Primary POC phone A</th><th>Primary POC phone B</th><th>Primary POC cell</th><th>Primary POC screen name</th><th>Primary POC notes</th><th>Secondary POC name</th><th>Secondary POC email</th><th>Secondary POC phone A</th><th>Secondary POC phone B</th><th>Secondary POC cell</th><th>Secondary POC screen name</th><th>Secondary POC notes</th>"
    for row in result:
        body += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td><td>{row[7]}</td><td>{row[8]}</td><td>{row[9]}</td><td>{row[10]}</td><td>{row[11]}</td><td>{row[12]}</td><td>{row[13]}</td><td>{row[14]}</td><td>{row[15]}</td><td>{row[16]}</td><td>{row[17]}</td><td>{row[18]}</td><td>{row[19]}</td><td>{row[20]}</td><td>{row[21]}</td><td>{row[22]}</td><td>{row[23]}</td><td>{row[24]}</td><td>{row[25]}</td><td>{row[26]}</td><td>{row[27]}</td><td>{row[28]}</td><td>{row[29]}</td><td>{row[30]}</td><td>{row[31]}</td><td>{row[32]}</td><td>{row[33]}</td><td>{row[34]}</td><td>{row[35]}</td><td>{row[36]}</td><td>{row[37]}</td><td>{row[38]}</td><td>{row[39]}</td><td>{row[40]}</td><td>{row[41]}</td><td>{row[42]}</td><td>{row[43]}</td><td>{row[44]}</td><td>{row[45]}</td><td>{row[46]}</td><td>{row[47]}</td><td>{row[48]}</td><td>{row[49]}</td><td>{row[50]}</td><td>{row[51]}</td><td>{row[52]}</td><td>{row[53]}</td><td>{row[54]}</td><td>{row[55]}</td><td>{row[56]}</td><td>{row[57]}</td><td>{row[58]}</td><td>{row[59]}</td><td>{row[60]}</td><td>{row[61]}</td><td>{row[62]}</td><td>{row[63]}</td><td>{row[64]}</td><td>{row[65]}</td><td>{row[66]}</td><td>{row[67]}</td><td>{row[68]}</td><td>{row[69]}</td><td>{row[70]}</td><td>{row[71]}</td><td>{row[72]}</td><td>{row[73]}</td><td>{row[74]}</td><td>{row[75]}</td><td>{row[76]}</td><td>{row[77]}</td><td>{row[78]}</td><td>{row[79]}</td><td>{row[80]}</td>"
    body += "</table>"

    msg.attach(MIMEText(body, 'html'))

    with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
        server.starttls()
        server.login(email_config['sender_email'], email_config['sender_password'])
        server.sendmail(email_config['sender_email'], email_config['receiver_email'], msg.as_string())      
 
def main(scelta):
    db_config, zabbix_config, email_config = load_config()

    ## Inizio popolamento tabella datacheck ##
    
    # Ottieni gli host da Zabbix
    zabbix_hosts = get_hosts_from_zabbix(zabbix_config)

    # Inserisci gli host nel database MariaDB
    insert_hosts_into_database(db_config, zabbix_hosts)

    # Ottieni le interfaces da Zabbix
    zabbix_if = get_if_from_zabbix(zabbix_config)

    # Inserisci le interfacce nel database MariaDB
    insert_if_into_database(db_config, zabbix_if)

    # Ottieni l inventario da Zabbix
    zabbix_inv = get_inv_from_zabbix(zabbix_config)

    # Inserisci l inventario nel database MariaDB
    insert_inv_into_database(db_config, zabbix_inv)
    
    ## Fine popolamento tabella datacheck ##

    if scelta == 1:
    
    # Query che controlla i record presenti nel DB e non in Zabbix (cancellazione errata)
        risultati = check_record_deleted(db_config)
        
        if risultati:
            invia_email_deleted(risultati, email_config)
            update_record_deleted(db_config)
            print("Email inviata con successo.")
        else:
            print("Nessun risultato da inviare.")

    elif scelta == 2:
    
    # Query che controlla i record diversi tra una tabella e l'altra (modifica errata)
        risultati2 = check_record_updated(db_config)

        if risultati2:
            invia_email_updated(risultati2, email_config)
            update_record_updated(db_config)
            print("Email inviata con successo.")
        else:
            print("Nessun risultato da inviare.")

    elif scelta == 3:
    
    # Query che controlla i record presenti in Zabbix e non nel DB (inserimento errato)
        risultati3 = check_record_inserted(db_config)

        if risultati3:
            invia_email_inserted(risultati3, email_config)
            update_record_inserted(zabbix_config,db_config)
            print("Email inviata con successo.")
        else:
            print("Nessun risultato da inviare.")            
    else:
        print("Scelta non valida")
    
if __name__ == "__main__":
    # Verifica che sia stato passato almeno un argomento da riga di comando
    if len(sys.argv) != 2:
        print("Usage: python script.py <scelta>")
        sys.exit(1)

    # Leggi la scelta dalla riga di comando
    scelta = int(sys.argv[1])

    # Esegui la funzione corrispondente
    main(scelta)
