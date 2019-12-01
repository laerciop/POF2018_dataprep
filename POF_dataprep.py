import pandas as pd
import xlrd
import zipfile
import ftplib
import shutil
import os
import sys

def POFPrep(s_name):
    s_dict = {'aluguel':['ALUGUEL_ESTIMADO.txt', 'Aluguel Estimado'],
         'caderneta':['CADERNETA_COLETIVA.txt', 'Caderneta Coletiva'],
         'd_coletiva':['DESPESA_COLETIVA.txt', 'Despesa Coletiva'],
         'd_individual':['DESPESA_INDIVIDUAL', 'Despesa Individual'],
         'morador':['MORADOR.txt', 'Morador'],
         'outros_r':['OUTROS_RENDIMENTOS.txt', 'Outros Rendimentos'],
         'rendimento_t':['RENDIMENTO_TRABALHO.txt', 'Rendimento do Trabalho']}
    dicio = pd.read_excel('temp/Documentos/Dicionários de váriaveis.xls', sheet_name=s_dict[s_name][1], skiprows=3, header=0)
    dicio.drop(labels='Categorias', axis=1, inplace=True)
    dicio.dropna(axis=0, how='all', inplace=True)
    col_size = list(dicio.loc[:, 'Tamanho'])
    col_size = [int(i) for i in col_size]
    col_names = list(dicio.loc[:, 'Código da variável'])
    pof_data = pd.read_fwf('/Users/laerciop/Desktop/ds/ibge/POF/2018/Dados/'+s_dict[s_name][0], widths=col_size)
    pof_data.columns = col_names
    pof_data.to_csv(s_dict[s_name][1]+'.csv', index=False)
    print("Done! File saved as "+s_dict[s_name][1]+'.csv')


def FtpIbgeRetrieve(filename):
    path = 'Orcamentos_Familiares/Pesquisa_de_Orcamentos_Familiares_2017_2018/Microdados/'
    try:
        ftp = ftplib.FTP("ftp.ibge.gov.br")
        ftp.login("anonymous", "anonymous")
    except:
        print("Couldn't connect. Check your connection and ftp.ibge.gov.br availability.")
    ftp.cwd(path)
    print("Starting Download of "+filename+"...")
    ftp.retrbinary("RETR "+filename, open(filename, 'wb').write)
    print("Done! Now unzipping...")
    ftp.quit()

def IBGEUnzipper(file):
    zfile = zipfile.ZipFile(file)
    zfile.extractall(path='temp/')
    print("Done!")
    zfile.close()

def IBGESold():
    shutil.rmtree('temp', ignore_errors=True)
    for f in filename:
        os.remove(f)

filename = ['Dados.zip', 'Documentacao.zip']

s_name = sys.argv[1]

print("Tryng to connect to IBGE server...")
for f in filename:
    FtpIbgeRetrieve(f)
    IBGEUnzipper(f)

print("Preparing data file...")
POFPrep(s_name)
IBGESold()