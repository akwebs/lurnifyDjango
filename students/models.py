from django.db import models
from sqlalchemy import null
from accounts.models import *
from courses.models import *
from test_series.models import *
from admin_section.models import *
from io import BytesIO
from django.core.files.uploadedfile import  File
from PIL import Image , ImageDraw
import qrcode

# Create your models here.



class student_referral(models.Model):
    qr_code_number      = models.CharField(max_length=10,null=True,blank=True , unique=True)
    qr_code             = models.ImageField(upload_to='student_qr_code', null=True, blank=True)
    qr_wroth            = models.CharField(max_length=10, null=True, blank=True ,default="5" , help_text="it will be calculated in %")
    adding_limit        = models.IntegerField(default=0)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.qr_code_number

    def save(self, *args, **kwargs):
        #qrcode_img = qrcode.make(f'https://lurnify.in/'+self.qr_code_number+'/')
        if self.qr_code:
            pass
        else:
            qrcode_img = qrcode.make(self.qr_code_number)
            canvas = Image.new('RGB', (400, 400), 'white')
            draw = ImageDraw.Draw(canvas)
            canvas.paste(qrcode_img)
            fname= 'qr_code/'+self.qr_code_number+'_'+self.lurnify_member_id.phone+'.png'
            buffer = BytesIO()
            canvas.save(buffer, format="PNG")
            self.qr_code.save(fname, File(buffer), save=False)
            canvas.close()
            super().save(*args, **kwargs)
        




class student_profile(models.Model):
    user            = models.ForeignKey(Account, on_delete=models.CASCADE)
    student_name    = models.CharField(max_length=50)
    email           = models.EmailField(max_length=50,null=True, blank=True)  
    image           = models.ImageField(upload_to="students_images" , default="default.jpeg") 
    phone           = models.CharField(max_length=15, null=True,  blank=True)    
    address         = models.CharField(max_length=100,null=True, blank=True)   
    city            = models.CharField(max_length=50, null=True,  blank=True)    
    state           = models.CharField(max_length=50, null=True,  blank=True)    
    pin_code        = models.CharField(max_length=10, null=True,  blank=True)   
    coaching_name   = models.CharField(max_length=100, null=True,  blank=True)
    coaching_city   = models.CharField(max_length=50, null=True,  blank=True)
    course_program  = models.CharField(max_length=100, null=True,  blank=True)   
    country         = models.CharField(max_length=50, null=True,  blank=True  ,default="india")    
    date_of_birth   = models.DateField(null=True, blank=True)
    referal_code_id = models.ForeignKey("members.referal_code",on_delete=models.SET_NULL, null=True)
    firstMonday     = models.DateField(null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.student_name) + " " + str(self.phone)

class students_referral(models.Model):
    referral_sent_student      = models.ForeignKey(student_profile, on_delete=models.CASCADE, related_name="referral_sent_student")
    referral_get_student       = models.ForeignKey(student_profile, on_delete=models.CASCADE, related_name="referral_get_student")
    




class test_summary(models.Model):
    student_id = models.ForeignKey(student_profile, on_delete=models.SET_NULL, null=True, blank=True)
    create_test_id = models.ForeignKey(create_test, on_delete=models.SET_NULL, null=True, blank=True)
        

class academic_details(models.Model):
    student_id = models.ForeignKey(student_profile, on_delete=models.CASCADE)
    stream_id = models.ForeignKey(stream , on_delete=models.SET_NULL, null=True, blank=True)
    course_id = models.ForeignKey(course,  on_delete=models.SET_NULL, null=True, blank=True)
    course_start_date = models.DateField(null=True, blank=True)
    course_completion_date = models.ForeignKey(course_dates, on_delete=models.SET_NULL, null=True, blank=True)
    target_rank= models.CharField(max_length=20,null=True, blank=True)
    daily_pace = models.CharField(max_length=10,null=True, blank=True)
    academic_limits_id      = models.ForeignKey(academic_limits, on_delete=models.SET_NULL, null=True, blank=True)
    academic_update_count   = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.student_id) + " " + str(self.course_id)


