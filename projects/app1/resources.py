from import_export import resources, widgets
from import_export.fields import Field
from .models import Student_Details, Marklist

class Table1Resource(resources.ModelResource):
    class Meta:
        model = Student_Details

class studentResource(resources.ModelResource):
    field2 = Field(attribute='field2', widget=widgets.ForeignKeyWidget(Student_Details, 'pk'))

    class Meta:
        model = Marklist
        skip_unchanged = True
        report_skipped = True
        fields = ('studentdetails','Semester','Mark')
