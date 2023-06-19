import requests

def vote(votes: list):
    max_dict = {}
    for element in set(votes):
        count = votes.count(element)
        max_dict.setdefault(count, [str(element)])
        print(max_dict)
        if str(element) not in max_dict[count]:
            max_dict[count].append(str(element))
    return ', '.join(max_dict[max(max_dict)])


courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]


def courses_duration(courses_list, duration_list):
    courses_list = []
    ready_dic = {}
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    durations_dict = {}
    for id, b in enumerate(courses_list):
        key = b['duration']
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id)
    durations_dict = dict(sorted(durations_dict.items()))
    for a, b in durations_dict.items():
        month = a
        for deep in b:
            course_id = deep
            name = courses_list[course_id]['title']
            ready_dic.setdefault(name, None)
            ready_dic[name] = month
    return ready_dic


def solution(a: float, b: float, c: float):
    def discriminant(a, b, c):
        d = b ** 2 - 4 * a * c
        return d

    if discriminant(a, b, c) < 0:
        return None
    elif discriminant(a, b, c) == 0:
        x_3 = - b / (2 * a)
        return x_3
    else:
        x_1 = (- b + discriminant(a, b, c) ** 0.5) / (2 * a)
        x_2 = (- b - discriminant(a, b, c) ** 0.5) / (2 * a)
        return x_1, x_2


def folder_create(folder_name):
    '''Функция создания папки на ЯД для загрузки фото'''
    with open('tokenyandex.txt', 'r') as f:
        tokenyandex = f.read().strip()
        fold_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': folder_name, "overwrite": "true"}
        headers = {'Content-Type': 'application/json', 'Authorization': tokenyandex}
        folder = requests.put(url=fold_url, headers=headers, params=params)
        if folder.status_code == 201:
            print(f'Папка {folder_name} успешно создана')
        elif folder.status_code == 409:
            print(f'Папка с именем {folder_name} уже существует')
        return folder.status_code