class lurnifighter_badges_status(models.Model):
    student_id              = models.ForeignKey(student_profile, on_delete=models.CASCADE)
    lurnifighter_badges_id  = models.ForeignKey(lurnifighter_badges, on_delete=models.SET_NULL, null=True, blank=True)
    is_completed            = models.BooleanField(default=False)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.student_id) + " " + str(self.lurnifighter_badges_id) 
     




class lurnifighter_levels(models.Model):
    student_id              =   models.ForeignKey(student_profile, on_delete=models.CASCADE , null =True)
    weekly_challange_id     =   models.ForeignKey(weekly_challange , on_delete=models.CASCADE , null=True )
    weekly_reward_id        =   models.ForeignKey(weekly_reward , on_delete=models.CASCADE , null=True)
    total_study_hours       =   models.FloatField(null=True, blank=True , default=0)
    total_test              =   models.IntegerField(null=True, blank=True , default=0)
    total_crowns            =   models.IntegerField(null=True, blank=True , default=0)
    refer_freinds           =   models.IntegerField(null=True, blank=True , default=0)
    test_performances       =   models.FloatField(null=True, blank=True , default=0)
    study_effectiveness     =   models.IntegerField(null=True, blank=True , default=0)
    coupon_received         =  models.IntegerField(null=True, blank=True)
    coupon_used             =  models.IntegerField(null=True, blank=True)
    level_status            =   models.CharField(max_length=100, choices=(('completed','completed'),('incomplete','incomplete'),),)
    created_at              =   models.DateTimeField(auto_now_add=True)
    updated_at              =   models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.student_id) + " " + str(self.weekly_challange_id)

    class Meta:
        verbose_name_plural = "Lurnifighter Levels"
        verbose_name        = "Lurnifighter Levels"

class referral_and_winner(models.Model):
    student_id       = models.ForeignKey(student_profile, on_delete=models.CASCADE , null =True)
    lurnifighter_referral_id = models.ForeignKey(lurnifighter_referral, on_delete=models.CASCADE, null=True)    
    created_at               = models.DateTimeField(auto_now_add=True)
    updated_at               = models.DateTimeField(auto_now=True)




class lurnifighter_coupons(models.Model):
    student_id              =  models.ForeignKey(student_profile, on_delete=models.CASCADE , null=True)
    weekly_challange_id     =  models.ForeignKey(weekly_challange , on_delete=models.CASCADE , null=True )
    weekly_reward_id        =  models.ForeignKey(weekly_reward , on_delete=models.CASCADE , null=True)    
    referral_coupon         =  models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.student_id) + " " + str(self.weekly_challange_id)

    class Meta:
        verbose_name_plural = "Lurnifighter Acuried Referral Coupons"
        verbose_name        = "Lurnifighter Acuried Referral Coupons" 

 


# monthly_certificates =

all_months=(
    ('january','january'),
    ('february','february'),
    ('march','march'),
    ('april','april'),
    ('may','may'),
    ('june','june'),
    ('july','july'),
    ('august','august'),
    ('september','september'),
    ('october','october'),
    ('november','november'),
    ('december','december'),
)


class monthly_certificate(models.Model):
    student_id                      = models.ForeignKey(student_profile, on_delete=models.CASCADE , null=True)
    monthly_challange_criteria_id   = models.ForeignKey(monthly_challange_criteria , on_delete=models.CASCADE , null=True)
    test_performance                = models.IntegerField()
    weekly_challange                = models.IntegerField()
    month_name                      = models.CharField(max_length=50, choices=all_months)
    certificate                     = models.BooleanField(default=False)

    def __str__(self):
        return str(self.student_id) 
    class Meta:
        verbose_name_plural = "Lurnifighter Monthly Certificates"
        verbose_name        = "Lurnifighter Monthly Certificates"

