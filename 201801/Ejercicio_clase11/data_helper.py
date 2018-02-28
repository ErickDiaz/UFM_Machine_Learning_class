import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model

def predict_price(data_casas):
	data_casas['y_modelo_1'] =  data_casas.apply(lambda row: (2.41262565*row.Area_Lote) + 107748.55024667, axis=1)
	data_casas['y_modelo_2'] =  data_casas.apply(lambda row: (1.5322*row.Area_Lote) + 10790.55, axis=1)
	data_casas['y_modelo_3'] =  data_casas.apply(lambda row: (3.12*row.Area_Lote) + 100750, axis=1)

	return data_casas