from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget


from .models import Publisher, Book, Buyer, Order

# Register your models here.


class BookResource(resources.ModelResource):
    school = fields.Field(column_name='publisher_name',
                          attribute='publisher',
                          widget=ForeignKeyWidget(Publisher, 'name'))

    class Meta:
        model = Book
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'title', 'publisher_name', 'link', 'author', 'suply', 'edition', 'year_of_publication',
                  'price_foreign_currency', 'price_indian_currency', 'ISBN', 'discount', 'expected_price', 'description', 'subject',)


class BookAdmin(ImportExportActionModelAdmin):
    resource_class = BookResource

    pass


admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Buyer)
admin.site.register(Order)
