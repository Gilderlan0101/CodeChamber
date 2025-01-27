# utf-8
import re

IMPROPER_KEYWORDS = [
    "adult", "porn", "xxx", "18+", "nsfw", "sex", "erotica", "xvideos",
    "localhost", " torrent",  "Bit.ly", " pornografia", " vazados", "pornographic",
]

def ValidatesLinks(github, linkedin, site):
    """
    Valida os links fornecidos (GitHub, LinkedIn e site pessoal) com base em regex.
    Retorna um dicionário indicando quais links são válidos.
    """

    github_regex = r"^https:\/\/(www\.)?github\.com\/[\w-]+(\/[\w-]+)?\/?$"
    linkedin_regex =  r"^https:\/\/(www\.)?linkedin\.com\/[\w-]+(\/[\w-]+)?\/?$"
    site_regex = r"^(https?:\/\/)?(www\.)?[\w\-]+\.[a-z]{2,}(\.[a-z]{2,})?(\/[\w\-]*)*\/?$"

    for text_in_link in IMPROPER_KEYWORDS:
        if text_in_link in github or text_in_link in linkedin or text_in_link in site:
            return {"github_valid": False, "linkedin_valid": False, "site_valid": False}

        
        

    results = {
        "github_valid": re.match(github_regex, github) is not None ,
        "linkedin_valid": re.match(linkedin_regex, linkedin) is not None,
        "site_regex": re.match(site_regex, site) is not None
    }

    return results

