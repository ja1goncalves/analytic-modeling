import pandas as pd
from datetime import datetime as dt


files = [
    'Simples_Geração_de_Energia_Dia_data_nordeste.csv',
    'Simples_Geração_de_Energia_Dia_data_norte.csv'
]


def parser(value):
    return dt.strptime(value, '%d/%m/%Y %H:%M')


def transform(csv):
    csv = f"data/origin/{csv}"
    to_csv = csv.replace('origin', 'transformed')

    print(f"Transformando arquivo '{csv}'")
    df = pd.read_csv(csv, index_col='Data Dica', parse_dates=True, date_parser=parser, delimiter=';')
    df = df.drop(columns=['Data Escala de Tempo 1 GE Simp 4', 'dsc_estado',
                          'id_subsistema', 'nom_tipousinasite', 'nom_usina2',
                          'Período Exibido GE'])
    df['date'] = df.index
    df.rename(
        columns={'Data Dica': 'date', 'Selecione Tipo de GE Simp 4': 'value'},
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
