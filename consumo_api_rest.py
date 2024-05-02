# exemplo de consumo de api rest do Movidesk

import requests
import pandas as pd
from datetime import datetime

def get_tickets(api_token, start_date, end_date):
    """
    Função para obter tickets da API Movidesk e salvar como um arquivo Excel.

    Args:
        api_token (str): Token de autenticação para a API da Movidesk.
        start_date (datetime): Data de início para filtrar a abertura dos tickets.
        end_date (datetime): Data de fim para filtrar a abertura dos tickets.

    Returns:
        str: Caminho do arquivo Excel criado ou uma mensagem de erro.
    """
    # URL base para a API de tickets
    url = "https://api.movidesk.com/public/v1/tickets"

    # Cabeçalhos para a requisição
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Formata as datas para o formato correto 'yyyy-MM-dd'
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    # Parâmetros de consulta, incluindo filtro de data
    params = {
        'token': api_token,
        '$filter': f"createdDate ge {start_date_str} and createdDate le {end_date_str}",
        'format': 'json'
    }

    # Executando a requisição GET
    response = requests.get(url, headers=headers, params=params)

    # Checando se a requisição foi bem sucedida
    if response.status_code == 200:
        tickets = response.json()
        # Cria um DataFrame a partir dos dados
        df = pd.DataFrame(tickets)
        # Define o nome do arquivo com a data e hora atual para evitar sobreposições
        file_name = f"tickets_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"
        # Salva o DataFrame em um arquivo Excel
        df.to_excel(file_name, index=False)
        return file_name  # Retorna o caminho do arquivo
    else:
        return f"Erro ao buscar tickets: {response.status_code} - {response.text}"

# Exemplo de uso da função
api_token = "seu_token"  # Substitua 'seu_token' pelo seu token de autenticação real
start_date = datetime(2024, 1, 1)  # Data de início do filtro
end_date = datetime(2024, 4, 30)   # Data de fim do filtro

file_path = get_tickets(api_token, start_date, end_date)
print(f"Arquivo gerado: {file_path}")
