import os

import requests
from dotenv import load_dotenv

from application.src.services.api_service import fetch_api_data

# Carregar as variáveis de ambiente
load_dotenv()


teste = fetch_api_data()


def get_exact_count():
    post_count = 0
    var = fetch_api_data()
    # Iterar sobre as chaves e valores do dicionário
    for key in var:
        post_count += 1  # Incrementar o contador se necessário

        continue

    return post_count


get_exact_count()


def get_top_stories(
    num_noticias,
):  # Define dinamicamente a quantidade de notícia
    api_url = os.getenv("API_NOTICIA")  #  API
    response = requests.get(api_url)

    if not api_url:
        print(
            "⚠️ Por favor, configure a chave da API de notícias! Acesse https://developer.nytimes.com/ para obter sua chave."
        )

    if response.status_code == 200:
        news_data = response.json()

        # Pega os resultados da API
        if "results" in news_data:
            articles = news_data["results"][
                :num_noticias
            ]  # Limita o número de notícias conforme num_noticias
            conteudos = []

            for article in articles:
                title = article["title"]
                url = article["url"]
                summary = article.get("abstract", "Sem resumo disponível.")

                # Tenta pegar a imagem
                image_url = None
                if (
                    "multimedia" in article
                    and article["multimedia"] is not None
                ):
                    for multimedia in article["multimedia"]:
                        if (
                            multimedia.get("format") == "Super Jumbo"
                        ):  # Usando .get() para evitar KeyError
                            image_url = multimedia["url"]
                            break

                conteudos.append({
                    "titulo": title,
                    "url": url,
                    "resumo": summary,
                    "imagem": image_url,
                })

            return conteudos  # Retorna a lista de notícias

        else:
            print("Erro: Nenhum resultado encontrado na resposta da API.")
            return []
    else:
        print(f"Erro na API: {response.status_code}")
        return []
