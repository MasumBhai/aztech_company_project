from django.db import models
from django.utils import timezone
from phone_field import PhoneField
from django.utils.safestring import mark_safe
from django.utils.text import slugify


# Create your models here.

class ContactUs(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=64, verbose_name='contact person\'s name')
    contact_time = models.DateTimeField(verbose_name='at Bangladesh Time')
    contact_mail = models.EmailField(max_length=120, verbose_name="contact's email address")
    contact_phone = PhoneField(verbose_name='Contact phone number')
    contact_msg = models.TextField(verbose_name="contact's message")

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
    client_logo = models.ImageField(upload_to='client_Logo/%Y/%m/%d/', blank=True, null=True,verbose_name="client image/logo")
    client_mail = models.EmailField(max_length=120, help_text="Client's email address", blank=True, null=True)
    client_phone = models.IntegerField(help_text="Client's phone number",blank=True,null=True)
    client_address = models.CharField(max_length=256, help_text="Client's Home/Office Address", blank=True, null=True)
    client_project_title = models.CharField(max_length=256, help_text="Client's Project Title We Have Done", blank=True,
                                            null=True)
    client_project_link = models.URLField(max_length=256,
                                          help_text="Github/GitLab repo link of Client work we have done", blank=True,
                                          null=True)
    client_agreement_date = models.DateTimeField(help_text="Client came to us/client's project delivery date",
                                                 blank=True, null=True)
    client_quote = models.TextField(verbose_name="Client's comment", help_text="Client's quote for us", blank=True,
                                         null=True)
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


STATUS = (
    (0, "in Draft"),
    (1, "Published")
)


class BlogPost(models.Model):
    title = models.CharField(max_length=256, verbose_name="Blog Title Info", blank=True, null=True)
    slug = models.SlugField(max_length=256, blank=True, null=True, unique=True,verbose_name="Link name(slug field)")
    author = models.EmailField(max_length=120, verbose_name="email address of Author", blank=True, null=True)
    updated_on = models.DateTimeField(verbose_name="Blog post modified Time", blank=True, null=True)
    content = models.TextField(verbose_name="Blog Content", blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name="Blog post created time")
    status = models.IntegerField(choices=STATUS, default=0)
    postImage = models.ImageField(verbose_name='Post-related-image', upload_to='blog-image/%Y/%m/%d/', blank=True,
                                  null=True)

    def image_tag(self):
        return mark_safe("<img src='/../../media/%s' width='150' height='150' />" % (self.postImage))

    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'BlogPost'
        verbose_name_plural = 'BlogPost'
        ordering = ['-created_on']
        db_table = "blogpost"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class CommentBox(models.Model):
    commented_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    commentator_name = models.CharField(max_length=120, verbose_name="name")
    commentator_email = models.EmailField(max_length=120, verbose_name="email address")
    comment_body = models.TextField(verbose_name="your thought")
    comment_posted_at = models.DateTimeField(default=timezone.now, blank=True, null=True,
                                             verbose_name="Comment posted time")
    comment_status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name = 'CommentBox'
        verbose_name_plural = 'CommentBox'
        ordering = ['-comment_posted_at']
        db_table = "commentbox"

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment_body, self.commentator_name)


class LatestProjects(models.Model):
    project_preview = models.ImageField(verbose_name='Project-slider-related-image(preview)',
                                        upload_to='project_preview/%Y/%m/', blank=True, null=True)
    project_title = models.CharField(max_length=256, help_text="Project Title", blank=True, null=True)
    project_client = models.CharField(max_length=256, help_text="Project's client descriptions", blank=True, null=True)
    project_industries = models.CharField(max_length=256, help_text="Helpful to which which industries", blank=True,
                                          null=True)
    project_services = models.CharField(max_length=256, help_text="Services provided during this project", blank=True,
                                        null=True)
    project_technologies = models.CharField(max_length=256, help_text="Technologies used in this Project", blank=True,
                                            null=True)
    project_challenges = models.TextField(
        help_text="Challenges faced to complete this project & the scope of this project", blank=True, null=True)
    project_solution = models.TextField(help_text="Broad description of what solution brings this project", blank=True,
                                        null=True)
    project_solution_pic = models.ImageField(help_text='Project-solution-related-image will be best for jpeg format',
                                             upload_to='project_solutions/%Y/%m/', blank=True, null=True)
    project_impact = models.TextField(help_text="Broad description of what impact brings this project", blank=True,
                                      null=True)
    project_impact_pic = models.ImageField(help_text='Project-impact-related-image will be best for jpeg format',
                                           upload_to='project_impacts/%Y/%m/', blank=True, null=True)
    project_uploaded_time = models.DateTimeField(verbose_name="Project uploaded time", default=timezone.now, blank=True,
                                                 null=True, help_text="Project handover/uploaded time")
    project_slug = models.SlugField(max_length=256, blank=True, null=True, unique=True)

    def image_tag(self):
        return mark_safe("<img src='/../../media/%s' width='150' height='150' />" % (self.project_preview))

    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'LatestProject'
        verbose_name_plural = 'LatestProjects'
        ordering = ['-project_uploaded_time']
        db_table = "latestprojects"

    def __str__(self):
        return "%s" % (self.project_title)

    def save(self, *args, **kwargs):
        value = self.project_title
        self.project_slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class SoftwareCompany(models.Model):
    company_logo = models.ImageField(verbose_name='Company-logo-should-be-nice',
                                     upload_to='project_impacts/%Y/%m/', blank=True, null=True)
    company_name = models.CharField(verbose_name='company-name',max_length=120,blank=True,null=True)
    company_mail = models.EmailField(verbose_name='company-official-mail-address',max_length=120,blank=True,null=True)
    company_phone = PhoneField(help_text="company-official-phone-number")
    company_address = models.CharField(verbose_name="company-office-address",max_length=256,blank=True,null=True)
    company_facebook = models.URLField(verbose_name="company-facebook-link-(if any)",blank=True,null=True)
    company_youtube = models.URLField(verbose_name="company-youtube-link-(if any)",blank=True,null=True)
    company_linkedin = models.URLField(verbose_name="company-linkedin-link-(if any)",blank=True,null=True)
    company_instagram = models.URLField(verbose_name="company-instagram-link-(if any)",blank=True,null=True)
    company_description = models.TextField(verbose_name="Company-description-why-choose-us?",blank=True,null=True)
    years_of_experiences = models.PositiveSmallIntegerField(verbose_name="years-of-experience",blank=True,null=True)
    years_of_collaborations = models.PositiveSmallIntegerField(verbose_name="years-of-collaborations-with-client",blank=True,null=True)
    clients_total_number = models.PositiveSmallIntegerField(verbose_name="total-clients-number",blank=True,null=True)
    experts_hired_total = models.PositiveSmallIntegerField(verbose_name="total-experts-hired-uptill",blank=True,null=True)
    product_delivers_total = models.PositiveSmallIntegerField(verbose_name="total-product-delivered-uptill",blank=True,null=True)

    def image_tag(self):
        return mark_safe("<img src='/../../media/%s' width='150' height='150' />" % (self.company_logo))

    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'SoftwareCompany'
        verbose_name_plural = 'SoftwareCompany'
        db_table = "softwarecompany"

    def __str__(self):
        return "%s" % (self.company_mail)
