from django.contrib import admin
from .models import Plant
admin.site.register(Plant)

from .models import Prediction
admin.site.register(Prediction)


from .models import Contact
admin.site.register(Contact)

admin.site.site_header = "LeafLab Admin Portal"
admin.site.site_title = "LeafLab Admin Portal"
admin.site.index_title = "Welcome To LeafLab Admin Portal"