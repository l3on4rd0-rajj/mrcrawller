import os

def fetch_queries_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"\x1b[31mArquivo {file_path} não encontrado.\x1b[0m")
        return []

