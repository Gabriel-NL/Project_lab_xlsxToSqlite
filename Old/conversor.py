
# Importação de bibliotecas
from sqlalchemy import create_engine
# Leitura da tabela "Sheet1"

def analisar_dados(data_origin,nome_municipio_selecionado, ano_selecionado, tipo_produto_selecionado):

  # Selecionar as linhas com os valores específicos
  linhas_filtradas = data_origin.query('Nome_Municipio == @nome_municipio_selecionado and Ano == @ano_selecionado and Produto_Tipo == @tipo_produto_selecionado')

  # Criar lista para armazenar os resultados
  lista_resultados = []

  # Imprimir os valores das colunas "produto_variavel" e "valor"
  for i in range(linhas_filtradas.shape[0]):
    produto_variavel = linhas_filtradas['Produto_Variavel'].iloc[i]
    valor = linhas_filtradas['Valor'].iloc[i]

    # Adicionar os valores à lista
    lista_resultados.append((produto_variavel, valor))

  return lista_resultados

def coletarEntradasUnicas(data_origin):

  # Criar conjunto vazio para armazenar combinações únicas
  combinacoes_unicas = set()

  # Iterar sobre as linhas do DataFrame
  for i in range(data_origin.shape[0]):
    # Obter valores de "ano" e "produto_tipo" da linha atual
    nome_municipio = data_origin['Nome_Municipio'].iloc[i]
    ano = data_origin['Ano'].iloc[i]
    produto_tipo = data_origin['Produto_Tipo'].iloc[i]

    # Criar tupla com os valores
    combinacao = (nome_municipio,produto_tipo,ano )

    # Se a combinação não estiver no conjunto, adicionar
    if combinacao not in combinacoes_unicas:
      combinacoes_unicas.add(combinacao)

  # Converter conjunto em lista e ordenar
  lista_unica = list(combinacoes_unicas)
  # Converter conjunto em lista e retornar
  #return list(combinacoes_unicas)[:20]
  return lista_unica

