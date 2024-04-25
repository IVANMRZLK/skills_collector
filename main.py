import urllib.request

import pandas as pd

vac_url_list = []
list_skills = []
skills_dict = {}

url = input('Введите ссылку на страницу поиска с настроеными фильтрами: ')

number_of_pages = int(input('Введите количество страниц: '))

html_code_bytes = urllib.request.urlopen(url).read()

encoding = 'utf-8'
html_code_str = html_code_bytes.decode(encoding)
# print(type(html_code_str))


for i in range(number_of_pages):
    print('Страница по счету', i)
    print(url)
    url = url.replace(f'page={i-1}', f'page={i}')
    print(url)
    html_code_bytes = urllib.request.urlopen(url).read()
    encoding = 'utf-8'
    html_code_str = html_code_bytes.decode(encoding)
    # print(html_code_str)
    g = 0
    while html_code_str.find('"desktop":"https://hh.ru/vacancy/') != -1:
        g += 1
        print('вакансия', g)
        # print(html_code_str)
        # href="https://hh.ru/v "desktop":"https://hh.ru/vacancy/
        index1 = html_code_str.find('"desktop":"https://hh.ru/vacancy/') + 11
        print('index1', index1)
        index2 = html_code_str.find('"desktop":"https://hh.ru/vacancy/') + 41
        print('index2', index2)

        vac_url = html_code_str[index1:index2]
        vac_url_list.append(vac_url)
        print('урл вакансии', vac_url)
        html_code_str = html_code_str[index2:]
    print(vac_url_list)
# сначала собрать список с вакансиями и потом его перебрать и из него подоставать все что надо
for vacancy_url in vac_url_list:

    vacancy_bytes = urllib.request.urlopen(vacancy_url).read()
    encoding = 'utf-8'
    vacancy_str = vacancy_bytes.decode(encoding)
    # print(vacancy_str)
    print(vacancy_url)

    if vacancy_str.find('"keySkill":[') != -1:
        index1 = vacancy_str.find('"keySkill":[') + 12
        #print('index1', index1)
        index2 = vacancy_str.find(']},"driverLicenseTypes"')#не понятно как определить
        #print('index2', index2)

        str_skills = vacancy_str[index1:index2]
        list_vac_skill = str_skills.split(',')
        list_skills.extend(list_vac_skill)
    else:
        list_skills.append('Скиллы не указаны')

    #print(list_skills)
    print(f"Осмотрено {vac_url_list.index(vacancy_url)+1} вакансий из {len(vac_url_list)}")

u_list_skills = list(set(list_skills))

for u_skill in u_list_skills:
    skills_dict[u_skill] = 0
    for skill in list_skills:
        if u_skill == skill:
            skills_dict[u_skill] += 1

print(skills_dict)

z = pd.DataFrame(skills_dict, index=[0])
z.to_excel("file_name.xlsx")
