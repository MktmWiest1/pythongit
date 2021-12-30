# 1. Создать базу данных для записи личных дел
# 2. Сделать проверку на выполнение , и если он
# выполнен то надо его удалить
# 3. Также нужна произвольная возможность записи
# новых личных дел
# 4. Проверка на уникальные задачи
import sqlite3
data_basa = sqlite3.connect("Plan.db")
sql = data_basa.cursor()
sql.execute("CREATE TABLE IF NOT EXISTS users(Day TEXT,Morning TEXT,Lunch TEXT,Evening TEXT)")
data_basa.commit()


def registr():
    global  day, morning, lunch, evening
    while True:
        day = input('What day of the week:')
        morning = input('What are your plans for the morning:')
        lunch = input('What are your lunch plans:')
        evening = input('What are your plans for the evening: ')

        sql.execute(f"SELECT Day FROM users WHERE DAY = '{day}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?,?,?,?)",
                        ( day, morning, lunch, evening))
            data_basa.commit()
            for value in sql.execute("SELECT * FROM users"):
                print(value)
        else:
            print("The day of the week should not be repeated!")
            for value in sql.execute("SELECT * FROM users"):
                print(value)
        delete_choose = input("Do you have any fulfilled days?"
                              "If there is, then write the day of the week, if not, then write no:")
        sql.execute("DELETE FROM users WHERE Day == ?", (delete_choose,))
        if delete_choose != "нет":
            for value in sql.execute("SELECT * FROM users"):
                print(value)
            continue
        choose = input("Do you want to continue recording your plans? Yes or no")
        if choose == "Yes":
            continue
        elif choose == "No":
            for value in sql.execute("SELECT * FROM users"):
                print(value)
            print("Your plans are registered!")
            break
        else:
            print("Write only yes or no")

            break


if __name__ == '__main__':
    registr()
