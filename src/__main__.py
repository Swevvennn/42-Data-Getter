import fire
from .cli import CLI
from os import system


if __name__ == "__main__":
    system('clear')
    fire.Fire(CLI)
