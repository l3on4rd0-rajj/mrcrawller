import stem.process
import sys

def configure_tor():
    tor_process = stem.process.launch_tor_with_config(
        config={
            'SocksPort': str(9050),
            'ControlPort': str(9051),
            'Log': ['NOTICE', 'ERR'],
        },
        init_msg_handler=print,
    )
    return tor_process

def cleanup_and_exit(tor_process=None):
    if tor_process:
        print("Encerrando o Tor...")
        tor_process.kill()
    print("Encerrando a aplicação.")
    sys.exit(0)

