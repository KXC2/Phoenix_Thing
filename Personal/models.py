from django.db import models

# Create your models here.

class Puns(models.Model):

    puns_text = models.CharField(max_length=250)
    pub_date = models.DateField('date published')

    def __str__(self):

        return str(self.puns_text)


class Thoughts(models.Model):

    thoughts_text = models.CharField(max_length=250)
    pub_date = models.DateField('date published')

    def __str__(self):

        return str(self.thoughts_text)

class DiaryEntry(models.Model):

    diary_entry = models.CharField(max_length=500)
    pub_date = models.DateField('date published')

    def __str__(self):

        return str(self.diary_entry)
