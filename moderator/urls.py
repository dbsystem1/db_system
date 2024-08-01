from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_home_base, name='moderator-default_home_base'),
    path('default_home/<id>', views.default_home, name='moderator-default_home'),
    path('search_user/', views.search_user, name='moderator-search_user'),
    path('filter_professor/', views.filter_professor, name='moderator-filter_professor'),
    path('edit_profile/', views.edit_profile, name='moderator-edit_profile'),
    path('show_professor_list/<id>', views.show_professor_list, name='moderator-show_professor_list'), 
    path('show_professor/<professor_id>/<address_id>/<departmant_id>/<academic_degree_id>/<theses_id>/', views.show_professor, name='moderator-show_professor'), 
    path('show_scientificJournal_list/<id>', views.show_scientificJournal_list, name='moderator-show_scientificJournal_list'),
    path('show_scientificJournal/<scientificJournal_id>', views.show_scientificJournal, name='moderator-show_scientificJournal'), 
    path('show_collection_list/<id>', views.show_collection_list, name='moderator-show_collection_list'), 
    path('show_collection/<collection_id>', views.show_collection, name='moderator-show_collection'), 
    path('show_conference_participation_list/<id>', views.show_conference_participation_list, name='moderator-show_conference_participation_list'), 
    path('show_conference_participation/<conference_participation_id>', views.show_conference_participation, name='moderator-show_conference_participation'), 
    path('show_patent_list/<id>', views.show_patent_list, name='moderator-show_patent_list'), 
    path('show_patent/<patent_id>', views.show_patent, name='moderator-show_patent'), 
    path('show_dissertation_leading_list/<id>', views.show_dissertation_leading_list, name='moderator-show_dissertation_leading_list'), 
    path('show_dissertation_leading/<dissertation_leading_id>', views.show_dissertation_leading, name='moderator-show_dissertation_leading'), 
    path('show_grant_list/<id>', views.show_grant_list, name='moderator-show_grant_list'), 
    path('show_grant/<grant_id>', views.show_grant, name='moderator-show_grant'), 
    path('show_prize_list/<id>', views.show_prize_list, name='moderator-show_prize_list'), 
    path('show_prize/<prize_id>', views.show_prize, name='moderator-show_prize'), 
    path('show_education_list/<id>', views.show_education_list, name='moderator-show_education_list'), 
    path('show_education/<education_id>', views.show_education, name='moderator-show_education'),
]