import pandas as pd

def load_data():
	data_casas = pd.read_csv('housing_data.csv')

	#Filtramos las columnas para tener una sola variable
	data_casas = data_casas[['LotArea', 'SalePrice']]
	data_casas = data_casas.rename(index = str, columns = {'LotArea' : 'Area_Lote', 'SalePrice' : 'Precio'})

	data_casas1 = data_casas[(data_casas.Area_Lote <= 5000) \
                        & (data_casas.Precio >= 100000) & (data_casas.Precio <= 120000) ] 

	data_casas2 = data_casas[(data_casas.Area_Lote > 5000) & (data_casas.Area_Lote <= 8000) \
	                        & (data_casas.Precio >= 110000) &(data_casas.Precio <= 130000) ] 

	data_casas3 = data_casas[(data_casas.Area_Lote > 8000) & (data_casas.Area_Lote <= 10000) \
	                        & (data_casas.Precio >= 120000) &(data_casas.Precio <= 140000) ] 

	data_casas4 = data_casas[(data_casas.Area_Lote > 10000) & (data_casas.Area_Lote <= 20000) \
	                        & (data_casas.Precio >= 120000) &(data_casas.Precio <= 150000) ] 

	return pd.concat([data_casas1, data_casas2, data_casas3, data_casas4])
