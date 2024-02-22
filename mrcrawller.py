import getpass
import os
from config.tor_config import configure_tor, cleanup_and_exit
from search.search_engine import search_for_queries
from utils.file_operations import fetch_queries_from_file
from utils.logging import print_title
import pyfiglet

def main():
    tor_process = None

    try:
        # Exibe o logotipo "mrcrawler"
        font = pyfiglet.Figlet(font='slant')
        print(font.renderText("mrcrawller"))

        user = getpass.getuser()
        domain = input("Digite o domínio alvo (por exemplo, 'site:example.com'): ")

        search_mode = input("Escolha o modo de busca:\n1. Surface Web\n2. Dark Web\n3. Ambos\n")

        search_dorks = input("Deseja buscar por dorks específicas? (1 - Sim, 2 - Não): ")
        
        if search_dorks == '1':
            dorks_input = input("Informe as dorks específicas separadas por vírgula: ")
            queries = [dork.strip() for dork in dorks_input.split(",")]
        else:
            # Constroi o caminho do arquivo de dorks de forma dinâmica
            file_path = os.path.join(os.path.dirname(__file__), "dorks.txt")
            queries = fetch_queries_from_file(file_path)

        if not queries:
            return

        if search_mode in ['2', '3']:
            print("Iniciando o Tor. Isso pode demorar um pouco...")
            tor_process = configure_tor()
            print("Conectado à rede Tor.")

        search_for_queries(queries, domain, user, search_mode, tor_process)

    except KeyboardInterrupt:
        print("\nBusca interrompida pelo usuário.")
        cleanup_and_exit(tor_process)

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        cleanup_and_exit(tor_process)

if __name__ == "__main__":
    main()
