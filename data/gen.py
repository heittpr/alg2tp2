from scripts.load import load_data
from scripts.pltime import plt_time
from scripts.pltmem import plt_mem
#from scripts.pltqlt import plt_qlt

def main():
    df = load_data()
    plt_time(df)
    plt_mem(df)
#    plt_qlt(df)

if __name__ == "__main__":
    main()
