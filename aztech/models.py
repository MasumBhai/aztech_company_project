from django.db import models

# Create your models here.
class aboutpage(models.Model):
    about_id = models.AutoField(primary_key=True)
    about_title = models.CharField(max_length=256,help_text='About Page Title',default='We Care,We Excel')
    about_pic = models.ImageField(upload_to='images/', blank=True, null=True)
    # about_something = models.TextField(blank=True,null=True,max_length=256,help_text='intro of about page')


    class Meta:
        # verbose_name = 'aboutpage'
        # verbose_name_plural = 'abouts'
        # ordering = ['user_id']
        db_table = 'aboutpage'

    def __str__(self):
        return "%s" % (self.about_title)


