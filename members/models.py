from django.db import models
from io import BytesIO
from django.core.files.uploadedfile import  File
from PIL import Image , ImageDraw
import qrcode


class member_type(models.Model):
    type_name        = models.CharField(max_length=50)
    
    def __str__(self):
        return self.type_name
    class Meta:
        verbose_name_plural = "Lur nify Member Types"
        verbose_name =  "Lurnify Member Types"

class lurnify_member(models.Model):
    account_id  = models.ForeignKey('accounts.Account', on_delete=models.SET_NULL, null=True)
    phone       = models.CharField(max_length=15, blank=True, null=True)
    name        = models.CharField(max_length=50)
    member_type = models.ForeignKey(member_type, 
                                on_delete=models.SET_NULL, blank=True, null=True)
    address     = models.CharField(max_length=50, blank=True, null=True)
    state       = models.CharField(max_length=50, blank=True, null=True)
    city        = models.CharField(max_length=50, blank=True, null=True)
    pincode     = models.CharField(max_length=50, blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)                        
    
    class Meta:
        verbose_name_plural = "Lurnify Members"
        verbose_name = "Lurnify Member"
    
    def __str__(self):
        return self.name

class Bank_detail(models.Model):
    lurnify_member_id   = models.ForeignKey(lurnify_member, on_delete=models.SET_NULL, null=True)
    bank_name           = models.CharField(max_length=50)
    branch_name         = models.CharField(max_length=50)
    ifsc_code           = models.CharField(max_length=50)
    account_no          = models.CharField(max_length=50)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Lurnify Member Bank Details"
        verbose_name = "Lurnify Member"
        unique_together = ('lurnify_member_id', 'bank_name', 'branch_name', 'ifsc_code', 'account_no')
    
    def __str__(self):
        return self.bank_name

    # withdrwal condition 
    # above 10 ,000
    # in 30 days    

class referal_code(models.Model):
    lurnify_member_id   = models.ForeignKey(lurnify_member, on_delete=models.SET_NULL, null=True)
    qr_code_number      = models.CharField(max_length=10,null=True,blank=True , unique=True)
    qr_code             = models.ImageField(upload_to='qr_code', null=True, blank=True)
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
    