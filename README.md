# POF2018_dataprep

### About IBGE's Pesquisa de Orçamentos Familiares (POF)

IBGE is the brazilian intitute for geography and socialeconomic statistics. It is a governmental instituition that conduct public interest surveys on geography, economics and population.

POF (initial for Family Spending Survey) is a research made every 10 years on household spending. The detailed documentation can be found in this link (in portuguese): https://www.ibge.gov.br/estatisticas/sociais/educacao/9050-pesquisa-de-orcamentos-familiares.html?=&t=o-que-e

### Microdados - Raw data

In this project we focusing on what is called "microdados", which is the raw data (the registers of every applied questionaire). IBGE provides this raw data for the community but it have some steps on preparation; this projetct aims to build a seamless Python data prep pipe for microdados.

#### POF2018_dataprep

POF2018_dataprep is a python script that downloads POF files and build the tables. To use it is very simple:

1) Download the python script;
2) Install the libraries (requirements bellow);
3) Run in the command line:

		python POF2018_dataprep [survey name]
		
	Where the survey name should be:
		aluguel: Aluguel Estimado (estimated rent)
		caderneta: Caderneta Coletiva (household annotations)
  	d_coletiva: Despesa Coletiva (household expenses)
  	d_individual: Despesa Individual (indicidual expenses)
  	morador: Dados Morador (residents data)
  	outros_r: Outros Rendimentos (another revenue source)
  	rendimento_t: Rendimento do Trabalho (work revenue)
	
	
#### Requirements

Python 3.7 basic libraries with the following installed packages:

Package           Version
----------------- -------
pandas            0.25.3
xlrd              1.2.0
