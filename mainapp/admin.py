from django.contrib import admin

from mainapp.models import News, Course, Lesson, CoursesTeacher, CourseFeedback

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CoursesTeacher)
admin.site.register(CourseFeedback)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # ordering = ('pk',)
    list_display = ('pk', 'title', 'deleted',)     # столбцы
    list_filter = ('deleted', 'created_at')        # фильтр
    list_per_page = 5                              # количество показываемых новостей на странице
    search_fields = ('title', 'preamble', 'body')  # поиск
    actions = ('mark_as_delete',)

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'
