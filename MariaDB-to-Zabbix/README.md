# MariaDB to Zabbix



## Getting started


Parte di codice che, partendo dal contenuto del DB gestisce gli host su Zabbix.

Tutti e tre gli script scrivono un log delle operazioni fatte.
L'insert gestisce i duplicati tramite un campo apposito nel DB che viene letto prima dell'inserimento e eventualmente aggiornato dopo.
Il delete cancella l'host su Zabbix e la corrispondente riga nel DB
L'update sovrascrive tutti i campi con quelli che trova nel DB

I tre script vanno fatti girare con cron (tipicamente ogni 15 minuti) e scalati di un minuto l'uno dall'altro. In futuro queste operazioni potrebbero essere gestite tramite RabbitMQ in modo da diventare istantanee

Gli script richiedono i seguenti moduli python: mysql.connector configparser json requests logging datetime
