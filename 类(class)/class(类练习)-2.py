
"""
创建北京和成都两个校区
    -创建Linux/Python两个课程
    -创建北京校区的Python 3期课程和成都校区的Linux1期课程
    -管理员创建了北京校区的学员小张，并将其分配在了Python3期
    -管理员创建了讲师小周，并将其分配给了Python 3期
    -讲师小周创建了一条Python3期的上课记录 Day02
    -讲师小周为Day02这节课所有的学院批改了作业，小张得了A，小王得了B
    -学员小张查看了自己所报的课程
    -学员小张在查看了自己在Python3的成绩列表然后退出了
    -学院小张给了讲师小周好评
"""

Course_list = []


class School(object):
    def __init__(self, school_name):
        self.school_name = school_name
        self.student_list = []
        self.teacher_list = []
        global Course_list

    def hire(self, ob):
        self.teacher_list.append(ob.name)
        print("我们请了一个新老师{}".format(ob.name))

    def enroll(self, ob):
        self.student_list.append(ob.name)
        print("我们有一个新学员{}".format(ob.name))


class Grade(School):
    def __init__(self, school_name, grade_code, grade_course):
        super(Grade, self).__init__(school_name)
        self.course = grade_course
        self.code = grade_code
        self.menbers = []
        Course_list.append(self.course)
        print("我们现在有了{}学校的,年级是{},课程是{}".format(self.school_name, self.code,  self.course))

    def course_info(self):
        print("课程大纲{}是day01, day02, day03".format(self.course))


Python = Grade("北京", 3, "Python")
Linux = Grade("成都", 1, "Linux")
print(Course_list)


class School_menber(object):
    def __init__(self, name, age, sex, role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []
        print("我叫{},我是一个{}".format(self.name, self.role))


stu_num_id = 00


class Students(School_menber):
    def __init__(self, name, age, sex, role, course):
        super(Students, self).__init__(name, age, sex, role)
        global stu_num_id
        stu_num_id += 1
        stu_id = course.school_name + "S" + str(course.code) + str(stu_num_id).zfill(2)
        # zfill 填充的作用, 当只有一位数时前面填充0 只能对str类型操作

        self.id = stu_id
        self.mark_list = {}

    def study(self, course):
        print("我来这里学习{}课,我的学号是{}".format(course.course, self.id))

    def pay(self, course):
        print("我交了1000,学{}".format(course.course))
        self.course_list.append(course.course)

    def praise(self, ob):
        print("{}觉得{}课真棒".format(self.name, ob.name))

    def mark_check(self):
        for i in self.mark_list.items():
            print(i)

    def out(self):
        print("我离开了")


tea_num_id = 00


class Teacher(School_menber):
    def __init__(self, name, age, sex, role, course):
        super(Teacher, self).__init__(name, age, sex, role)
        global tea_num_id
        tea_num_id += 1
        tea_id = course.school_name + "T" + str(course.code) + str(tea_num_id).zfill(2)
        self.id = tea_id

    def teach(self, course):
        print("我来这里讲{}课,我的id是{}".format(course.course, self.id))

    def record_mark(self, Date, course, obj, level):
        obj.mark_list[str(course.course) + ": Date" + "学员: " + str(obj.name) + f": 第{Date}天 "] = level


a = Students("小张", 18, "man", "student", Python)
Python.enroll(a)
a.study(Python)
a.pay(Python)
b = Students("小b", 18, "man", "student", Linux)
Linux.enroll(b)
b.study(Linux)
c = Students("小v", 18, "man", "student", Linux)
Linux.enroll(c)
c.study(Linux)
t = Teacher("小周", 30, "man", "Teacher", Python)
Linux.hire(t)
a.praise(t)
t.record_mark(1, Python, a, "A")
t.record_mark(2, Python, a, "c")
print(a.course_list, a.mark_list)
a.mark_check()
a.out()
