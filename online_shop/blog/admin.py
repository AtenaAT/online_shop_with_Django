from django.contrib import admin
from .models import Post


def make_published(modeladmin, request,queryset):
    result=queryset.update(post_status='published')
    if result ==1:
        message_bit= "The post was"
    else:
        message_bit="{} posts were".format(result)
    modeladmin.message_user(request, "{} published successfully".format(message_bit))

make_published.short_description= 'publish selected post'
#--------------------------------------------------------------------------------------------------
#draft
def make_draft(modeladmin, request, queryset):
    result= queryset.update(post_status='draft')
    if result ==1:
        message_bit='The post was'
    else:
        message_bit='{} posts were'.format(result)
    modeladmin.message_user(request, "{} draft successfully".format(message_bit))

make_draft.short_description= 'draft selected post'
#-------------------------------------------------------------------------------------------------
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ('post_title','post_Slug','post_published','post_status' )
    prepopulated_fields= {'post_Slug':('post_title',)}
    list_filter=('post_published','post_status')
    search_fields= ('post_title','post_descripton')
    actions= [make_published, make_draft ]
