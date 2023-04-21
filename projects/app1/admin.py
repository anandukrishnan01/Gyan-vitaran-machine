from django.contrib import admin
from .models import Marklist,Student_Details,ImageConverter
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.admin import ImportExportMixin
from .resources import studentResource
# Register your models here.

admin.site.register(ImageConverter)


class Studentdata(resources.ModelResource):

    class Meta:
        model = Student_Details

    def __init__(self, form_fields=None):
        super().__init__()
        self.form_fields = form_fields

    def get_export_fields(self):
        return [self.fields[f] for f in self.form_fields]



@admin.register(Student_Details)
class studentdetail(admin.ModelAdmin):
    pass

@admin.register(Marklist)
class collegeadmin(ImportExportModelAdmin):
    resource_class = studentResource
    list_display = ('studentdetails','Semester','Mark')
    list_filter = ('studentdetails','Semester','Mark')

