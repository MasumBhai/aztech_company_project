from django.db import models
from phone_field import PhoneField
from django.utils.safestring import mark_safe


# Create your models here.
class AboutPage(models.Model):
    about_id = models.AutoField(primary_key=True)
    about_title = models.CharField(max_length=256, help_text='About Page Title', default='We Care,We Excel')
    about_pic = models.ImageField(upload_to='images/', blank=True, null=True)

    # about_something = models.TextField(blank=True,null=True,max_length=256,help_text='intro of about page')

    def image_tag(self):
        return mark_safe("<img src='/../../media/%s' width='150' height='150' />" % (self.about_pic))

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
    contact_name = models.CharField(max_length=64, help_text='contact\'s name')
    contact_time = models.DateTimeField(help_text='Local BanglDesh Time')
    contact_mail = models.EmailField(max_length=120, help_text="contact's email address")
    contact_phone = PhoneField(help_text='Contact phone number')
    contact_msg = models.TextField(help_text="contact's message")

    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'
        ordering = ['-contact_time']  # from top to bottom
        db_table = 'contact'

    def __str__(self):
        return "%s" % (self.contact_mail)


class JobRequest(models.Model):
    participant_id = models.AutoField(primary_key=True)
    participant_name = models.CharField(max_length=64, help_text="participant's name")
    participant_time = models.DateTimeField(help_text="Local BanglDesh Time")
    participant_mail = models.EmailField(max_length=120, help_text="participant's email address")
    participant_phone = PhoneField(help_text="participant's phone number")
    participant_linkedIn = models.URLField(verbose_name="LinkidIn-Id", max_length=200,
                                           help_text="participant's Linkedin Profile Link", blank=True, null=True)
    participant_github = models.URLField(verbose_name="Github-Id", max_length=200,
                                         help_text="participant's Github Profile Link", blank=True, null=True)
    participant_msg = models.TextField(help_text="participant's msg to get job")
    participant_resume = models.FileField(verbose_name='Resume', upload_to='resume/%Y/%m/%d/', blank=True, null=True)
    participant_cover_letter = models.FileField(verbose_name='Cover-Letter', upload_to='cover-letter/%Y/%m/%d/',
                                                blank=True, null=True)

    class Meta:
        verbose_name = 'JobRequest'
        verbose_name_plural = 'JobRequest'
        ordering = ['-participant_time']  # from top to bottom
        db_table = 'jobrequest'

    def __str__(self):
        return "%s" % (self.participant_id)


class OurClients(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=256, help_text="Client's individual name or Company name", blank=True,
                                   null=True)
    client_logo = models.ImageField(upload_to='client_Logo/%Y/%m/%d/', blank=True, null=True)
    client_mail = models.EmailField(max_length=120, help_text="Client's email address", blank=True, null=True)
    client_phone = models.IntegerField(help_text="Client's phone number", blank=True, null=True)
    client_address = models.CharField(max_length=256, help_text="Client's Home/Office Address", blank=True, null=True)
    client_project_title = models.CharField(max_length=256, help_text="Client's Project Title We Have Done", blank=True,
                                            null=True)
    client_project_link = models.URLField(max_length=256,
                                          help_text="Github/GitLab repo link of Client work we have done", blank=True,
                                          null=True)
    client_agreement_date = models.DateTimeField(help_text="Client came to us/client's project delivery date",
                                                 blank=True, null=True)
    client_payment = models.IntegerField(verbose_name="Client's Payment", help_text="Client's paid amount", blank=True,
                                         null=True)
    def image_tag(self):
        return mark_safe("<img src='/../../media/%s' width='150' height='150' />" % (self.client_logo))

    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'OurClients'
        verbose_name_plural = 'OurClients'
        ordering = ['-client_id']  # from top to bottom
        db_table = 'ourclients'

    def __str__(self):
        return "%s" % (self.client_id)
