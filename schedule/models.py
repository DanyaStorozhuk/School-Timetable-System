from django.db import models

# Create your models here.



class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    
    # subject - це назва поля моделі
    # models.ForeignKey(Subject, ...) - це тип поля в Django - який означає звязок багато до одного (Many-to-One relationship)
    # Тобто - багато вчителів можуть привязуватися до одного предмету
    # on_delete=models.CASCADE – важлива поведінка при видаленні об'єкта.
    # Тобто - якщо видалили предмет — видаляємо і всіх вчителів, хто його викладав"
    # related_name='teachers' – це ім'я зворотного доступу.
    # Через це ім’я ти зможеш з моделі Subject дістати всіх пов’язаних вчителів.
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return self.name




class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Students(models.Model):
    name = models.CharField(max_length=30)
    title = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    # student_class - це назва поля моделі
    # models.ForeignKey(Class, ...) - це тип поля в Django - який означає звязок багато до одного (Many-to-One relationship)
    # Тобто - багато студентів можуть належати до одного класу
    # on_delete=models.CASCADE – важлива поведінка при видаленні об'єкта.
    # Тобто - якщо видалили клас — видаляємо і всіх студентів, хто там навчався"
    # related_name='students' – це ім'я зворотного доступу.
    # Через це ім’я ти зможеш з моделі Class дістати всіх пов’язаних студентів.
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
    
class Schedule(models.Model):
    day = models.CharField(max_length=15)
    students = models.ForeignKey(Students, on_delete=models.CASCADE, related_name="schedule")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=30)
    time_start = models.DateField()
    time_end = models.DateField()

    def __str__(self):
        return self.day



class Grade(models.Model):
    grade = models.IntegerField()
    students = models.ForeignKey(Students, on_delete=models.CASCADE)
    

