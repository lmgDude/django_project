import collections
from math import isnan

import pandas as pd

data_frame_salary = pd.DataFrame(columns=['salary', 'town', 'year'])
data_salary = pd.DataFrame(columns=['Год', 'Средняя зарплата'])
data_vacancy = pd.DataFrame(columns=['Год', 'Количество вакансий'])

dict_currency = {'USD': 68.67, 'RUR': 1, 'RUB': 1, 'KZT': 0.1484, 'BYR': 28.32, 'UAH': 1.86, 'EUR': 74.34}
dict_vacancies_count = {}
dict_years = {}

for i in range(2003, 2023):
    dict_vacancies_count[str(i)] = 0

vacancies_data = pd.read_csv('data_base.csv')


for index, row in vacancies_data.iterrows():
    year = row['datetime'][:4]
    currency = row['currency']
    salary_from = row['salary_from']
    salary_to = row['salary_to']
    dict_vacancies_count[year] = dict_vacancies_count[year] + 1
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
    if dict_years.get(year, False) is False:
        dict_years[year] = [salary]
    else:
        dict_years[year].append(salary)

dict_years = collections.OrderedDict(sorted(dict_years.items()))
print(dict_years)

for key, value in dict_years.items():
    data_salary.loc[len(data_salary.index)] = {'Год': key, 'Средняя зарплата': int(sum(value) / len(value))}

for key, value in dict_vacancies_count.items():
    data_vacancy.loc[len(data_vacancy.index)] = {'Год': key, 'Количество вакансий': value}


data_salary.to_csv('data_salary.csv', index=False)
data_vacancy.to_csv('data_vacancy.csv', index=False)
