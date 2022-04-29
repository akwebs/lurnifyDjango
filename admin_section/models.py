from django.db import models

from django.db import models
from accounts.models import BaseFields



class payment_allow_days(BaseFields):
    allow_days = models.IntegerField(default=0)

    def __str__(self):
        return str(self.allow_days)
    
class academic_limits(models.Model):
    limit_no = models.IntegerField(default=0)

    def __str__(self):
        return str(self.limit_no)
    class Meta:
        verbose_name_plural = "Academic Update Limits"
        verbose_name = "Academic Update Limit"


class cash_coupons(BaseFields):
    coupon_code             = models.CharField(max_length=8, unique=True , null=True, blank=True)
    coupon_name             = models.CharField(max_length=50)
    coupon_value            = models.IntegerField(null=True,  blank=True)
    expires_at              = models.DateField()

    def __str__(self):
        return str(self.coupon_name) + " " + str(self.coupon_value)

    class Meta:
        verbose_name_plural = "Cash Coupons"
        verbose_name = "Cash Coupon"


class monthly_challange_criteria(BaseFields):
    test_performance            =   models.IntegerField()
    weekly_challange            =   models.IntegerField()
    
    def __str__(self):
        return str(self.test_performance) + " " + str(self.weekly_challange)
    
    
    class Meta:
        verbose_name_plural = "Monthly Challange Criteria"
        verbose_name        = "Monthly Challange Criteria"


class lurnifighter_badges(BaseFields):
    level_name              = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Lurnifighter Badges Levels"
        verbose_name        = "Lurnifighter Badges Levels"  

    def __str__(self):
        return str(self.level_name)

class lurnifighter_referral(BaseFields):
    badge_name         = models.CharField(max_length=50)
    reffrral_count     = models.IntegerField(null=True, blank=True , default=0)
    description        = models.CharField(max_length=100 , null=True, blank=True)
    top                = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Lurnifighter Referral Badges"
        verbose_name        = "Lurnifighter Referral Badges"    


       
            
#payments
class weekly_challange(BaseFields):  
    lurnifighter_badges_id  = models.ForeignKey(lurnifighter_badges, on_delete=models.CASCADE, null=True)
    week_name               = models.CharField(max_length=50)
    week_number             = models.IntegerField(null=True,  blank=True)
    total_study_hours       = models.FloatField(null=True,    blank=True)
    total_test              = models.IntegerField(null=True,  blank=True , default=0)
    total_crowns            = models.IntegerField(null=True,  blank=True , default=0)
    refer_freinds           = models.IntegerField(null=True,  blank=True , default=0)
    test_performances       = models.FloatField(null=True,    blank=True , default=0)
    study_effectiveness     = models.IntegerField(null=True,  blank=True , default=0)

    def __str__(self):
        return str(self.week_number)

    class Meta:
        verbose_name_plural = "Weekly Challenge"
        verbose_name        = "Weekly Challenge"

class weekly_reward(BaseFields):
    weekly_challange_id     =  models.ForeignKey(weekly_challange , on_delete=models.CASCADE , null=True )
    trophy                  =  models.BooleanField(default=True)
    no_of_coins             =  models.BigIntegerField(null=True,  blank=True, default=0)
    refer_freind_coupons    =  models.IntegerField(null=True,  blank=True, default=0)
    cash_coupons_id         =  models.ManyToManyField(cash_coupons, blank=True)

    def __str__(self):
        return str(self.weekly_challange_id)

    class Meta:
        verbose_name_plural = "Weekly Reward"
        verbose_name        = "Weekly Reward"    



class test_and_study(BaseFields):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=50)
    coins = models.IntegerField(default=10)
    crowns      = models.IntegerField(default=1)


    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Create Daily Challenge Test and Study"
        verbose_name        = "Create Daily Challenge Test and Study"


class daily_challenge(BaseFields):
    test_and_study_id   = models.ManyToManyField(test_and_study , related_name='test_and_studys')
    to_day              = models.DateField()
    crown               = models.IntegerField(default=1)

    def __str__(self):
        return str(self.to_day)

    class Meta:
        verbose_name_plural = "Create Daily Challenge"
        verbose_name        = "Create Daily Challenge"   
