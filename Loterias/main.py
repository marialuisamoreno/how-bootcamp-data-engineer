import requests
import pandas as pd

url = ''
r = requests.get(url)

# Retorno da URL
r_text = r.text

# Criar meu dataframe
df = pd.read_html(r_text)

# Verificar se realmente criou um dataframe
type(df)
type(df[0])

# Tornando a lista em dataframe
df = df[0].copy()

# Números da população
nr_pop = list(range(1, 25)) 
nr_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24] 
nr_impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25] 
nr_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]

# Todas as combinações que poderemos ter
comb = [] 
var = []

lst_campos = ['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 
'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 
'Bola13', 'Bola14', 'Bola15']