# DAILY CHALLENGE 
class lurnifighter_daily_challenge(models.Model):
    student_id              = models.ForeignKey(student_profile, on_delete=models.CASCADE)
    test_and_study_id       = models.ForeignKey(test_and_study, on_delete=models.CASCADE , related_name='test_studies')
    total_coins             = models.IntegerField(default=0)
    total_crown             = models.IntegerField(default=0)
    is_completed            = models.BooleanField(default=False)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now=True)


class lurnifighter_cashcoupons(models.Model):
    student_id              = models.ForeignKey(student_profile, on_delete=models.CASCADE , null=True)
    got_for                 = models.CharField(max_length=50)
    cash_coupons_id         = models.ForeignKey(cash_coupons, on_delete=models.CASCADE, null=True)
    is_used                 = models.BooleanField(default=False)
    is_opened               = models.BooleanField(default=False)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.student_id) + " " + str(self.cash_coupons_id)

    class Meta:
        verbose_name_plural = "Lurnifighter Acuried Cash Coupons"
        verbose_name        = "Lurnifighter Acuried Cash Coupons"    

# payments
class student_payments(models.Model):
    student_id              = models.ForeignKey(student_profile, on_delete=models.CASCADE , null=True)
    allow_days              = models.ForeignKey("admin_section.payment_allow_days", on_delete=models.CASCADE , null=True)
    allow_date              = models.DateField()
    course_id               = models.ForeignKey(course , on_delete=models.CASCADE , null=True)
    course_dates_id         = models.ForeignKey(course_dates , on_delete=models.CASCADE , null=True)
    total_amount            = models.BigIntegerField(default=0) 
    remain_amount           = models.BigIntegerField(default=0) 
    paid_amount             = models.BigIntegerField(default=0) 
    total_paid              = models.BooleanField(default=False)
    
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.student_id) 

    class Meta:
        verbose_name_plural = "Student  Payments"
        verbose_name        = "Student  Payments"

class payment_installments(models.Model):
    student_id              = models.ForeignKey(student_profile, on_delete=models.CASCADE , null=True)
    student_payments_id         = models.ForeignKey(student_payments, on_delete=models.CASCADE , null=True)
    installment_no              = models.IntegerField()
    order_id                    = models.CharField(max_length=100)
    payment_id                  = models.CharField(max_length=100  , null=True, blank=True)
    installment_amount          = models.BigIntegerField(default=0)
    is_paid                     = models.BooleanField(default=False)
    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)



# SYINCING START FROM HERE 
class student_study(models.Model):
    studentId              = models.ForeignKey(student_profile, on_delete=models.CASCADE )
    courseId               = models.ForeignKey(course ,         on_delete=models.CASCADE )
    subjectId              = models.ForeignKey(subjects,        on_delete=models.CASCADE )
    unitId                 = models.ForeignKey(unit ,           on_delete=models.CASCADE )
    chapterId              = models.ForeignKey(chapter ,        on_delete=models.CASCADE)
    chapterDuration        = models.IntegerField(default=0 , null=True , blank=True)
    newChapterDuration     = models.IntegerField(default=0 , null=True , blank=True)
    topicId                = models.ForeignKey(topic,           on_delete=models.CASCADE , null=True , blank=True)
    topicDuration          = models.IntegerField(default=0 , null=True , blank=True)
    newTopicDuration       = models.IntegerField(default=0 , null=True , blank=True)
    startDatetime          = models.DateTimeField(null=True , blank=True)
    endDatetime            = models.DateTimeField(null=True , blank=True)
    startDate              = models.DateField(null=True , blank=True)
    studiedTime            = models.TimeField(null=True , blank=True)
    studyStatus            = models.CharField(max_length=50 , null=True , blank=True)
    coins                  = models.BigIntegerField(default=0 , null=True , blank=True)
    eNess                  = models.CharField(max_length=50 , null=True , blank=True)
    totalDuration          = models.BigIntegerField(default=0 , null=True , blank=True)
    isSync                 = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.studentId) 

    class Meta:
        verbose_name_plural = "Student  Study"
        verbose_name        = "Student  Study"
        


