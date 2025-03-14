import requests

def usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()["results"][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"Nome: {nome}\nEmail: {email}\nPaís: {pais}"
    except requests.RequestException as e:
        return f"Erro {e}"
def main():
    print("Criando usuario")
    usuario = usuario_aleatorio()
    print(usuario)
if __name__ == "__main__":
   main()
