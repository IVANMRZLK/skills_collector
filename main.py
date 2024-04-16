import urllib.request

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

    for g in range(1, 21):
        print(html_code_str)
        # href="https://hh.ru/v
        index1 = html_code_str.find('href="https://hh.ru/v') + 6
        print('index1', index1)
        index2 = html_code_str.find('href="https://hh.ru/v') + 65
        print('index2', index2)

        vac_url = html_code_str[index1:index2]
        print('урл вакансии', vac_url)

        vac_html_code_bytes = urllib.request.urlopen(vac_url).read()
        encoding = 'utf-8'
        vac_html_code_str = vac_html_code_bytes.decode(encoding)
#       здесь мы получаем код страницы конкретной вакансии и дальше нам надо найти навыки.
        while vac_html_code_str.find('data - qa = "bloko-tag__text"') != -1 :
            vac_index1 = vac_html_code_str.find('data - qa = "bloko-tag__text"') + 29
            vac_index2 = vac_html_code_str.find('<', vac_index1)
            skill = html_code_str[vac_index1:vac_index2]

            if skill in list(skills_dict.keys()):
                skills_dict[skill] += 1
            else:
                skills_dict[skill] = 1

            vac_html_code_str = vac_html_code_str[vac_index2:]
#
        html_code_str = html_code_str[index2:]

print(skills_dict)
# некст надо сделать вывод в хl