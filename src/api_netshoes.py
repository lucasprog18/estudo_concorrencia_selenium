# Mesmo sem o acesso total à API (ainda), achei interessante começar a estruturar a lógica desde já
import requests
import openpyxl

# Configuração da API (caso seja necessário autenticação)
BASE_URL = "https://api.netshoes.com.br/v1/produtos"
API_KEY = "SUA_CHAVE_AQUI"  # Caso precise autenticação

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def buscar_produtos(termo_busca):
    """Realiza requisição para buscar produtos na API da Netshoes."""
    params = {"query": termo_busca}
    response = requests.get(BASE_URL, headers=HEADERS, params=params)

    if response.status_code == 200:
        return response.json()  # Retorna os dados como dicionário
    else:
        print(f"❌ Erro na API: {response.status_code}")
        return None

def salvar_em_excel(produtos):
    """Salva os produtos encontrados em um arquivo Excel."""
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Produtos Netshoes"
    sheet.append(["Nome", "Preço"])

    for produto in produtos:
        sheet.append([produto["nome"], produto["preco"]])

    workbook.save("api_netshoes.xlsx")
    print("\n✅ Dados salvos em 'api_netshoes.xlsx'!")

# Exemplo de uso (ainda não funcional sem chave de API)
produtos = buscar_produtos("tênis nike")
if produtos:
    salvar_em_excel(produtos)
