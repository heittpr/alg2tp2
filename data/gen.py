from scripts.load import load_data
from scripts.pltime import plt_time
from scripts.pltmem import plt_mem
from scripts.pltsumv import plt_sumv

def main():
    df = load_data()
    plt_time(df)
    plt_sumv(df)
    plt_mem(df)

if __name__ == "__main__":
    main()
