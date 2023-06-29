from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    content = models.TextField(verbose_name= '내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    writer= models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    #blank값은 공백을 허용할 것인가, null값은 null값을 허용할 것인가? 
    #1대 다 관계에서는 Foreignkey를 필수로 쓰고 to 속성과 on_delete속성을 넣어줘야한다! 
    
class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일')
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)