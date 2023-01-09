import requests
import json

base_url = 'https://petstore.swagger.io/v2'

# ПИТОМЦЫ
# Добавляем нового питомца
print('------ВСЁ О ВАШИХ ПИТОМЦАХ------\n\n')
print("'Добавляем нового питомца'")

pet_new = {
    "id": 1935678,
    "category": {"id": 0, "name": "turtle"},
    "name": "Silvia",
    "photoUrls": ["string"],
    "tags": [{"id": 0, "name": "turtle"}],
    "status": "available"
}

pet_js = json.dumps(pet_new, ensure_ascii=False)

res_post = requests.post(f'{base_url}/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=pet_js)

print(f'Статус ответа от сервера на POST запрос: {res_post.status_code}')
print(res_post.text)
print(res_post.json())
print(type(res_post.json()))
print('\n---------------------\n')


# Добавляем фото питомца
print("'Добавляем фото питомца'")

petId = 1935678
pet_photo = 'Silvia.jpg'
files = {'file': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
res_post_photo = requests.post(f'{base_url}/pet/{petId}/uploadImage', headers={'accept': 'application/json'}, files=files)

print(f'Статус ответа от сервера на POST запрос: {res_post_photo.status_code}')
print(res_post_photo.text)
print(res_post_photo.json())
print(type(res_post_photo.json()))
print('\n---------------------\n')



# Просмотр информации по питомцу по id
print("'Просмотр инфо по питомцу'")

id = 1935678
res_get = requests.get(f'{base_url}/pet/{id}', headers={'accept': 'application/json'})

print(f'Статус ответа от сервера на GET запрос: {res_get.status_code}')
print(res_get.text)
print(res_get.json())
print(type(res_get.json()))
print('\n---------------------\n')


# Изменяем данные питомца
print("'Изменяем данные питомца'")

pet_new_change = {
    "id": 1935678,
    "category": {"id": 0, "name": "lizard"},
    "name": "Silvia",
    "photoUrls": ["string"],
    "tags": [{"id": 0, "name": "lizard"}],
    "status": "sold"
}

pet_js = json.dumps(pet_new_change, ensure_ascii=False)
res_put = requests.put(f'{base_url}/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=pet_js)


print(f'Статус ответа от сервера на PUT запрос: {res_put.status_code}')
print(res_put.text)
print(res_put.json())
print(type(res_put.json()))
print('\n---------------------\n')


# Обновляем питомца данными формы
print("'Обновляем данные питомца по форме'")

petId_new = 1935678
name_change = 'Lizabet'
status_change = 'pending'
info = f'name={name_change}&status={status_change}'

res_post_form = requests.post(f'{base_url}/pet/{petId_new}', headers={'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}, data=info)


print(f'Статус ответа от сервера на POST запрос: {res_post_form.status_code}')
print(res_post_form.text)
print(res_post_form.json())
print(type(res_post_form.json()))
print('\n---------------------\n')

# Удаление питомца
print("'Удаляем питомца'")

petId = 1935678

res_delet = requests.delete(f'{base_url}/pet/{petId}', headers={'accept': 'application/json'})

print(f'Статус ответа от сервера на DELET запрос: {res_delet.status_code}')
print(res_delet.text)
print(res_delet.json())
print(type(res_delet.json()))
print('\n---------------------\n')



# ОПЕРАЦИИ С ПОЛЬЗОВАТЕЛЯМИ
# Создать список пользователей с заданным входным массивом
print('-------ОПЕРАЦИИ С ПОЛЬЗОВАТЕЛЯМИ-----\n\n')
print("'Создаём список пользователей'")

list_user_object = [
    {
        "id": 0,
        "username": "MarkS",
        "firstName": "Mark",
        "lastName": "Hoff",
        "email": "markhoff@gmail.ru",
        "password": "password",
        "phone": "+7852369741",
        "userStatus": 0
    },
    {
        "id": 0,
        "username": "EmilZZ",
        "firstName": "Emilyen",
        "lastName": "Russo",
        "email": "russoemil@mail.ru",
        "password": "password",
        "phone": "+27778495162",
        "userStatus": 0
    }
]

info_list = json.dumps(list_user_object, ensure_ascii=False)
res_post_userlist = requests.post(f'{base_url}/user/createWithArray', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=info_list)

print(f'Статус ответа от сервера на POST запрос: {res_post_userlist.status_code}')
print(res_post_userlist.text)
print(res_post_userlist.json())
print(type(res_post_userlist.json()))
print('\n---------------------\n')

# Найти пользователя по имени
print("'Найти пользователя по имени'")

username = 'MarkS'
res_get_user = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})

print(f'Статус ответа от сервера на GET запрос: {res_get_user.status_code}')
print(res_get_user.text)
print(res_get_user.json())
print(type(res_get_user.json()))
print('\n---------------------\n')

# Внести изменения в данные пользователя
print("'Внести изменения в данные пользователя'")

username = 'MarkS'
new_user = {
    "id": 0,
    "username": "MarkSS",
    "firstName": "Mark",
    "lastName": "Hoff",
    "email": "markhoffer@gmail.ru",
    "password": "password",
    "phone": "+7852369741",
    "userStatus": 0
}
new_user_js = json.dumps(new_user, ensure_ascii=False)
res_put_user = requests.put(f'{base_url}/user/{username}', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=new_user_js)

print(f'Статус ответа от сервера на PUT запрос: {res_put_user.status_code}')
print(res_put_user.text)
print(res_put_user.json())
print(type(res_put_user.json()))
print('\n---------------------\n')