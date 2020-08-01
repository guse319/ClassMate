from django.db import models
from accounts.models import MyUser, MyUserManager

class TutorManager(models.Manager):
    def create_tutor(self, user, name):
        profile = self.model(user=user, name=name)
        profile.save(using=self._db)
        return profile

class TeacherManager(models.Manager):
    def create_teacher(self, user, name):
        profile = self.model(user=user, name=name)
        profile.save(using=self._db)
        return profile

class StudentManager(models.Manager):
    def create_student(self, user, name):
        profile = self.model(user=user, name=name)
        profile.save(using=self._db)
        return profile

class ParentManager(models.Manager):
    def create_parent(self, user, name):
        profile = self.model(user=user, name=name)
        profile.save(using=self._db)
        return profile



class TutorProfile(models.Model):
    user = models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    school = models.CharField(
        verbose_name='school',
        max_length=100,
        default=''
    )

    name = models.CharField(
        verbose_name='name',
        max_length=100,
        default='',
    )

    clients = models.CharField(
        verbose_name='clients',
        max_length=50,
        default='',
    )

    subjects = models.TextField(
        verbose_name='subjects',
        max_length=400,
        default='',
    )

    major = models.CharField(
        verbose_name='major',
        max_length=50,
        default='',
    )

    accommodations = models.CharField(
        verbose_name='accommodations',
        max_length=50,
        default='',
    )

    def __str__(self):
        return self.name

    objects = TutorManager()

class TeacherProfile(models.Model):
    user = models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    school = models.CharField(
        verbose_name='school',
        max_length=255,
        default='',
    )

    name = models.CharField(
        verbose_name='name',
        max_length=100,
        default='',
    )

    def __str__(self):
        return self.name

    objects = TeacherManager()

class StudentProfile(models.Model):
    user = models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    school = models.CharField(
        verbose_name='school',
        max_length=255,
        default='',
    )

    name = models.CharField(
        verbose_name='name',
        max_length=100,
        default='',
    )

    gradelevel = models.CharField(
        verbose_name='gradelevel',
        max_length=20,
        default='',
    )


    def __str__(self):
        return self.name

    objects = StudentManager()

class ParentProfile(models.Model):
    user = models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    school = models.CharField(
        verbose_name='school',
        max_length=255,
        default='',
    )

    name = models.CharField(
        verbose_name='name',
        max_length=100,
        default='',
    )

    def __str__(self):
        return self.name

    objects = ParentManager()
