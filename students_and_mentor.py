class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

# Первое задание
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# Второе задание
    def average_grade_student(self):
        if not self.grades:
            return 0
        grades_list_st = []
        for grade in self.grades.values():
            grades_list_st.extend(grade)
            return round(sum(grades_list_st) / len(grades_list_st), 1)


# третье задание метод __str__
    def __str__(self):
        average_grade = self.average_grade_student()
        return f'''Имя: {self.name} 
Фамили: {self.surname} 
Средняя оценка за лекции: {average_grade}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}   
Завершеные курсы: {" ".join(self.finished_courses)}'''


# третье задание операторы сравнения
    def __gt__(self, other):
        average_grade_st = self.average_grade_student()
        return average_grade_st <= other.average_grade_student()





class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.lecturer_list = []

# класс Лекторы первое задание
class Lecturer(Mentor):
    #первое задание и второе задание
        def __init__(self, name, surname):
            super().__init__(name, surname)
            self.grades = {}





        def average_grade_lecture(self):
            if not self.grades:
                return 0
            grades_list = []
            for grade in self.grades.values():
                grades_list.extend(grade)
                return round(sum(grades_list) / len(grades_list), 1)





        def __str__(self):
            average_grade_lec = self.average_grade_lecture()
            return f'''Имя: {self.name} 
Фамили: {self.surname} 
Средняя оценка за лекции: {average_grade_lec}'''

# Операторы сравнения
        def __gt__(self, other):
            average_grade_lec = self.average_grade_lecture()
            return average_grade_lec >= other.average_grade_lecture()




















class Reviewer(Mentor):
    #первое и второе задание
        def __init__(self, name, surname):
            super().__init__(name, surname)
        def rate_hw(self, student, course, grade):
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'

        def __str__(self):
            return f'''Имя: {self.name} 
Фамили: {self.surname}'''



















best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
best_student.grades['Python'] = [10, 10, 10, 10, 9]
best_student.grades['Git'] = [10, 10, 10, 10, 9]
best_student.grades['Введение в программирование'] = [ 10, 10, 8, 10, 10]
best_student.average_grade_student()


best_student2 = Student('Mat', 'Smit', 'your_gender')
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Введение в программирование']
best_student2.grades['Git'] = [10, 9, 10, 7, 9]
best_student2.grades['Введение в программирование'] = [ 10, 10, 9, 10, 10]


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor2 = Reviewer('Some', 'Buddy')
cool_mentor2.courses_attached += ['Javascript']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python', 'Git']
cool_lecturer.grades['Python'] = [10, 10, 10, 10, 9]
cool_lecturer.grades['Git'] = [9, 10, 10, 10, 9]

cool_lecturer2 = Lecturer('Don', 'Grant')
cool_lecturer2.courses_attached += ['Git']
cool_lecturer2.grades['Git'] = [10, 10, 8, 10, 9]


# Четвертое задание подсчет средней оценки за дз и лекции
lecturer_list = [cool_lecturer, cool_lecturer2]
def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lecturer in lecturer_list:
        if course_name in lecturer.courses_attached:
            sum_all += lecturer.average_grade_lecture()
            count_all += 1
            average_rating = sum_all / count_all
            return average_rating


student_list = [best_student, best_student2]

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for student in student_list:
        if course_name in student.courses_in_progress:
            sum_all += student.average_grade_student()
            count_all += 1
            average_rating = sum_all / count_all
            return average_rating








cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 10)


cool_mentor2.rate_hw(best_student, 'Javascript', 10)
cool_mentor2.rate_hw(best_student, 'Javascript', 9)
cool_mentor2.rate_hw(best_student, 'Javascript', 10)




print(cool_mentor)
print("")
print(cool_mentor2)
print("")
print(cool_lecturer)
print("")
print(cool_lecturer2)
print("")
print(best_student)
print("")
print(best_student2)
print("")
print(Student.__gt__(best_student2, best_student))
print("")
print(Lecturer.__gt__(cool_lecturer, cool_lecturer2))
print("")
print(lecturer_rating(lecturer_list, 'Python'))
print("")
print(lecturer_rating(lecturer_list, 'Git'))
print("")
print(student_rating(student_list, 'Python'))
print("")
print(student_rating(student_list, 'Git'))
print("")




