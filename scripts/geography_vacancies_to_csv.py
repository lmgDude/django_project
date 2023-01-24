import collections
import itertools
import pandas as pd
from math import isnan

data_frame_salary = pd.DataFrame(columns=['salary', 'town', 'year'])
geography_salary = pd.DataFrame(columns=['Город', 'Средняя зарплата'])
geography_vacancy = pd.DataFrame(columns=['Город', 'Доля вакансий'])
dict_currency = {'USD': 68.67, 'RUR': 1, 'RUB': 1, 'KZT': 0.1484, 'BYR': 28.32, 'UAH': 1.86, 'EUR': 74.34}
dict_geography_vacancy = {}
dict_geography_salary = {}

vacancies_data = pd.read_csv('data_base.csv')
count_data = len(vacancies_data)


for index, row in vacancies_data.iterrows():
    year = row['datetime'][:4]
    town = row['town']
    currency = row['currency']
    salary_from = row['salary_from']
    salary_to = row['salary_to']

    if dict_geography_vacancy.get(town, False) is False:
        dict_geography_vacancy[town] = 1
    else:
        dict_geography_vacancy[town] = dict_geography_vacancy[town] + 1

    if not isnan(salary_from) or not isnan(salary_to):
        if isnan(salary_from):
            average_sum_salary = int(salary_to)
        elif isnan(salary_to):
            average_sum_salary = int(salary_from)
        else:
            average_sum_salary = (int(salary_to) + int(salary_from)) / 2
        data_frame_salary.loc[len(data_frame_salary.index)] = {'salary': average_sum_salary * dict_currency[currency],
                                                               'town': row['town'], 'year': year}

for index, row in data_frame_salary.iterrows():
    salary = row['salary']
    town = row['town']
    year = row['year']
    if dict_geography_salary.get(town, False) is False:
        dict_geography_salary[town] = [salary]
    else:
        dict_geography_salary[town].append(salary)

dict_geography_salary = collections.OrderedDict(sorted(dict_geography_salary.items()))
dict_geography_salary = dict(sorted(dict_geography_salary.items(), key=lambda item: sum(item[1]) / len(item[1]), reverse=True))

for key, value in itertools.islice(dict_geography_salary.items(), 9):
    geography_salary.loc[len(geography_salary.index)] = {'Город': key, 'Средняя зарплата': int(sum(value) / len(value))}

average_salary = 0
count_salary = 0
for key, value in itertools.islice(dict_geography_salary.items(), 9, None):
    average_salary += sum(value) / len(value)
    count_salary += 1

geography_salary.loc[len(geography_salary.index)] = {'Город': 'Другие города',
                                                       'Средняя зарплата': int(average_salary / count_salary)}

dict_geography_vacancy = dict(sorted(dict_geography_vacancy.items(), key=lambda item: item[1], reverse=True))

all_vacancies = 0

for key, value in itertools.islice(dict_geography_vacancy.items(), 9):
    all_vacancies += value
    geography_vacancy.loc[len(geography_vacancy.index)] = {'Город': key, 'Доля вакансий': str(round(
        (value / count_data * 100), 2)) + '%'}

geography_vacancy.loc[len(geography_vacancy.index)] = {'Город': 'Другие города',
                                                       'Доля вакансий': str(round(((count_data - all_vacancies)
                                                                                   / count_data * 100), 2)) + '%'}


geography_salary.to_csv('geography_salary.csv', index=False)
geography_vacancy.to_csv('geography_vacancy.csv', index=False)
