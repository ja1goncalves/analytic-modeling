import pandas as pd
from datetime import datetime as dt


files = [
    'DADO_TESTE_UBE_48_12_univariate.csv',
    'DADO_TREINO_UBE_48_12_univariate.csv'
]


def parser(value):
    return dt.strptime(value, '%m/%d/%Y %H:%M:%S %p').strftime('%Y-%m-%d')


def transform(csv):
    csv = f"data/origin/{csv}"
    to_csv = csv.replace('origin', 'transformed')
    # Data Dica,value,date
    print(f"Transformando arquivo '{csv}'")
    df = pd.read_csv(csv, index_col='index',parse_dates=True)
    df['date'] = df.index

    df['value'] = df['value'].astype('float64')

    df.to_csv(to_csv)
    print(f"Tranformação concluida em '{to_csv}'")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for file in files:
        transform(file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
