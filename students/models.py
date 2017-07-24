from django.db import models


"""Student Model"""


class Student(models.Model):

    class Meta(object):
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенти'

    first_name = models.CharField(max_length=256, blank=False, verbose_name='Ім’я')
    last_name = models.CharField(max_length=256, blank=False, verbose_name='Прізвище')
    middle_name = models.CharField(max_length=256, blank=True, verbose_name='По-батькові', default='')
    birthday = models.DateField(blank=False, verbose_name='Дата народження', null=True)
    photo = models.ImageField(blank=True, verbose_name='Фото', null=True)
    student_group = models.ForeignKey('students.Group', verbose_name='Група', blank=False, null=True, on_delete=models.PROTECT)
    ticket = models.CharField(max_length=256, blank=False, verbose_name='Білет')
    notes = models.TextField(blank=True, verbose_name='Додаткові нотатки')

    def __str__(self):
        return '% s % s' % (self.first_name, self.last_name)


"""Group Model"""


class Group(models.Model):

    class Meta(object):
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'

    title = models.CharField(max_length=256, blank=False, verbose_name='Назва')
    leader = models.OneToOneField(Student, verbose_name='Староста', blank=True, null=True, on_delete=models.SET_NULL)
    notes = models.TextField(blank=True, verbose_name='Додаткові нотатки')

    def __str__(self):
        if self.leader:
            return '% s (% s % s)' % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return '% s' % (self.title,)


"""Student Model"""


# class Student(models.Model):
#
#     class Meta(object):
#         verbose_name = 'Student'
#         verbose_name_plural = 'Students'
#
#     first_name = models.CharField(max_length=256, blank=False, verbose_name='First name')
#     last_name = models.CharField(max_length=256, blank=False, verbose_name='Last name')
#     middle_name = models.CharField(max_length=256, blank=True, verbose_name='Third name', default='')
#     birthday = models.DateField(blank=False, verbose_name='Was born', null=True)
#     photo = models.ImageField(blank=True, verbose_name='Photo', null=True)
#     student_group = models.ForeignKey('students.Group', verbose_name='Group', blank=False, null=True, on_delete=models.PROTECT)
#     ticket = models.CharField(max_length=256, blank=False, verbose_name='Ticket')
#     notes = models.TextField(blank=True, verbose_name='Notes')
#
#     def __str__(self):
#         return '% s % s' % (self.first_name, self.last_name)
#
#
# """Group Model"""
#
#
# class Group(models.Model):
#
#     class Meta(object):
#         verbose_name = 'Group'
#         verbose_name_plural = 'Groups'
#
#     title = models.CharField(max_length=256, blank=False, verbose_name='Name')
#     leader = models.OneToOneField(Student, verbose_name='Leader', blank=True, null=True, on_delete=models.SET_NULL)
#     notes = models.TextField(blank=True, verbose_name='Notes')
#
#     def __str__(self):
#         if self.leader:
#             return '% s (% s % s)' % (self.title, self.leader.first_name, self.leader.last_name)
#         else:
#             return '% s' % (self.title,)


class MonthJournal(models.Model):
    class Meta:
        verbose_name = 'Місячний журнал'
        verbose_name_plural = 'Місячні журнали'

    student = models.ForeignKey('Student', verbose_name='Студент', blank=False, unique_for_month='date')
    date = models.DateField(verbose_name='Дата', blank=False)
    present_day1 = models.BooleanField(default=False)
    present_day2 = models.BooleanField(default=False)
    present_day3 = models.BooleanField(default=False)
    present_day4 = models.BooleanField(default=False)
    present_day5 = models.BooleanField(default=False)
    present_day6 = models.BooleanField(default=False)
    present_day7 = models.BooleanField(default=False)
    present_day8 = models.BooleanField(default=False)
    present_day9 = models.BooleanField(default=False)
    present_day10 = models.BooleanField(default=False)
    present_day11 = models.BooleanField(default=False)
    present_day12 = models.BooleanField(default=False)
    present_day13 = models.BooleanField(default=False)
    present_day14 = models.BooleanField(default=False)
    present_day15 = models.BooleanField(default=False)
    present_day16 = models.BooleanField(default=False)
    present_day17 = models.BooleanField(default=False)
    present_day18 = models.BooleanField(default=False)
    present_day19 = models.BooleanField(default=False)
    present_day20 = models.BooleanField(default=False)
    present_day21 = models.BooleanField(default=False)
    present_day22 = models.BooleanField(default=False)
    present_day23 = models.BooleanField(default=False)
    present_day24 = models.BooleanField(default=False)
    present_day25 = models.BooleanField(default=False)
    present_day26 = models.BooleanField(default=False)
    present_day27 = models.BooleanField(default=False)
    present_day28 = models.BooleanField(default=False)
    present_day29 = models.BooleanField(default=False)
    present_day30 = models.BooleanField(default=False)
    present_day31 = models.BooleanField(default=False)

    def __str__(self):
        return '%s: %d, %d' % (self.student.last_name, self.date.month, self.date.year)





