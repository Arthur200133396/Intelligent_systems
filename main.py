import csv
import numpy as np
import pandas as pd
import seaborn as sb
from random import randint

#Считываем файлы:
df_male = pd.read_csv('moscow_male.csv', sep=';', encoding='ansi', decimal=',')
df_female = pd.read_csv('moscow_female.csv', sep=';', encoding='ansi', decimal=',')

#Убираем лишний столбец
df_male = df_male.drop("Unnamed: 6", axis=1)
df_female = df_female.drop("Unnamed: 6", axis=1)

df_male = df_male[df_male["ID"] != "ID"]
df_female = df_female[df_female["ID"] != "ID"]

#Проверяем:
print(df_male.head())
print()
print(df_female.head())

print()
#Задание 1: Создать новую колонку "Sex" и заполнить ее значениями по умолчанию для каждого набора данных (moscow_female.csv и moscow_male.csv)

df_male["Sex"] = "Male"
df_female["Sex"] = "Female"


#Задание 2: Объединить оба набора данных в один датафрейм (например , merge по полю "Year")

print("Задание 2")
print(df_male.shape)
print(df_female.shape)

df = pd.concat([df_female, df_male], ignore_index=True)

#print(df.describe())
print(df)
print()

#Задание 3: Выделить последнюю букву имени в именах мальчика или девочки
print("Задание 3")
df["Last_char"] = df["Name"].str[-1]
#print(df.head())
print(df)
print()

#Задание 4: Визуализировать зависимость последней буквы в имени от пола
print("Задание 4")
dfs = df.sort_values("Last_char")
print(dfs.groupby(["Last_char", "Sex"])["ID"].count())


#sb.set(rc={"figure.figsize":(16, 12)})
#sb.countplot(data = dfs, x = "Last_char", hue = "Sex")
print()

#Задание 5: Написать функцию, которая на основе любого введеного имени, подбирает к нему обращение ("Г-жа" и "Г-дин")
print("Задание 5")

grouped = dfs.groupby(["Last_char", "Sex"])["ID"].count()

def get_appeal(name):
    sex_from_df = df[df["Name"] == name]["Sex"].unique()
    if (sex_from_df.size != 0):
        print("Имя найдено в DataFrame")
        print(sex_from_df[0])

    lc = name[-1]
    male_with_lc = grouped.get((lc, "Male"), default=0)
    female_with_lc = grouped.get((lc, "Female"), default=0)

    if (male_with_lc > female_with_lc):
        print("Определено по последней букве")
        print("Male")

    if (female_with_lc > male_with_lc):
        print("Определено по последней букве")
        print("Female")

get_appeal("Никита")