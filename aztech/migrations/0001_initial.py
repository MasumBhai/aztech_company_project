# Generated by Django 3.2.4 on 2021-07-15 20:12

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('about_id', models.AutoField(primary_key=True, serialize=False)),
                ('about_title', models.CharField(default='We Care,We Excel', help_text='About Page Title', max_length=256)),
                ('about_pic', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'db_table': 'aboutpage',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_name', models.CharField(help_text="contact's name", max_length=64)),
                ('contact_time', models.DateTimeField(help_text='Local BanglDesh Time')),
                ('contact_mail', models.EmailField(help_text="contact's email address", max_length=120)),
                ('contact_phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31)),
                ('contact_msg', models.TextField(help_text="contact's message")),
            ],
            options={
                'verbose_name': 'ContactUs',
                'verbose_name_plural': 'ContactUs',
                'db_table': 'contact',
                'ordering': ['-contact_time'],
            },
        ),
        migrations.CreateModel(
            name='JobRequest',
            fields=[
                ('participant_id', models.AutoField(primary_key=True, serialize=False)),
                ('participant_name', models.CharField(help_text="participant's name", max_length=64)),
                ('participant_time', models.DateTimeField(help_text='Local BanglDesh Time')),
                ('participant_mail', models.EmailField(help_text="participant's email address", max_length=120)),
                ('participant_phone', phone_field.models.PhoneField(help_text="participant's phone number", max_length=31)),
                ('participant_linkedIn', models.URLField(blank=True, help_text="participant's Linkedin Profile Link", null=True, verbose_name='LinkidIn-Id')),
                ('participant_github', models.URLField(blank=True, help_text="participant's Github Profile Link", null=True, verbose_name='Github-Id')),
                ('participant_msg', models.TextField(help_text="participant's msg to get job")),
                ('participant_resume', models.FileField(blank=True, null=True, upload_to='resume/%Y/%m/%d/', verbose_name='Resume')),
                ('participant_cover_letter', models.FileField(blank=True, null=True, upload_to='cover-letter/%Y/%m/%d/', verbose_name='Cover-Letter')),
            ],
            options={
                'verbose_name': 'JobRequest',
                'verbose_name_plural': 'JobRequest',
                'db_table': 'jobrequest',
                'ordering': ['-participant_time'],
            },
        ),
        migrations.CreateModel(
            name='OurClients',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(blank=True, help_text="Client's individual name or Company name", max_length=256, null=True)),
                ('client_logo', models.ImageField(blank=True, null=True, upload_to='client_Logo/%Y/%m/%d/')),
                ('client_mail', models.EmailField(blank=True, help_text="Client's email address", max_length=120, null=True)),
                ('client_phone', models.IntegerField(blank=True, help_text="Client's phone number", null=True)),
                ('client_address', models.CharField(blank=True, help_text="Client's Home/Office Address", max_length=256, null=True)),
                ('client_project_title', models.CharField(blank=True, help_text="Client's Project Title We Have Done", max_length=256, null=True)),
                ('client_project_link', models.URLField(blank=True, help_text='Github/GitLab repo link of Client work we have done', max_length=256, null=True)),
                ('client_agreement_date', models.DateTimeField(blank=True, help_text="Client came to us/client's project delivery date", null=True)),
                ('client_payment', models.IntegerField(blank=True, help_text="Client's paid amount", null=True, verbose_name="Client's Payment")),
            ],
            options={
                'verbose_name': 'OurClients',
                'verbose_name_plural': 'OurClients',
                'db_table': 'ourclients',
                'ordering': ['-client_id'],
            },
        ),
    ]
