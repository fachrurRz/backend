from django.contrib import admin

# Register your models here.
from website.models import (
    ElementWord, Event, Task,
    Submission, Post, Comment,
    PostType,
    Album, TaskStatistic,
    EventStatistic, UserStatistic,
    Vote, VoteOption, Voting, QnA,
    TaskScore,
)


class ElementWordModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'testimony', 'approved')
    list_filter = ('approved', )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser == True:
            return ()
        return ('author', 'testimony')

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = ElementWord


class EventModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'start_time', 'end_time')

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = Event


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_kenalan')
    list_filter = ('is_kenalan',)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = Task


class TaskScoreModelAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'name', 'task', 'score', 'comment')
    search_fields = ('user__profile__name',)

    def user_profile(self, obj):
        return obj.user.profile.name

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = TaskScore


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'summary', 'content', 
                    'cover_image_link', 'attachment_link', 'post_type')
    list_filter = ('post_type',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = Post


class SubmissionModelAdmin(admin.ModelAdmin):
    list_display = ('task_and_user', 'user_profile', 'task', 'file_link',
                    'is_checked', 'is_approved', 'created_at', 'updated_at')
    list_filter = ('task', 'is_checked', 'is_approved')
    search_fields = ('user__profile__name', 'task__id', 'user__id')

    def task_and_user(self, obj):
        return str(obj.task.id) + ' ' + str(obj.user.id)
    def user_profile(self, obj):
        return obj.user.profile

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser == True:
            return ()
        return ('file_link', 'user_profile', 'task',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = Submission


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment')

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = Comment


class PostTypeModelAdmin(admin.ModelAdmin):
    list_display = ('post_type',)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = PostType


class AlbumModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'album_link')

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = Album


class TaskStatisticModelAdmin(admin.ModelAdmin):
    list_display = ('task', 'amount')

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = TaskStatistic


class EventStatisticModelAdmin(admin.ModelAdmin):
    list_display = ('event', 'attendee', 'on_time', 'late', 'permission', 'absent')

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = EventStatistic


class UserStatisticModelAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'name', 'task', 'amount_total', 'amount_approved_total',)
    search_fields = ('user__profile__name',)

    def user_profile(self, obj):
        return obj.user.profile.name

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = UserStatistic


class VoteOptionInline(admin.StackedInline):
    list_display = ('name', 'description', 'total_voters',)
    model = VoteOption

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False


class VoteModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'total_voters', 'start_time', 'end_time')
    search_fields = ('title',)
    inlines = [
        VoteOptionInline,
    ]

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = Vote

class QnAModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment')

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = QnA

admin.site.register(ElementWord, ElementWordModelAdmin)
admin.site.register(Event, EventModelAdmin)
admin.site.register(Task, TaskModelAdmin)
admin.site.register(TaskScore, TaskScoreModelAdmin)
admin.site.register(Submission, SubmissionModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
admin.site.register(PostType, PostTypeModelAdmin)
admin.site.register(Album, AlbumModelAdmin)
admin.site.register(TaskStatistic, TaskStatisticModelAdmin)
admin.site.register(EventStatistic, EventStatisticModelAdmin)
admin.site.register(UserStatistic, UserStatisticModelAdmin)
admin.site.register(Vote, VoteModelAdmin)
admin.site.register(Voting)
admin.site.register(QnA, QnAModelAdmin)