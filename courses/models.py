from email.mime import image
from django.db import models
from django.forms import DurationField
from accounts.models import *



class stream(BaseFields):
    stream_name = models.CharField(max_length=100)
    image       = models.ImageField(upload_to='Streamimages/',null=True,blank=True)
    def __str__(self):
        return self.stream_name


class subjects(BaseFields):
    subject_name            = models.CharField(max_length=50)
    duration                = models.CharField(null=True ,blank=True,max_length=100)
    
    def __str__(self):
        return self.subject_name
class course(BaseFields):
    name            = models.CharField(max_length=255)
    stream_id       = models.ForeignKey(stream,on_delete=models.SET_NULL,null=True , blank=True)
    description     = models.TextField(null=True ,blank=True)
    duration        = models.CharField(null=True ,blank=True,max_length=100)
    start_date      = models.DateField(null=True ,blank=True)
    end_date        = models.DateField(null=True ,blank=True)
    course_expires  = models.DateField(null=True ,blank=True)
    course_fee      = models.CharField(null=True ,blank=True,max_length=100)
    course_type     = models.CharField(null=True ,blank=True,choices=[('1_year','1 Year Program'),('2_year','2 Year Program')],max_length=100)
    subjects        = models.ManyToManyField(subjects,blank=True,related_name='link_subjects')


    def __str__(self):
        return str(self.stream_id.stream_name) + " > " + self.name

class course_dates(BaseFields):
    course_id               = models.ForeignKey(course,on_delete=models.SET_NULL,null=True , blank=True)
    course_completion_date  = models.DateField(null=True ,blank=True)
    image                   = models.ImageField(upload_to='Calenderimages/',null=True,blank=True)
    duration                = models.CharField(null=True ,blank=True,max_length=50)

    def __str__(self):
        return str(self.course_id) + " > " + str(self.course_completion_date)


class unit(BaseFields):
    subject_id      = models.ForeignKey(subjects,on_delete=models.SET_NULL,null=True , blank=True , related_name="subjectUnit")
    unit_name       = models.CharField(max_length=100)
    duration        = models.CharField(null=True ,blank=True,max_length=100)

    def __str__(self):
        return str(self.subject_id.subject_name) + " > " + str(self.unit_name)

class chapter(BaseFields):
    subjects_id     = models.ForeignKey(subjects,on_delete=models.SET_NULL,null=True , blank=True , related_name="subjectChapter")
    unit_id         = models.ForeignKey(unit,on_delete=models.SET_NULL,null=True , blank=True , related_name="unitChapter")
    chapter_name    = models.CharField(max_length=100)
    duration        = models.CharField(null=True ,blank=True,max_length=100)

    def __str__(self):
        return str(self.subjects_id.subject_name) + " > " + str(self.unit_id.unit_name) + " > " + str(self.chapter_name)

topic_type=(
    ('normal','normal'),
    ('full','full'),
    ('formula','formula'),
)

class topic(BaseFields):
    chapter_id      = models.ForeignKey(chapter,on_delete=models.SET_NULL,null=True , blank=True , related_name="chapterTopic")
    serial_number= models.CharField(max_length=100,null=True ,blank=True)
    duration        = models.CharField(null=True ,blank=True,max_length=100)
    topic_importance=models.CharField(null=True ,blank=True,max_length=50)
    topic_lable     = models.CharField(max_length=100,null=True ,blank=True,choices=topic_type)
    topic_name       = models.CharField(max_length=100)
    def __str__(self):
        return str(self.chapter_id.subjects_id.subject_name) + " > " + str(self.chapter_id.chapter_name) + " > " + str(self.topic_name)
    
class subtopic(BaseFields):
    topic_id        = models.ForeignKey(topic,on_delete=models.SET_NULL,null=True , blank=True, related_name="topicSubtopic")
    subtopic_name   = models.CharField(max_length=100)
    duration        = models.CharField(null=True ,blank=True,max_length=100)

    def __str__(self):
        return self.subtopic_name


class subbtopic_text(BaseFields):
    subtopic_id     = models.ForeignKey(subtopic,on_delete=models.SET_NULL,null=True , blank=True,related_name="subtopicText")
    subtopic_text   = models.TextField(null=True ,blank=True)
    
    def __str__(self):
        return self.subtopic_text

    
# class question_bank(models.Model):
#     chapter_id      = models.ForeignKey(chapter,on_delete=models.SET_NULL,null=True , blank=True)
#     topic_id        = models.ForeignKey(topic,on_delete=models.SET_NULL,null=True , blank=True)
#     question_number = models.IntegerField(null=True ,blank=True)
#     question_text        = models.TextField(null=True ,blank=True)
#     question_image = models.FileField(null=True ,blank=True , upload_to='question_images')

    
