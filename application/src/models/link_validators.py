# utf-8
import re
import urllib.parse

# Lista de palavras impróprias
IMPROPER_KEYWORDS = [
    "adult",
    "porn",
    "xxx",
    "18+",
    "nsfw",
    "sex",
    "erotica",
    "xvideos",
]


def is_valid_link(url):
    github_regex = r"^https:\/\/(www\.)?github\.com\/[\w-]+(\/[\w-]+)?\/?$"
    return re.match(github_regex, url) is not None


def is_linkedin_link(url):
    linkedin_regex = r"^https:\/\/(www\.)?linkedin\.com\/[\w-]+(\/[\w-]+)?\/?$"
    return re.match(linkedin_regex, url) is not None


def personal_link(url):
    """
    Valida o link enviado pelo usuário:
    - Bloqueia links com palavras impróprias.
    - Verifica se é uma URL válida.
    """
    if not url:
        return False  # URL vazia não é válida

    # Verificar se a URL contém palavras impróprias
    for word in IMPROPER_KEYWORDS:
        if word in url.lower():
            return False

    # Verificar se a URL tem um formato válido
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.scheme and parsed_url.netloc
