from django.contrib import admin
from .models import Professor
from .models import Address
from .models import Departmant
from .models import AcademicDegree
from .models import Article
from .models import Collection
from .models import Theses
from .models import Patent
from .models import Dissertation
from .models import Conference
from .models import Grant
from .models import Prize
from .models import Education
from .models import ProfessorUpdateHistory, AddressUpdateHistory, DepartmantUpdateHistory, AcademicDegreeUpdateHistory, ThesesUpdateHistory
from .models import ArticleUpdateHistory, CollectionUpdateHistory, GrantUpdateHistory, PrizeUpdateHistory, EducationUpdateHistory, ConferenceUpdateHistory, PatentUpdateHistory, DissertationUpdateHistory   


admin.site.register(ProfessorUpdateHistory)
admin.site.register(AddressUpdateHistory)
admin.site.register(DepartmantUpdateHistory)
admin.site.register(AcademicDegreeUpdateHistory)
admin.site.register(ThesesUpdateHistory)
admin.site.register(ArticleUpdateHistory)
admin.site.register(CollectionUpdateHistory)
admin.site.register(GrantUpdateHistory)
admin.site.register(PrizeUpdateHistory)
admin.site.register(EducationUpdateHistory)
admin.site.register(ConferenceUpdateHistory)
admin.site.register(PatentUpdateHistory)
admin.site.register(DissertationUpdateHistory)

admin.site.register(Professor)
admin.site.register(Address)
admin.site.register(Departmant)
admin.site.register(AcademicDegree)
admin.site.register(Article)
admin.site.register(Collection)
admin.site.register(Theses)
admin.site.register(Conference)
admin.site.register(Patent)
admin.site.register(Dissertation)
admin.site.register(Grant)
admin.site.register(Prize)
admin.site.register(Education)
