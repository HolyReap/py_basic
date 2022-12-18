class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)  
        
    def rate_lr(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'   
    
    def course_list_act(self):
        res = ''
        for item in self.courses_in_progress:
            if res == '':
                res = item
            else:
                res += f', {item}'
        return res
    
    def course_list_fin(self):
        res = ''
        for item in self.finished_courses:
            if res == '':
                res = item
            else:
                res += f', {item}'
        return res
        
    def avrg_grade(self):
        if self.grades == {}:
            return 'Нет оценок'
        count_grades = 0
        sum_grades = 0
        for item in self.grades.values():
            count_grades += len(item) 
            sum_grades += sum(item)  
        return round(sum_grades/count_grades,2)  
    
    def __str__(self):
        res = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n' 
            f'Средняя оценка за домашние задания: {self.avrg_grade()}\n'
            f'Курсы в процессе изучения: {self.course_list_act()}\n'
            f'Завершенные курсы: {self.course_list_fin()}\n'
        )
        return res     
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Сравнение не со студентом'
        if self.avrg_grade() == 'Нет оценок':
            return f'Нет оценок у {self.name} {self.surname}'
        if other.avrg_grade() == 'Нет оценок':
            return f'Нет оценок у {other.name} {other.surname}'  
        return self.avrg_grade() < other.avrg_grade()  
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def avrg_grade(self):
        if self.grades == {}:
            return 'Нет оценок'
        count_grades = 0
        sum_grades = 0
        for item in self.grades.values():
            count_grades += len(item) 
            sum_grades += sum(item)  
        return round(sum_grades/count_grades,2)   
    
    def __str__(self):
        res = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n' 
            f'Средняя оценка за лекции: {self.avrg_grade()}\n'
        )
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Сравнение не с лектором'
        if self.avrg_grade() == 'Нет оценок':
            return f'Нет оценок у {self.name} {self.surname}'
        if other.avrg_grade() == 'Нет оценок':
            return f'Нет оценок у {other.name} {other.surname}'  
        return self.avrg_grade() < other.avrg_grade()
        
class Rewiewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
        )
        return res

def avarage_hw_course(students_list, course):
    count_grades = 0
    sum_grades = 0
    for student in students_list:
        if isinstance(student, Student):
            count_grades += len(student.grades[course]) 
            sum_grades += sum(student.grades[course])  
    if count_grades == 0:
        return 'Нет оценок'
    return round(sum_grades/count_grades,2)   

def avarage_lect_course(lecturers_list, course):
    count_grades = 0
    sum_grades = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer):
            count_grades += len(lecturer.grades[course]) 
            sum_grades += sum(lecturer.grades[course])  
    if count_grades == 0:
        return 'Нет оценок'
    return round(sum_grades/count_grades,2) 

rewiewer_1 = Rewiewer ('Jhon', 'Smith')
rewiewer_2 = Rewiewer ('Guy', 'Fawkes')

lecturer_1 = Lecturer ('Hannibal','Lector')
lecturer_2 = Lecturer ('Jonathan','Crane')

student_1 = Student('Jane','Doe','F')
student_2 = Student('Mary','Sue','F')

rewiewer_1.courses_attached += ['Cooking']
lecturer_1.courses_attached += ['Cooking']
lecturer_2.courses_attached += ['Cooking']
student_1.courses_in_progress += ['Cooking']
student_2.courses_in_progress += ['Cooking']

rewiewer_2.courses_attached += ['Philosophy']
lecturer_1.courses_attached += ['Philosophy']
student_1.courses_in_progress += ['Philosophy']
student_2.courses_in_progress += ['Philosophy']

rewiewer_1.courses_attached += ['Agronomy']
lecturer_2.courses_attached += ['Agronomy']
student_2.courses_in_progress += ['Agronomy']

student_1.finished_courses += ['Basket weaving']
student_2.finished_courses += ['Wilderness survival']

