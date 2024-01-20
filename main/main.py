import sqlite3

db = sqlite3.connect('university.db')

db.execute('''CREATE TABLE IF NOT EXISTS students(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name VARCHAR(50),
           age INTEGER,
           major VARCHAR(50));''')

db.execute('''CREATE TABLE IF NOT EXISTS courses(
           course_id INTEGER PRIMARY KEY AUTOINCREMENT,
           course_name VARCHAR(50),
           instructor VARCHAR(50));''')

"""db.execute('''CREATE TABLE IF NOT EXISTS student_course(
           student_id INTEGER,
           course_id INTEGER,
           PRIMARY KEY (student_id, course_id),
           FOREIGN KEY (student_id) REFERENCES students (id),
           FOREIGN KEY (course_id) REFERENCES courses (course_id));''')"""



while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")
    
    match choice:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case _:
            print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")



"""INSERT INTO students(name, age, major)
VALUES  ("STudent6", 126, "major61")
INSERT INTO courses(course_name, instructor)
VALUES  ("instructor3243", "123")
"""