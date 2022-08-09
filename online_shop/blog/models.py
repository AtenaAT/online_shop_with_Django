from django.db import models
from django.utils import timezone

class Post(models.Model):
    status_choice=(
        ('published','منتشر شده'),
        ('draft', 'Draft')
    )
    post_title= models.CharField(max_length= 80, verbose_name= 'عنوان')
    post_Slug= models.SlugField(max_length=100, verbose_name= 'slug')
    post_descripton= models.TextField(verbose_name= 'توضیحات پست')
    post_created= models.DateTimeField(auto_now_add= True)
    post_updated= models.DateTimeField(auto_now= True)
    post_status= models.CharField(max_length=80, choices=status_choice, default='draft', verbose_name= 'وضعیت')
    post_published= models.DateTimeField(default=timezone.now, verbose_name= 'انتشار پست')


    class Meta:
        verbose_name= 'پست'
        verbose_name_plural= 'پست ها'

    def __str__(self):
        return self.post_title