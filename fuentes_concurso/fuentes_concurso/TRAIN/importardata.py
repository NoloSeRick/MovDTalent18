#!/usr/bin/python
import mysql.connector
import csv
import argparse
import mysql.connector as mariadb
import uuid


# input parameter handling
DEFAULT_INSTANCE = '57'
INSTANCES = ['51', '55', '56', '57']
PORTS = ['5173', '5539', '5620', '5704','3306']
ENGINES = ['InnoDB', 'MyISAM']
DEFAULT_ENGINE = 'InnoDB'
HOST = '127.0.0.1'
USER = 'root'
port = '3306'
PASSWORD = ''
DATABASE = 'db_talent'
TABLE_DEFINITION = (


)
CSV_FILE = 'TRAIN_TARGET.txt'

parser = argparse.ArgumentParser(description='Creates and imports the nodes table.')
parser.add_argument('--engine', choices=ENGINES, default=DEFAULT_ENGINE,
                    help='Chosen engine (default: ' + DEFAULT_ENGINE + ')')
parser.add_argument('--instance', choices=INSTANCES, default=DEFAULT_INSTANCE,
                    help='Instance version (default: ' + DEFAULT_INSTANCE + ')')
options = parser.parse_args()
# port = PORTS[INSTANCES.index(options.instance)]

# database connection
# mariadb_connection = mariadb.connect(user='root', password='',host='127.0.0.1',database='db_talent')   output1tab.csv
# cursor = mariadb_connection.cursor()

db = mariadb.connect(user='root', password='',host='127.0.0.1',database='db_talent')
cursor = db.cursor()


#direccion_csv_file="SELECT direccion from zdata WHERE idz=(SELECT MAX(idz)  FROM zdata)"
#cursor.execute(direccion_csv_file)
#direccion=cursor.fetchall()


#CSV_FILE = 'archivobase/output1tab.csv'
#CSV_FILE = 'D:/xampp/htdocs/bancoripleyweb/app/storage/app/archivoscsv/2018/04/24/10/output1tabv2.csv'
#CSV_FILE = 'D:\xampp\htdocs\bancoripleyweb\app/storage/app/archivoscsv/2018/04/24/11/output1tabv2.csv'
#CSV_FILE = direccion[0][0]




# Obtener el nombre de tabla de base de datos
# create_table = TABLE_DEFINITION + ' ENGINE=' + options.engine
#obtener_nombreTabla="SELECT nombreTabla from zdata WHERE idz=(SELECT MAX(idz)  FROM zdata)"
#cursor.execute(obtener_nombreTabla)
#nametable=cursor.fetchall()

# data import descomentar

load_data = "LOAD DATA INFILE '" + CSV_FILE + "' INTO TABLE TRAIN_TARGET FIELDS TERMINATED BY '|' IGNORE 1 LINES"
cursor.execute(load_data)

#load_data = "DELETE FROM "+nametable[0][0]+" LIMIT 1"
#cursor.execute(load_data)

# finishing
if (options.engine == 'MyISAM'):
    cursor.execute('FLUSH TABLES')
else:
    db.commit()

cursor.close()
db.close()
