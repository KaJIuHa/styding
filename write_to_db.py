from config import conn


cur = conn.cursor()


def write_user_name_to_db(id, name):
    cur.execute("SELECT id_user_tg FROM tg_user WHERE id_user_tg = %s", (id, ))

    if cur.fetchone() is not None:
        print('User already exists')
    else:
        cur.execute(
            "INSERT INTO tg_user(id_user_tg, name) VALUES (%s, %s)", (id, name))
        conn.commit()


def get_category_id(category: str) -> int:
    cur.execute(
        'SELECT id_c_exp FROM category_expense WHERE title = %s', (category, ))
    return cur.fetchone()


def write_to_expense(data: dict) -> None:
    try:
        keys = ['title', 'expanses', 'date', 'id', 'category', 'name']

        for k in keys:
            data[k]

    except KeyError as err:
        print(f'Ошибка! Тип ошибки: {err}')

    except Exception as e:
        print('Что пошло не так', e)

    else:
        title = data['title']
        exp = data['expanses']
        date = data['date']
        id = data['id']
        category = get_category_id(data['category'])
        name = data['name']

        write_user_name_to_db(id, name)
        cur.execute("INSERT INTO expense(title, price, exp_date, owner_id, category_id) VALUES (%s, %s, %s, %s, %s);",
                    (title, exp, date, id, category))
        conn.commit()
    finally:
        conn.close()


if __name__ == '__main__':
    user_data = {
        'title': 'Auto',
        'date': '10.01.2023',
        'category': 'Кредит',
        'expanses': '1000.50',
        'id': 1021338626,
        'name': 'Вячеслав'
    }

    write_to_expense(user_data)
