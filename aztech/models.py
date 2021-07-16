from django.db import models
from django.utils import timezone
from phone_field import PhoneField
from django.utils.safestring import mark_safe
from django.utils.text import slugify


# Create your models here.
# class AboutPage(models.Model):
#     about_id = models.AutoField(primary_key=True)
#     about_title = models.CharField(max_length=256, help_text='About Page Title', default='We Care,We Excel')
#     about_pic = models.ImageField(upload_to='images/', blank=True, null=True)
#
#     # about_something = models.TextField(blank=True,null=True,max_length=256,help_text='intro of about page')
#
#     def image_tag(self):
#         return mark_safe("<img src='/../../media/%s' width='150' height='150' />" % (self.about_pic))
#
#     image_tag.allow_tags = True
#
#     class Meta:
#         # verbose_name = 'aboutpage'
#         # verbose_name_plural = 'abouts'
#         # ordering = ['user_id']
#         db_table = 'aboutpage'
#
#     def __str__(self):
#         return "%s" % (self.about_title)


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


STATUS = (
    (0, "in Draft"),
    (1, "Published")
)


class BlogPost(models.Model):
    title = models.CharField(max_length=256, help_text="Blog Title Info", blank=True, null=True)
    slug = models.SlugField(max_length=256, blank=True, null=True, unique=True)
    author = models.EmailField(max_length=120, help_text="Author is email address holder", blank=True, null=True)
    updated_on = models.DateTimeField(help_text="Blog post modified Time", blank=True, null=True)
    content = models.TextField(help_text="Blog Content", blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now, blank=True, null=True, help_text="Blog post created time")
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
    commentator_name = models.CharField(max_length=120, help_text="Commentator's name")
    commentator_email = models.EmailField(max_length=120, help_text="Commentator's email address")
    comment_body = models.TextField(help_text="Comments Content")
    comment_posted_at = models.DateTimeField(default=timezone.now, blank=True, null=True,
                                             help_text="Comment created time")
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
    project_solution_pic = models.ImageField(verbose_name='Project-solution-related-image must be in jpeg format',
                                             upload_to='project_solutions/%Y/%m/', blank=True, null=True)
    project_impact = models.TextField(help_text="Broad description of what impact brings this project", blank=True,
                                      null=True)
    project_impact_pic = models.ImageField(verbose_name='Project-impact-related-image must be in jpeg format',
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


# class SoftwareFarm(models.Model):
#     company_logo = models.ImageField(verbose_name='Company-logo-should-be-nice',
#                                      upload_to='project_impacts/%Y/%m/', blank=True, null=True)
#     years_of_experiences = models.PositiveSmallIntegerField(verbose_name="years-of-experience",blank=True,null=True)
#     years_of_collaborations = models.PositiveSmallIntegerField(verbose_name="years-of-collaborations-with-client",blank=True,null=True)
#     clients_total_number = models.PositiveSmallIntegerField(verbose_name="total-clients-number",blank=True,null=True)
#     experts_hired_total = models.PositiveSmallIntegerField(verbose_name="total-experts-hired-uptill",blank=True,null=True)
#     product_delivers_total = models.PositiveSmallIntegerField(verbose_name="total-product-delivered-uptill",blank=True,null=True)
#
#     def image_tag(self):
#         return mark_safe("<img src='/../../media/%s' width='150' height='150' />" % (self.company_logo))
#
#     image_tag.allow_tags = True
