if __name__ != "__main__":
    raise RuntimeError("Only for use with the -m switch, not as a Python API")

from .borad_cli import main
main()