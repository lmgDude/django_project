import itertools
import matplotlib.pyplot as plt
import pandas as pd


vacancies_data = pd.read_csv('file_name_of_data.csv')
count_data = len(vacancies_data)

dict_years = {'2003': {}, '2004': {}, '2005': {}, '2006': {}, '2007': {}, '2008': {}, '2009': {}, '2010': {},
              '2011': {}, '2012': {}, '2013': {}, '2014': {}, '2015': {}, '2016': {}, '2017': {}, '2018': {},
              '2019': {}, '2020': {}, '2021': {}, '2022': {}}


for index, row in vacancies_data.iterrows():
    year = row['datetime'][:4]
    skills = row['skills']

    if str(skills) != 'nan':
        list_skills = str(skills).split('\r\n')
        for item in list_skills:
            if dict_years[year].get(item, False) is False:
                dict_years[year][item] = 1
            else:
                dict_years[year][item] = dict_years[year][item] + 1

for key, value in dict_years.items():
    dict_years[key] = dict(sorted(value.items(), key=lambda item: item[1], reverse=True))

list_frame_skills = []

for key, value in dict_years.items():
    year = f'Навыки за {key} год'
    list_frame_skills.append(pd.DataFrame(columns=[year, 'Количество']))
    for key_value, value_value in itertools.islice(value.items(), 10):
        list_frame_skills[-1].loc[len(list_frame_skills[-1].index)] = {year: key_value, 'Количество': value_value}

list_frame_skills = list_frame_skills[12:]

'''Сохранение csv файлов'''
"""for data in list_frame_skills:
    data.to_csv(f'{list(data.columns.values)[0]}.csv', index=False)"""

for year in range(2015, 2023):
    data = pd.read_csv(f'Навыки за {year} год.csv')

    X = [str(i) for i in data[f'Навыки за {year} год']]
    Y = data['Количество']

    plt.bar(X, Y, color='blue')
    plt.xticks(rotation=75)
    plt.grid(axis='y', linewidth=0.5)
    plt.title(f"Распределение навыков за {year}")
    plt.tight_layout()
    plt.locator_params(axis="both", integer=True, tight=True)
    """plt.show()"""

    plt.savefig(f'{year}.png', format='png')
