import pandas as pd
from datetime import datetime as dt


files = [
    '2000_2021_Brazilian_Northeast_Region_daily_MW_instantaneous_maximum_demand_series.csv',
]


def parser(value):
    return dt.strptime(value, '%m/%d/%Y %H:%M:%S %p')


def transform(csv):
    csv = f"data/origin/{csv}"
    to_csv = csv.replace('origin', 'transformed')

    print(f"Transformando arquivo '{csv}'")
    df = pd.read_csv(csv, index_col='Din Instante', parse_dates=True, date_parser=parser)
    df = df.drop(columns=['Data do Incio da Semana Din Instante DM Simp 4', 'Data Escala de Tempo 1 DM Simp 4',
                          'Período Exibido DM Simp 4', 'Subsistema', 'Data Escala de Tempo 1 DM Simp 4.1',
                          'Texto Data Incio da Semana Din Instante DM'])
    df['date'] = df.index
    df.rename(
        columns={'Din Instante': 'date', 'Selecione Tipo de DM Simp 4': 'value'},
        inplace=True
    )

    df['value'] = df['value'].astype('float64')

    df.to_csv(to_csv)
    print(f"Tranformação concluida em '{to_csv}'")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for file in files:
        transform(file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
