import datetime

def print_title():
    # O código da função print_title deve ser copiado aqui.
    pass

def generate_log(query, result_count, user, activity, error=None):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"Timestamp: {timestamp}, User: {user}, Query: {query}, Result Count: {result_count}, Activity: {activity}"
    if error:
        log_message += f", Error: {error}"
    with open("search_log.txt", "a") as log_file:
        log_file.write(log_message + "\n")
