# Import pandas and cars.csv
import pandas as pd
import numpy as np
app = pd.read_csv('TRAIN_FUENTE_DATOS.txt', index_col = 0)

#print(app.iloc[0])
grupo1 = app.groupby(["PERIODO","ID_CLIENTE"]).mean()
#data.groupby(PERIODO,ID_CLIENTE).mean()
print(grupo1.count())

#dt2 = app.groupby('SEG')

# Print out country column as Pandas Series
##print(app.count())
##total_rows = app['ID_CLIENTE'].count

# Print out country column as Pandas DataFrame
##app.set_index(["ID_CLIENTE"]).count()

##df[['col1', 'col2', 'col3', 'col4']].groupby(['col1', 'col2']).agg(['mean', 'count'])
