import conversor as lib
import pandas as pd

def multiple(data_origin,data_format,data_destination):
    print("Tabelas carregadas! \n Extraindo dados...")
    # Executar a função
    lista_chaves = lib.coletarEntradasUnicas(data_origin.copy())
    lista_chaves = sorted(lista_chaves)
    
    iteration=1
    for n_mun,t_prod,ano in lista_chaves:
        lista_dados = lib.analisar_dados(data_origin.copy(),n_mun, ano, t_prod)
        data_format.loc[iteration,'Nome_Municipio']=n_mun
        data_format.loc[iteration,'Ano']=ano
        data_format.loc[iteration,'Produto_Tipo']=t_prod 
        for prod,val in lista_dados:
            data_format.loc[iteration,prod]=val
        progress_percentage = (iteration) / len(lista_chaves) * 100
        print(f"\rProcessing line {iteration}/{len(lista_chaves)} - Progress: {progress_percentage:.2f}%", end="", flush=True)
        iteration+=1
        #print(iteration)
    print("Dados extraidos! \n Salvando...")
    data_format.to_excel(data_destination)
    print("Processo concluido!")

if __name__ == "__main__":
    print("Iniciando o processo de conversão. \n Isto vai demorar um pouco")
    
    print("Carregando tabelas...")
    data_origin = pd.read_excel(r'Tables/Produção extrativa vegetal por município (Original).xlsx', sheet_name="Produção extrativa vegetal")
    data_format = pd.read_excel(r'Formato.xlsx', sheet_name="Produção extrativa vegetal") 
    data_destination = "Produção extrativa vegetal.xlsx"
    print(data_destination)
    multiple(data_origin,data_format,data_destination)
    


