from load import load_data
from pltime import plt_time

def main():
    df = load_data()
    plt_time(df)

if __name__ == "__main__":
    main()
