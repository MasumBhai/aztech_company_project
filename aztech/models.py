from django.db import models
from phone_field import PhoneField
from django.utils.safestring import mark_safe

# Create your models here.
class AboutPage(models.Model):
    about_id = models.AutoField(primary_key=True)
    about_title = models.CharField(max_length=256,help_text='About Page Title',default='We Care,We Excel')
    about_pic = models.ImageField(upload_to='images/', blank=True, null=True)
    # about_something = models.TextField(blank=True,null=True,max_length=256,help_text='intro of about page')

    def image_tag(self):
        return mark_safe("<img src='media/images/%s' width='150' height='150' />" % (self.about_pic))

    image_tag.allow_tags = True

    class Meta:
        # verbose_name = 'aboutpage'
        # verbose_name_plural = 'abouts'
        # ordering = ['user_id']
        db_table = 'aboutpage'

    def __str__(self):
        return "%s" % (self.about_title)

class ContactUs(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=64,help_text='contact\'s name')
    contact_time = models.DateTimeField(help_text='Local BanglDesh Time')
    contact_mail = models.EmailField(max_length=120,help_text="contact's email address")
    contact_phone = PhoneField(help_text='Contact phone number')
    contact_msg = models.TextField(help_text="contact's message")

    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'
        ordering = ['-contact_time']  # from top to bottom
        db_table = 'contact'

    def __str__(self):
        return "%s" % (self.contact_mail)







