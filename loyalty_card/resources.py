from import_export import resources
from .models import *

class CCKResource(resources.ModelResource):
    class Meta:
        model = CCK
        import_id_fields = ['student_id']

class SheetResource(resources.ModelResource):
    class Meta:
        model = Sheet
        import_id_fields = ['student_id']

class GithubResource(resources.ModelResource):
    class Meta:
        model = Github
        import_id_fields = ['student_id']

class MachiResource(resources.ModelResource):
    class Meta:
        model = Machi
        import_id_fields = ['student_id']

class HotpotResource(resources.ModelResource):
    class Meta:
        model = Hotpot
        import_id_fields = ['student_id']

