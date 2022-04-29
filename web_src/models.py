from django.db import models
from accounts.models import *
from tinymce.models import HTMLField
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=255)
    dream = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class hero_section(BaseFields):
    title = models.CharField(max_length=200)
    description = HTMLField(null=True,blank=True)
    btn_text = models.CharField(max_length=200)
    btn_link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hero_section/',null=True,blank=True)

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Section'
    def ImageUrl(self):
        return self.image.url
    def __str__(self):
        return self.title

class feature_section(BaseFields):
    s_no = models.IntegerField(default=0)
    icon = models.CharField(max_length=200,null=True,blank=True)
    heading = models.CharField(max_length=200)
    description = HTMLField(null=True,blank=True)
    class Meta:
        verbose_name = 'Feature Section'
        verbose_name_plural = 'Feature Section'
    def __str__(self):
        return str(self.s_no) + ' ' + str(self.heading)

class video_section(BaseFields):
    title = models.CharField(max_length=200)
    img_1 = models.ImageField(upload_to='video_section/',null=True,blank=True)
    img_1_alt = models.CharField(max_length=200,null=True,blank=True)
    img_2 = models.ImageField(upload_to='video_section/',null=True,blank=True)
    img_2_alt = models.CharField(max_length=200,null=True,blank=True)
    img_3 = models.ImageField(upload_to='video_section/',null=True,blank=True)
    img_3_alt = models.CharField(max_length=200,null=True,blank=True)
    video_link = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Video Section'
        verbose_name_plural = 'Video Section'
    def Img_1 (self):
        return self.img_1.url
    def Img_2 (self):
        return self.img_2.url
    def Img_3 (self):
        return self.img_3.url
    def __str__(self):
        return self.title

class growth_section(BaseFields):
    heading = models.CharField(max_length=200)
    btn_1_text = models.CharField(max_length=200)
    btn_1_link = models.CharField(max_length=200)
    btn_2_text = models.CharField(max_length=200)
    btn_2_link = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Growth Section'
        verbose_name_plural = 'Growth Section'
    def __str__(self):
        return self.heading

class growth_section_data(BaseFields):
    heading = models.CharField(max_length=200)
    description = HTMLField(null=True,blank=True)
    icon = models.CharField(max_length=200,null=True,blank=True)
    class Meta:
        verbose_name = 'Growth Section Data'
        verbose_name_plural = 'Growth Section Data'
    def __str__(self):
        return self.heading


class steps_section(BaseFields):
    heading = models.CharField(max_length=200)
    btn_1_text = models.CharField(max_length=200)
    btn_1_link = models.CharField(max_length=200)
    btn_2_text = models.CharField(max_length=200)
    btn_2_link = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Steps Section'
        verbose_name_plural = 'Steps Section'
    def __str__(self):
        return self.heading

class steps(BaseFields):
    top_heading = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)
    description = HTMLField(null=True,blank=True)
    image = models.ImageField(upload_to='steps/',null=True,blank=True)
    img_alt = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Steps'
        verbose_name_plural = 'Steps'
    def ImageUrl(self):
        return self.image.url
    def __str__(self):
        return self.top_heading

class testimonial_section(BaseFields):
    heading = models.CharField(max_length=200)
    no_of_testimonial = models.IntegerField(default=0)
    description     = models.TextField(null=True,blank=True)
    class Meta:
        verbose_name = 'Testimonial Section'
        verbose_name_plural = 'Testimonial Section'
    def __str__(self):
        return self.heading

class testimonials (BaseFields):
    s_no = models.IntegerField(default=0,null=True,blank=True)
    name = models.CharField(max_length=200)
    testimonial = models.TextField(null=True,blank=True)
    rank       = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='testimonials/',null=True,blank=True)
    img_alt = models.CharField(max_length=200,null=True,blank=True)
    class Meta:
        verbose_name = 'Testimonials'
        verbose_name_plural = 'Testimonials'
    def ImageUrl(self):
        return self.image.url
    def __str__(self):
        return self.name

