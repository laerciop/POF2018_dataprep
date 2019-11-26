import pandas as pd
import xlrd
import zipfile
import ftplib
import shutil
import os

def POFPrep(s_name):
    base = 'MORADOR.txt'
    dicio = pd.read_excel('temp/Documentos/Dicion†rios de v†riaveis.xls', sheet_name='Morador', skiprows=3, header=0)
    dicio.drop(labels='Categorias', axis=1, inplace=True)
    dicio.dropna(axis=0, how='all', inplace=True)
    col_size = list(dicio.loc[:, 'Tamanho'])
    col_size = [int(i) for i in col_size]
    col_names = list(dicio.loc[:, 'Código da variável'])
    pof_data = pd.read_fwf('/Users/laerciop/Desktop/ds/ibge/POF/2018/Dados/'+base, widths=col_size)
    pof_data.columns = col_names
    csv = pof_data.to_csv('Morador.csv', index=False)
    print("File saved as")


def FtpIbgeRetrieve(filename):
    path = 'Orcamentos_Familiares/Pesquisa_de_Orcamentos_Familiares_2017_2018/Microdados/'
    ftp = ftplib.FTP("ftp.ibge.gov.br")
    ftp.login("guest", "guest") 
    ftp.cwd(path)
    ftp.retrbinary("RETR "+filename, open(filename, 'wb').write)
    ftp.quit()

def IBGEUnzipper(filename):
    zipfile = zipfile.ZipFile(filename)
    zipfile.extractall(path='temp/')
    zipfile.close()

def IBGESold():
    shutil.rmtree('temp', ignore_errors=True)
    for f in filename:
        os.remover(f)


filename = ['Dados.zip', 'Documentacao.zip']

s_name = 'SURVEY_NAME'

for f in filename:
    FtpIbgeRetrieve(f)
    IBGEUnzipper(f)

POFPrep(s_name)
IBGESold()