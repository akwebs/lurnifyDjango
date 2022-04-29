from django.db import models
from courses.models import *
from accounts.models import *

QUESTIONS_TYPE_CHOICES=(
    ('normal','normal'),
    ('chapter','chapter'),
    ('topic','topic'),
    ('formula','formula'),)

Test_Set=(
    ('1','set-1'),
    ('2','set-2'),
    ('3','set-3'),
    ('4','set-4'),
    ('5','set-5'),
    ('6','set-6'),
    ('7','set-7'),
    ('8','set-8'),
    ('9','set-9'),
    ('10','set-10'),
)

Test_level=(
    ('1','level-1'),
    ('2','level-2'),
    ('3','level-3'),
    ('4','level-4'),
    
)

class create_test(BaseFields):
    test_name           = models.CharField(max_length=50)
    test_type           = models.CharField(max_length=10 , choices=QUESTIONS_TYPE_CHOICES , default='normal')
    course_id           = models.ForeignKey(course,   on_delete=models.SET_NULL , null=True , blank=True)
    subject_id          = models.ForeignKey(subjects, on_delete=models.SET_NULL , null=True , blank=True)
    chapter_id          = models.ForeignKey(chapter,  on_delete=models.SET_NULL , null=True , blank=True)
    topic_id            = models.ForeignKey(topic,    on_delete=models.SET_NULL , null=True , blank=True)
    test_duration       = models.CharField(max_length=5 ,default="2" , help_text="Time in minutes")
    question_positive_marks = models.CharField(max_length=5 ,default="4" , help_text="Positive marks for each question")
    question_negative_marks = models.CharField(max_length=5 ,default="1" , help_text="Negative marks for each question")

    test_set            = models.CharField(max_length=10 , choices=Test_Set , default='1')
    test_level          = models.CharField(max_length=10 , choices=Test_level , default='1')   


    def __str__(self):
        return self.test_name    



class instructions(BaseFields):
    create_test             = models.ForeignKey(create_test, on_delete=models.SET_NULL , null=True , blank=True , related_name="createTestInstructions")
    instruction_text = models.CharField(max_length=200)
    def __str__(self):
        return self.instruction_text





class questions_bank(BaseFields):
    DIFFICULTY_CHOICES=(
        ('easy','easy'),
        ('medium','medium'),
        ('hard','hard'),)

    QUESTIONS_STYLE_CHOICES=(
        ('single','single'),
        ('multiple','multiple'),
        ('true_false','true_false'),
        ('fill_in_the_blanks','fill_in_the_blanks'),
        ('range','range'),
    )    
    create_test             = models.ForeignKey(create_test, on_delete=models.SET_NULL , null=True , blank=True , related_name="testQuestionBank")
    question_text           = models.TextField(max_length=200,null=True ,blank=True)
    question_difficulty     = models.CharField(max_length=10,  default='easy',  choices=DIFFICULTY_CHOICES )
    question_style          = models.CharField(max_length=20 , default='single',choices=QUESTIONS_STYLE_CHOICES )
    questions_options       = models.CharField(max_length=5,   default="4" ,    help_text="Number of options")
    correct_option          = models.CharField(max_length=4,   default="1" ,    help_text="Correct option")
    question_image          = models.ImageField(upload_to='question_images',null=True ,blank=True)
    solution_image          = models.ImageField(upload_to='solution_images',null=True ,blank=True)
    solution_text           = models.TextField(max_length=200,null=True ,blank=True)
    is_verified             = models.BooleanField(default=False)
    
    



    
    