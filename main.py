import json

menuItems = [
    "Добавление задачи",
    "Список задач",
    "Изменение статуса задач",
    "Удаление задачи"
    ]
dataBase = {}
taskItems = []
status = []

class getConfig:
    def __init__(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        dataBase = data["DataBase"]
        taskItems = data["TaskItems"]
        status = data["Status"]
        print("Succesfull")

class menu:
    def __init__(self):
        for item in menuItems:
            print(item)
        while True:
            try:
                choise = int(input("Выбор: "))
                if choise > 0 and choise < len(menuItems):
                    # тут добавлять пункты меню
                    print("Yeha")
                else: print("Не верный выбор")
            except ValueError as e: print(f"Error: {e} ")

class main:
    print("!")
    getConfig()
    menu()