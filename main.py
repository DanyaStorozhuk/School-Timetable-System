import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_timetable.settings")


django.setup()


from datetime import datetime 
from django.core.exceptions import ObjectDoesNotExist
from schedule.models import Teacher, Class, Students, Subject, Schedule, Grade
t1 = Teacher.objects.create(name="Ivan Petrow")
t2 = Teacher.objects.create(name="Olga Nikitiokova")
t3 = Teacher.objects.create(name="Oleg Shevchenko")

c1 = Class.objects.create(name = '3-g')
c2 = Class.objects.create(name = '5-a')
c3 = Class.objects.create(name = '8-d')

Students.objects.create(name = 'Alex Kravcyk',  school_class= c2)
Students.objects.create(name = 'Maria Petryze',  school_class= c1)
Students.objects.create(name = 'Sofia Melnyk',  school_class=c3)
Students.objects.create(name='Dmytro Koval', school_class=c1)
Students.objects.create(name='Anna Tkachenko', school_class=c2)



Subject.objects.create(name='Mathematics', teacher=t1)
Subject.objects.create(name='English', teacher=t2)
Subject.objects.create(name='History', teacher=t3)
Subject.objects.create(name='Science', teacher=t1)


def add_subject():
    print("\nДодавання предмета")
    name = input("Введіть назву предмета: ").strip().lower()
    description = input("Введіть опис предмета:").strip().lower()

    if not name:
        print("Назва предмета не може бути порожньою")
        return
    
    # якщо предмет з такою назвою вже існує
    if Subject.objects.filter(name = name).exists():
        print("Предмет з такою назвою вже існує")
        return
    
    subject = Subject(name = name, description = description)
    subject.save()
    print(f"Предмет {name} успішно додано!")


def add_teacher():
    print("\nДодавання Вчителя")
    name = input("Введіть назву Вчителля:").strip().lower()
    age = input("Ведіть ваш вік").strip().lower()
    email = input("Веддіть вашу почту").strip().lower()
    subject = input("Веддіть предмет який веде цей вчитель").strip().lower()

    if not all([name, age, email, subject]):
        print("Поля не можуть бути порожні")
        return

    try:
        subject = Subject.objects.get(name = subject)
    except ObjectDoesNotExist:
        print(f"Предмет '{subject}' не знайдено!")
        return
    

    try:
        teacher = Teacher(
            name = name,
            age = age,
            email = email,
            subject = subject
        )
        teacher.save()
        print(f" Вчителя '{name,}' успішно додано!")
    except Exception as e:
        print(f"Помилка прии додаванні вчителя: {e}")


def add_class():
    print("\nДодавання Класу")
    name = input("Введіть назву Класу :").strip()

    if not name:
        print("Назва Класу не може бути порожнім")
        return
    
    if Class.objects.filter(name = name).exists():
        print(f"Клас з назвою '{name}' вже існує!")
        return
    

    class_new = Class(name = name)
    class_new.save()

    print(f"Клас '{name}' успішно доданий!")
    



################################


def add_students():
    print("\nДодавання студента")
    name = input("Введіть ім'я студента:").strip().lower()
    title = input("Ведіть опис цього студента").strip().lower()
    age = input("Введіть вік студента:").strip().lower()
    email = input("Ведіть почту студента:").strip().lower()
    student_class = input("В якому класі цей студент").strip().lower()

    if not all([name, title, age, email, student_class]):
        print("Ім'я студента та його інформація не можу бути порожньою")
        return

    try:
        student = Class.objects.get(name = student_class)
    except ObjectDoesNotExist:
        print(f"Такого класу '{name}' не знайдено! ")
        return
    

    try:
        student = Students(
            name = name,
            title = title,
            age = int(age),
            email = email,
            student_class = student_class
        )
        
        student.save()

        print(f"Студента '{name}' додано успішно!")
    except Exception as e:
        print(f"Помилка при додавані учня:{e}")




def add_lessons_schedule():
    print("\nДодавання заняття в розклад")
    day = input("Введіть день:").strip().lower()
    teacher = input("Введіть вчителя: ").strip().lower()
    students = input("Введіть студента:").strip().lower()
    subject = input("Введіть назву предмета: ").strip().lower()
    time_start = input("Введіть час початку (ГГ:ХХ): ").strip()
    time_end = input("Введіть час закінчення (ГГ:ХХ): ").strip()

    if not all([subject, students, teacher, day, time_start, time_end]):
        print("Обов'язкові поля не можуть бути порожніми!")
        return

    # дивимось чи є в "школі" такий предмет, студент та викладач
    try:
        existing_subject = Subject.objects.get(name=subject)
        existing_student = Students.objects.get(name = students)
        existing_teacher = Teacher.objects.get(name=teacher)
    except ObjectDoesNotExist as e:
        print(f"Не знайдено: {e}")
        return

    # перевіряємо чи коректна дата (переводимо в формат Date)
    try:
        time_start = datetime.strptime(time_start, "%H:%M")
        time_end = datetime.strptime(time_end, "%H:%M")
    except ValueError:
        print("Неправильний формат часу! Використовуйте ГГ:ХХ")
        return

    # створюємо та зберігаємо заняття в розкладі
    try:
        schedule = Schedule(
            day = day,
            students = existing_student,
            teacher = existing_teacher,
            subject = existing_subject,
            time_start=time_start,
            time_end=time_end
        )
        schedule.save()
        print(f"Заняття успішно додано до розкладу!")
    except Exception as e:
        print(f"Помилка при додаванні заняття: {e}")


def add_grade():
    print("\nДодавання оцінку")
    grade = input("Введіть оцінку:").strip().lower()
    students = input("Ведіть оцінку учня").strip().lower()
    

    if not all([grade, students]):
        print("поле з оцінкою не може бути порожнім")
        return

    
    grade = Grade(grade = grade, students=students)
    grade.save()
    print(f"{grade} успішно додано!")


def main():
    while True:
        print("УПРАВЛІННЯ ШКІЛЬНИМ РОЗКЛАДОМ")
        print("1 - Додати предмет")
        print("2 - Додати вчителя")
        print("3 - Додати клас")
        print("4 - Додати учня")
        print("5 - Додати заняття в розклад")
        print("6 - Додати оцінку")
        print("7 - Вийти")
        choice = input("Виберіть опцію від 1 до 7: ").strip()


        if choice == '1':
            add_subject()
        if choice == '2':
            add_subject()
        if choice == '3':
            add_subject()
        if choice == '4':
            add_subject()
        if choice == '5':
            add_subject()
        if choice == '6':
            add_subject()
        if choice == '7':
            print("Програма завершена.")
            break
        else:
            print("Невірний виріб! Обирайте уважніше")
        
            








