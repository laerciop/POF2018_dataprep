import pandas as pd
import xlrd

def POF_prep(s_name):
    dicio = pd.read_excel('/Users/laerciop/Desktop/ds/ibge/POF/2018/Documentos/dicionario.xls', sheet_name='Morador', skiprows=3, header=0)
    dicio.drop(labels='Categorias', axis=1, inplace=True)
    dicio.dropna(axis=0, how='all', inplace=True)
    col_size = list(dicio.loc[:, 'Tamanho'])
    col_size = [int(i) for i in col_size]
    col_names = list(dicio.loc[:, 'Código da variável'])
    pof_data = pd.read_fwf('/Users/laerciop/Desktop/ds/ibge/POF/2018/Dados/MORADOR.txt', widths=col_size)
    pof_data.columns = col_names
    csv = pof_data.to_csv('Morador.csv', index=False)
    print("File saved as")