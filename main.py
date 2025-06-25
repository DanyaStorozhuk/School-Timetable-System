from schedule.models import Teacher, Class, Students, Subject


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