import pandas as pd
import numpy as np

carsa = pd.read_csv('TEST_ENVIO.txt', index_col = 0, sep='|', encoding='utf-8')
carsb = pd.read_csv('TEST_PLANTAPOST.txt', index_col = 1, sep='|', encoding='utf-8')
carsc = pd.read_csv('TEST_FUENTE_VOZ.txt', index_col = 1, sep='|', encoding='utf-8')
#carsd = pd.read_csv('TRAIN_FUENTE_DATOS.txt', index_col = 1, sep='|', encoding='utf-8')
#carse = pd.read_csv('TRAIN_FUENTE_APLICACIONES.txt', index_col = 1, sep='|', encoding='utf-8')
#carsf = pd.read_csv('TRAIN_FUENTE_EQUIPOS.txt', index_col = 1, sep='|', encoding='utf-8')
#carsg = pd.read_csv('TRAIN_FUENTE_CONSULTA_PREV_PORTA.txt', index_col = 1, sep='|', encoding='utf-8')


pf1 = pd.merge(carsa,carsb[['ANTIGUEDAD_LINEA', 'ANTIGUEDAD_POSTPAGO','EDAD']],
         on='ID_CLIENTE')
pf2 = pf1.groupby('ID_CLIENTE').mean()

pf3 = pd.merge(pf2[['ANTIGUEDAD_LINEA', 'ANTIGUEDAD_POSTPAGO','EDAD']],carsc[['CALLS_IN_OFF','CALLS_OUT_OFF','DEST_VOICE_OFF']],
         on='ID_CLIENTE')
pf4 = pf3.groupby('ID_CLIENTE').mean()

print(pf4)
pf4.to_csv('TEST_CRUCE_TODO_V1.csv')
