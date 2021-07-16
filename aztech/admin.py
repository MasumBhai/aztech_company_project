from django.contrib import admin
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

admin.site.unregister(Group)


# Register your models here.

# @admin.register(AboutPage)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['about_title', 'image_tag']
#     list_filter = ['about_title']
#     list_display_links = ['about_title']
#     # radio_fields = {"goods_order_status": admin.HORIZONTAL}
#     # readonly_fields = ('goods_order_id', 'buyer_id', 'goods_id', 'pub_date')
#     # search_fields = ['Field1', 'Field2']
#     list_per_page = 15
#     paginator = Paginator
#     pass


@admin.register(ContactUs)
class UserContact(admin.ModelAdmin):
    list_display = ['contact_mail', 'contact_time', 'contact_name', 'contact_phone', 'contact_msg']
    list_filter = ['contact_name']
    list_display_links = ['contact_mail']
    readonly_fields = ('contact_name', 'contact_mail', 'contact_phone', 'contact_time', 'contact_msg')
    list_per_page = 15
    paginator = Paginator
    pass


@admin.register(JobRequest)
class UserContact(admin.ModelAdmin):
    list_display = ['participant_mail', 'participant_time', 'participant_name', 'participant_phone',
                    'participant_linkedIn', 'participant_github', 'participant_msg', 'participant_resume',
                    'participant_cover_letter']
    # list_filter = ['contact_name']
    list_display_links = ['participant_mail']
    fields = ['participant_id', 'participant_name', ('participant_mail', 'participant_phone'),
              ('participant_linkedIn', 'participant_github'), ('participant_resume', 'participant_cover_letter'),
              'participant_msg']
    readonly_fields = ['participant_id', 'participant_mail', 'participant_time', 'participant_name',
                       'participant_phone',
                       'participant_linkedIn', 'participant_github', 'participant_msg', 'participant_resume',
                       'participant_cover_letter']
    list_per_page = 15
    paginator = Paginator
    pass


@admin.register(OurClients)
class ClientDetails(admin.ModelAdmin):
    list_display = ['client_id', 'client_mail', 'client_name', 'client_project_title', 'client_project_link',
                    'client_phone', 'client_address', 'client_agreement_date', 'client_payment', 'image_tag', ]
    list_filter = ['client_payment']
    list_display_links = ['client_mail']
    fields = ['client_logo', ('client_name', 'client_address'), ('client_mail', 'client_phone'),
              ('client_agreement_date', 'client_payment'), ('client_project_title', 'client_project_link'), ]
    list_per_page = 15
    paginator = Paginator
    pass


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on', 'updated_on', 'image_tag')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    fields = ['postImage', ('author', 'status'), ('created_on', 'updated_on'), 'slug', 'title', 'content', ]
    actions = ['approve_post']
    list_per_page = 10
    paginator = Paginator
    summernote_fields = ('content',)

    def approve_post(self, request, queryset):
        queryset.update(status=1)


admin.site.register(BlogPost, PostAdmin)


class CommentAdmin(SummernoteModelAdmin):
    list_display = (
        'commented_post', 'commentator_name', 'comment_posted_at', 'comment_body', 'comment_status',
        'commentator_email')
    list_filter = ('comment_status', 'comment_posted_at')
    search_fields = ('commentator_name', 'commentator_email', 'comment_body')
    actions = ['approve_comments']
    fields = ['commented_post', ('comment_posted_at', 'comment_status'), ('commentator_name', 'commentator_email'),
              'comment_body']
    list_per_page = 10
    paginator = Paginator
    summernote_fields = ('comment_body',)

    def approve_comments(self, request, queryset):
        queryset.update(comment_status=1)


admin.site.register(CommentBox, CommentAdmin)


@admin.register(LatestProjects)
class ProjectDetails(admin.ModelAdmin):
    list_display = (
        'image_tag', 'project_client', 'project_services', 'project_technologies',
        'project_challenges', 'project_uploaded_time')
    list_filter = ('project_services', 'project_client')
    search_fields = ('project_title', 'project_services', 'project_technologies',)
    fields = ['project_preview', ('project_title', 'project_uploaded_time'), ('project_client', 'project_industries'),
              ('project_services', 'project_technologies'), 'project_challenges',
              ('project_solution_pic', 'project_impact_pic'), ('project_solution', 'project_impact')]
    list_per_page = 10
    paginator = Paginator
    pass
