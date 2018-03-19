import pandas as pd

def load_data():
	data_casas = pd.read_csv('housing_data.csv')

	#renombramos las columnas
	data_casas = data_casas.rename(index = str, columns = {'BuildingArea' : 'Area_Lote', \
														   'Price' : 'Precio', \
														   'Rooms' : 'dormitorios', \
														   'Bathroom' : 'banios',
														   'Car' : 'paqueos',
														   'SellerG' : 'Vendedor',
														   'YearBuilt': 'anio_construccion'})

	#filtramos las columnas
	data_casas = data_casas[['Area_Lote', 'Precio', 'dormitorios', 'banios', 'paqueos', 'anio_construccion', 'Vendedor']]

	#eliminamos los valores nulos
	data_casas = data_casas.dropna()

	data_casas['banios'] = data_casas.banios.astype(int)
	data_casas['paqueos'] = data_casas.paqueos.astype(int)
	data_casas['anio_construccion'] = data_casas.anio_construccion.astype(int)

	data_casas = data_casas[:1000]

	return data_casas
