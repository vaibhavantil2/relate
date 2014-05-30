from django.contrib import admin
from course.models import (Course, Participation, InstantFlowRequest,
        FlowVisit, FlowGroupVisit, FlowPage)


class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)


class ParticipationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Participation, ParticipationAdmin)


class InstantFlowRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(InstantFlowRequest, InstantFlowRequestAdmin)


class FlowGroupVisitAdmin(admin.ModelAdmin):
    pass

admin.site.register(FlowGroupVisit, FlowGroupVisitAdmin)