class faq_section(BaseFields):
    heading = models.CharField(max_length=200)
    description = HTMLField(null=True,blank=True)
    image = models.ImageField(upload_to='faq_section/',null=True,blank=True)
    img_alt = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'FAQ Section'
        verbose_name_plural = 'FAQ Section'
    def ImageUrl(self):
        return self.image.url
    def __str__(self):
        return self.heading
class faq (BaseFields):
    question = models.CharField(max_length=200)
    answer = HTMLField(null=True,blank=True)
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
    def __str__(self):
        return self.question

class pricing_section(BaseFields):
    heading = models.CharField(max_length=200)
    description = HTMLField(null=True,blank=True)
    class Meta:
        verbose_name = 'Pricing Section'
        verbose_name_plural = 'Pricing Section'
    def __str__(self):
        return self.heading

class pricing_table(BaseFields):
    course_name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    features = HTMLField(null=True,blank=True)
    btn_text = models.CharField(max_length=200)
    btn_link = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Pricing Table'
        verbose_name_plural = 'Pricing Table'
    def __str__(self):
        return self.course_name


class showcase_section(BaseFields):
    heading = models.CharField(max_length=200)
    description = HTMLField(null=True,blank=True)
    class Meta:
        verbose_name = 'Showcase Section'
        verbose_name_plural = 'Showcase Section'
    def __str__(self):
        return self.heading

class showcase_section_data(BaseFields):
    heading = models.CharField(max_length=200)
    description = HTMLField(null=True,blank=True)
    image = models.ImageField(upload_to='showcase_section/',null=True,blank=True)
    img_alt = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Showcase Section Data'
        verbose_name_plural = 'Showcase Section Data'
    def ImageUrl(self):
        return self.image.url
    def __str__(self):
        return self.heading

class contact_section(BaseFields):
    heading = models.CharField(max_length=200)
    description = HTMLField(null=True,blank=True)
    btn_text = models.CharField(max_length=200)
    btn_link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='contact_section/',null=True,blank=True)
    img_alt = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Contact Section'
        verbose_name_plural = 'Contact Section'
    def __str__(self):
        return self.heading


class footer_section(BaseFields):
    heading = models.CharField(max_length=200)
    description = HTMLField(null=True,blank=True)
    class Meta:
        verbose_name = 'Footer Section'
        verbose_name_plural = 'Footer Section'
    def __str__(self):
        return self.heading

WIDGET_CHOICES = (
    ('about_us', 'About Us'),
    ('menu', 'Menu'),
    ('contact_us', 'Contact Us'),
    ('social_media', 'Social Media'),
    ('footer', 'Footer')
)

class menu(BaseFields):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
    def __str__(self):
        return self.name

class menu_data(BaseFields):
    name = models.CharField(max_length=200,null=True,blank=True)
    link = models.CharField(max_length=200,null=True,blank=True)
    icon = models.CharField(max_length=200,null=True,blank=True)
    icon_class = models.CharField(max_length=200,null=True,blank=True)
    menu = models.ForeignKey(menu,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
    def __str__(self):
        return str(self.name) + ' - ' + str(self.menu.name)

class privacy_policy(BaseFields):
    heading = models.CharField(max_length=200)
    description = HTMLField(null=True,blank=True)
    slug = models.CharField(max_length=50 ,null=True,blank=True )
    class Meta:
        verbose_name = 'Privacy Policy'
        verbose_name_plural = 'Privacy Policy'
    def __str__(self):
        return self.heading

class footer_widget(BaseFields):
    widget_type = models.CharField(max_length=200, choices=WIDGET_CHOICES)
    heading_text = models.CharField(max_length=200)
    description = HTMLField(null=True,blank=True)
    heading_img = models.ImageField(upload_to='footer_widget/',null=True,blank=True)
    heading_img_alt = models.CharField(max_length=200)
    menu = models.ForeignKey(menu,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        verbose_name = 'Footer Widget'
        verbose_name_plural = 'Footer Widget'
    def __str__(self):
        return self.heading