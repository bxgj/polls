#/usr/bin/python

import django
django.setup()
from django.utils import timezone
from polls.models import *

def main():
    for i in range(100):
        q_text='question'+str(i)
        q = Question(question_text=q_text, pub_date=timezone.now())
        q.save()

def show():
    total_objects=Question.objects.all().count()
    print total_objects
    


