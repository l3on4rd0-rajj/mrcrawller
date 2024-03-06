from googlesearch import search
import random
import time
import datetime
from termcolor import colored
from bs4 import BeautifulSoup
from utils.file_operations import fetch_queries_from_file
from config.user_agents import generate_random_user_agent
from utils.logging import generate_log
from utils.search_results import get_search_results


def search_for_queries(queries, domain, user, search_mode, tor_process):
    for query in queries:
        full_query = f"{domain} {query}"
        print(f"Realizando busca por: {full_query}")

        try:
            user_agent = generate_random_user_agent()
            results = get_search_results(full_query, user_agent)
            result_count = len(results)

            if results:
                print(colored("Resultados encontrados:", 'green'))
                for idx, result in enumerate(results, 1):
                    print(f"[+] {idx}. {result}")
                generate_log(full_query, result_count, user, "Search")
            else:
                print("\x1b[31mNenhum resultado encontrado.\x1b[0m")

            print("Aguarde um momento...")
            time.sleep(random.randint(5, 10))

        except Exception as e:
            print(f"Erro ao realizar a busca: {e}")
            generate_log(full_query, 0, user, "Search", error=str(e))

