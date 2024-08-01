from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.models import User
from user.profileForm import ProfileForm
from django.utils.datastructures import MultiValueDictKeyError

from user.models import Professor, AcademicDegree, Address, Prize, Article, Collection, Departmant, Theses, Conference, Dissertation, Grant, Patent, Education
from user.IndividualQuestionnaireForm import ProfessorForm, AcademicDegreeForm, AddressForm, DepartmantForm, ThesesForm
from user.scientificJournalForm import ArticleForm
from user.collectionForm import CollectionForm
from user.conferenceParticipationForm import ConferenceParticipationForm
from user.patentForm import PatentForm
from user.dissertationForm import DissertationForm
from user.grantForm import GrantForm
from user.prizeForm import PrizeForm 
from user.educationForm import EducationForm
from django.shortcuts import get_object_or_404

from .filters import ProfessorDegreeFilterForm
from datetime import date
from datetime import datetime, timedelta
from django.db.models.functions import ExtractYear
from django.contrib.auth import login, logout
from django.db.models import Q

@never_cache
def default_home_base(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    return render(request, 'moderator/default_home_base.html')

@never_cache
def default_home(request, id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    
    user = get_object_or_404(User, id=id)
    return render(request, 'moderator/default_home.html', {'user': user})

@never_cache
def edit_profile(request):  
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    
    current_user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()        
            return redirect('user-update_success') # Redirect to login page after successful registration
    else:
        form = ProfileForm(instance=current_user)
    
    return render(request, 'moderator/edit_profile.html', {'form': form})

@never_cache
def search_user(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    if request.method == "POST":
        try:
            searched = request.POST.get('searched', '')
            words = searched.split()
            professors = Professor.objects.all()
            users = User.objects.all()
            if len(words) >= 2:
                professors = professors.filter(
                    Q(first_name__icontains=words[0], last_name__icontains=words[1]) |
                    Q(first_name__icontains=words[1], last_name__icontains=words[0])
                )
                if not professors.exists():
                    professors = None
            elif len(words) == 1:
                professors = professors.filter(
                    Q(first_name__icontains=words[0]) | 
                    Q(last_name__icontains=words[0]) |
                    Q(user__username__icontains=words[0])
                )
                users = users.filter(
                    Q(username__icontains=words[0])
                )
                if not professors.exists():
                    professors = None
                if not users.exists():
                    users = None
        except MultiValueDictKeyError:
            searched = ''  # Default value if 'searched' key is not found
        return render(request, 'moderator/search_user.html', {'searched': searched, 'professors': professors, 'users': users})
    
    return render(request, 'moderator/search_user.html')

def filter_professor(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    
    form = ProfessorDegreeFilterForm(request.GET)
    professors = Professor.objects.all()
    filtered_data = []
    users_not_professors = None
    flag = False

    if request.GET:  
        if form.is_valid():
            professor_first_name = form.cleaned_data.get('professor_first_name')
            professor_last_name = form.cleaned_data.get('professor_last_name')          
            professor_patronomic = form.cleaned_data.get('professor_patronomic')
            professor_membership_of_RA_NAS = form.cleaned_data.get('professor_membership_of_RA_NAS')
            professor_gender = form.cleaned_data.get('professor_gender')
            professor_position = form.cleaned_data.get('professor_position')
            professor_domain = form.cleaned_data.get('professor_domain')
            professor_smaller_age = form.cleaned_data.get('professor_smaller_age')
            professor_bigger_age = form.cleaned_data.get('professor_bigger_age') 
            degree_science = form.cleaned_data.get('degree_science')
            degree_degree = form.cleaned_data.get('degree_degree')
            professor_work_time = form.cleaned_data.get('professor_work_time')
            filtered_data = AcademicDegree.objects.select_related('professor', 'user')

            flag2 = False

            if professor_first_name:
                filtered_data = filtered_data.filter(professor__first_name=professor_first_name)
                flag2 = True
            if professor_last_name:
                filtered_data = filtered_data.filter(professor__last_name=professor_last_name)
                flag2 = True
            if professor_patronomic:
                filtered_data = filtered_data.filter(professor__patronomic=professor_patronomic)
                flag2 = True
            if professor_membership_of_RA_NAS:
                filtered_data = filtered_data.filter(professor__membership_of_RA_NAS=professor_membership_of_RA_NAS)
                flag2 = True
            if professor_gender:
                filtered_data = filtered_data.filter(professor__gender=professor_gender)
                flag2 = True
            if professor_position:
                filtered_data = filtered_data.filter(professor__position=professor_position)
                flag2 = True
            if professor_work_time:
                filtered_data = filtered_data.filter(professor__work_time=professor_work_time)
                flag2 = True  
            if professor_domain:
                filtered_data = filtered_data.filter(professor__domain=professor_domain)
                flag2 = True
            if professor_smaller_age:
                birth_date_filter = datetime.now() - timedelta(days=365.25 * professor_smaller_age) - timedelta(365)
                filtered_data = filtered_data.filter(professor__birth_date__gte=birth_date_filter) #poqr
                flag2 = True
            if professor_bigger_age:
                birth_date_filter = datetime.now() - timedelta(days=365.25 * professor_bigger_age) - timedelta(365)
                filtered_data = filtered_data.filter(professor__birth_date__lte=birth_date_filter) #մե
                flag2 = True
            if degree_science:
                filtered_data = filtered_data.filter(science=degree_science)
                flag2 = True
            if degree_degree:
                filtered_data = filtered_data.filter(degree=degree_degree)            
                flag2 = True

            if not flag2:
                filtered_data = None

    else:
        flag = True

    users_not_professors = User.objects.exclude(professor__isnull=False)

    return render(request, 'moderator/filter_professor.html', {'form': form, 'filtered_data': filtered_data, 'users_not_professors': users_not_professors, 'professors' : professors, 'flag' : flag})

#show
@never_cache
def show_professor(request, professor_id, address_id, departmant_id, academic_degree_id, theses_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    professor = Professor.objects.get(pk=professor_id)
    address = Address.objects.get(pk=address_id)
    departmant = Departmant.objects.get(pk=departmant_id)
    academic_degree = AcademicDegree.objects.get(pk=academic_degree_id)
    theses = Theses.objects.get(pk=theses_id)
    professorForm = ProfessorForm(request.POST or None, instance=professor)
    addressForm = AddressForm(request.POST or None, instance=address)
    departmantForm = DepartmantForm(request.POST or None, instance=departmant)
    academic_degreeForm = AcademicDegreeForm(request.POST or None, instance=academic_degree)
    thesesForm = ThesesForm(request.POST or None, instance=theses)

    context = {
        'professorForm': professorForm,
        'addressForm': addressForm,
        'departmantForm': departmantForm,
        'academic_degreeForm': academic_degreeForm,
        'thesesForm': thesesForm,
        'id': professor.user.id,
        'professor': professor,
    }

    return render(request, 'moderator/show_professor.html', context)

@never_cache
def show_scientificJournal(request, scientificJournal_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    scientificJournal = Article.objects.get(pk=scientificJournal_id)
    scientificJournalForm = ArticleForm(request.POST or None, instance=scientificJournal)
    return render(request, 'moderator/show_scientificJournal.html', {'scientificJournalForm': scientificJournalForm, 'id': scientificJournal.user.id,})

@never_cache
def show_collection(request, collection_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    collection = Collection.objects.get(pk=collection_id)
    collectionForm = CollectionForm(request.POST or None, instance=collection)
    return render(request, 'moderator/show_collection.html', {'collectionForm': collectionForm, 'id': collection.user.id,})

@never_cache
def show_patent(request, patent_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    patent = Patent.objects.get(pk=patent_id)
    patentForm = PatentForm(request.POST or None, instance=patent)
    return render(request, 'moderator/show_patent.html', {'patentForm': patentForm, 'id': patent.user.id,})

@never_cache
def show_dissertation_leading(request, dissertation_leading_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    dissertation_leading = Dissertation.objects.get(pk=dissertation_leading_id)
    dissertation_leadingForm = DissertationForm(request.POST or None, instance=dissertation_leading)
    return render(request, 'moderator/show_dissertation_leading.html', {'dissertation_leadingForm': dissertation_leadingForm, 'id': dissertation_leading.user.id,})

@never_cache
def show_conference_participation(request, conference_participation_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    conference_participation = Conference.objects.get(pk=conference_participation_id)
    conference_participationForm = ConferenceParticipationForm(request.POST or None, instance=conference_participation)
    return render(request, 'moderator/show_conference_participation.html', {'conference_participationForm': conference_participationForm, 'id': conference_participation.user.id,})

@never_cache
def show_grant(request, grant_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    grant = Grant.objects.get(pk=grant_id)
    grantForm = GrantForm(request.POST or None, instance=grant)
    return render(request, 'moderator/show_grant.html', {'grantForm': grantForm, 'id': grant.user.id,})

@never_cache
def show_prize(request, prize_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    prize = Prize.objects.get(pk=prize_id)
    prizeForm = PrizeForm(request.POST or None, instance=prize)
    return render(request, 'moderator/show_prize.html', {'prizeForm': prizeForm, 'id': prize.user.id,})

@never_cache
def show_education(request, education_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    education = Education.objects.get(pk=education_id)
    educationForm = EducationForm(request.POST or None, instance=education)
    return render(request, 'moderator/show_education.html', {'educationForm': educationForm, 'id': education.user.id,})

#show lists
@never_cache
def show_professor_list(request, id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    professor_list = Professor.objects.filter(user_id=id)
    address_list = Address.objects.filter(user_id=id)
    departmant_list = Departmant.objects.filter(user_id=id)
    academic_degree_list = AcademicDegree.objects.filter(user_id=id)
    theses_list = Theses.objects.filter(user_id=id)

    professor = list(zip(professor_list, address_list, departmant_list, academic_degree_list, theses_list))

    return render(request, 'moderator/show_professor_list.html', {'professor': professor})

@never_cache
def show_scientificJournal_list(request, id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    scientificJournal_list = Article.objects.filter(user_id=id)
    return render(request, 'moderator/show_scientificJournal_list.html', {'scientificJournal_list': scientificJournal_list})

@never_cache
def show_collection_list(request, id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    collection_list = Collection.objects.filter(user_id=id)
    return render(request, 'moderator/show_collection_list.html', {'collection_list': collection_list})

@never_cache
def show_patent_list(request, id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    patent_list = Patent.objects.filter(user_id=id)
    return render(request, 'moderator/show_patent_list.html', {'patent_list': patent_list})

@never_cache
def show_dissertation_leading_list(request, id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    dissertation_leading_list = Dissertation.objects.filter(user_id=id)
    return render(request, 'moderator/show_dissertation_leading_list.html', {'dissertation_leading_list': dissertation_leading_list})

@never_cache
def show_conference_participation_list(request, id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    conference_participation_list = Conference.objects.filter(user=id)
    return render(request, 'moderator/show_conference_participation_list.html', {'conference_participation_list': conference_participation_list})

@never_cache
def show_grant_list(request, id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    grant_list = Grant.objects.filter(user_id=id)
    return render(request, 'moderator/show_grant_list.html', {'grant_list': grant_list})

@never_cache
def show_prize_list(request, id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    prize_list = Prize.objects.filter(user_id=id)
    return render(request, 'moderator/show_prize_list.html', {'prize_list': prize_list})

@never_cache
def show_education_list(request, id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    education_list = Education.objects.filter(user_id=id)
    return render(request, 'moderator/show_education_list.html', {'education_list': education_list})
