from django.contrib import admin

from myblogs.models import Post_messages,User_messages

class User_Admin(admin.ModelAdmin):
    list_display=['name','password','qq','register_date']
admin.site.register(User_messages,User_Admin)
class Post_Admin(admin.ModelAdmin):
    list_display=['username','title','pub_date']
admin.site.register(Post_messages,Post_Admin)
