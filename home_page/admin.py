from django.contrib import admin
from .models import Home,Studentlife,Home_features,About,Home_facility

admin.site.register(Home)
admin.site.register(Home_features)
admin.site.register(Home_facility)

admin.site.register(Studentlife)

admin.site.register(About)


# @admin.register(Materials)
# class StudentlifeAdmin(admin.StackedInline):
#     model = Studentlife

# @admin.register(Materials)
# class MaterialsAdmin(admin.ModelAdmin):
#     inlines = [Multiple_fileAdmin]

#     class Meta:
#        model = Materials

# @admin.register(Multiple_file)
# class Multiple_fileAdmin(admin.ModelAdmin):
#     pass