# -*- coding: utf-8 -*-
"""LESSON_9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xD61ykWaJo8jZPmKWkh68oumRt4NAtPf

Задача 1
Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
"""

import pandas as pd
df = pd.read_csv('/content/sample_data/california_housing_train.csv')

df

df_new = df[df['population'] < 500]['median_house_value']

df_new

df_new.mean()

"""Задача 2
Узнать какая максимальная households в зоне минимального значения population
"""

df[df['population'] == df['population'].min()]['households'].max()