student_1.rate_lr(lecturer_1, 'Cooking', 10)
student_1.rate_lr(lecturer_1, 'Cooking', 10)
student_1.rate_lr(lecturer_1, 'Cooking', 8)
student_1.rate_lr(lecturer_2, 'Cooking', 10)
student_1.rate_lr(lecturer_2, 'Cooking', 5)
student_2.rate_lr(lecturer_1, 'Cooking', 10)
student_2.rate_lr(lecturer_1, 'Cooking', 10)
student_2.rate_lr(lecturer_2, 'Cooking', 8)
student_2.rate_lr(lecturer_2, 'Cooking', 8)

student_1.rate_lr(lecturer_1, 'Philosophy', 10)
student_1.rate_lr(lecturer_1, 'Philosophy', 10)
student_1.rate_lr(lecturer_1, 'Philosophy', 8)
student_1.rate_lr(lecturer_1, 'Philosophy', 10)
student_1.rate_lr(lecturer_1, 'Philosophy', 8)
student_2.rate_lr(lecturer_1, 'Philosophy', 10)
student_2.rate_lr(lecturer_1, 'Philosophy', 7)
student_2.rate_lr(lecturer_1, 'Philosophy', 8)
student_2.rate_lr(lecturer_1, 'Philosophy', 8)

student_2.rate_lr(lecturer_2, 'Agronomy', 10)
student_2.rate_lr(lecturer_2, 'Agronomy', 8)
student_2.rate_lr(lecturer_2, 'Agronomy', 10)
student_2.rate_lr(lecturer_2, 'Agronomy', 9)
student_2.rate_lr(lecturer_2, 'Agronomy', 6)
student_2.rate_lr(lecturer_2, 'Agronomy', 8)

rewiewer_1.rate_hw(student_1, 'Cooking', 6)
rewiewer_1.rate_hw(student_1, 'Cooking', 6)
rewiewer_1.rate_hw(student_1, 'Cooking', 8)
rewiewer_1.rate_hw(student_1, 'Cooking', 7)
rewiewer_1.rate_hw(student_1, 'Cooking', 5)
rewiewer_1.rate_hw(student_2, 'Cooking', 10)
rewiewer_1.rate_hw(student_2, 'Cooking', 5)
rewiewer_1.rate_hw(student_2, 'Cooking', 10)
rewiewer_1.rate_hw(student_2, 'Cooking', 8)

rewiewer_2.rate_hw(student_1, 'Philosophy', 6)
rewiewer_2.rate_hw(student_1, 'Philosophy', 5)
rewiewer_2.rate_hw(student_1, 'Philosophy', 5)
rewiewer_2.rate_hw(student_1, 'Philosophy', 6)
rewiewer_2.rate_hw(student_1, 'Philosophy', 8)
rewiewer_2.rate_hw(student_2, 'Philosophy', 10)
rewiewer_2.rate_hw(student_2, 'Philosophy', 9)
rewiewer_2.rate_hw(student_2, 'Philosophy', 8)
rewiewer_2.rate_hw(student_2, 'Philosophy', 9)

rewiewer_1.rate_hw(student_2, 'Agronomy', 4)
rewiewer_1.rate_hw(student_2, 'Agronomy', 7)
rewiewer_1.rate_hw(student_2, 'Agronomy', 10)
rewiewer_1.rate_hw(student_2, 'Agronomy', 9)
rewiewer_1.rate_hw(student_2, 'Agronomy', 9)
rewiewer_1.rate_hw(student_2, 'Agronomy', 8)

print(lecturer_1)
print(lecturer_2)
print(rewiewer_1)
print(rewiewer_2)
print(student_1)
print(student_2)

print(lecturer_1 > lecturer_2)
print(student_1 > student_2)

all_students = [student_1, student_2]
all_lecturers = [lecturer_1, lecturer_2]

print(avarage_hw_course(all_students, 'Cooking'))
print(avarage_lect_course(all_lecturers, 'Cooking'))
