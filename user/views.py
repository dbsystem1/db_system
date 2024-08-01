from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Professor, AcademicDegree, Address, Prize, Article, Collection, Departmant, Theses, Conference, Dissertation, Grant, Patent, Education
from .IndividualQuestionnaireForm import ProfessorForm, AcademicDegreeForm, AddressForm, DepartmantForm, ThesesForm
from .scientificJournalForm import ArticleForm
from .collectionForm import CollectionForm
from .conferenceParticipationForm import ConferenceParticipationForm
from .patentForm import PatentForm
from .dissertationForm import DissertationForm
from .grantForm import GrantForm
from .prizeForm import PrizeForm 
from .educationForm import EducationForm
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .registrationForm import UserRegistrationForm
from django.contrib.auth import authenticate, login
from .loginForm import LoginForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User

from .profileForm import ProfileForm
from .passwordChangeForm import PasswordChangingForm

from django.contrib.auth import update_session_auth_hash
from django.views.decorators.cache import never_cache

from django.utils.translation import activate

from .models import ProfessorUpdateHistory, AddressUpdateHistory, DepartmantUpdateHistory, AcademicDegreeUpdateHistory, ThesesUpdateHistory
from .models import ArticleUpdateHistory, CollectionUpdateHistory, GrantUpdateHistory, PrizeUpdateHistory, EducationUpdateHistory, ConferenceUpdateHistory, PatentUpdateHistory, DissertationUpdateHistory   

def my_view(request):
    activate('hy')  # Activate Armenian language
    # Your view logic here

@never_cache
def add_professor(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    submitted = False
    if request.method == "POST":
        professorForm = ProfessorForm(request.POST, request.FILES)
        academicDegreeForm = AcademicDegreeForm(request.POST)
        addressForm = AddressForm(request.POST)
        departmantForm = DepartmantForm(request.POST)
        thesesForm = ThesesForm(request.POST)
        if professorForm.is_valid() and academicDegreeForm.is_valid() and addressForm.is_valid() and departmantForm.is_valid() and thesesForm.is_valid():
            professor = professorForm.save(commit=False)
            professor.user = request.user
            professor.save()
            
            accademicDegrre = academicDegreeForm.save(commit=False)
            accademicDegrre.user = request.user
            accademicDegrre.professor = professor 
            accademicDegrre.save()

            address = addressForm.save(commit=False)
            address.user = request.user
            address.professor = professor 
            address.save()

            department = departmantForm.save(commit=False)
            department.user = request.user
            department.professor = professor 
            department.save()

            theses = thesesForm.save(commit=False)
            theses.user = request.user
            theses.professor = professor 
            theses.save()

            return HttpResponseRedirect('/add_professor/?submitted=True')
    else:
        professorForm = ProfessorForm()
        academicDegreeForm = AcademicDegreeForm()
        addressForm = AddressForm()
        departmantForm = DepartmantForm()
        thesesForm = ThesesForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'user/add_professor.html', {'professorForm': professorForm, 'addressForm': addressForm, 'academicDegreeForm': academicDegreeForm, 'departmantForm': departmantForm, 'thesesForm': thesesForm, 'submitted': submitted})

@never_cache
def show_professor_list(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    professor_list = Professor.objects.filter(user_id=request.user)
    address_list = Address.objects.filter(user_id=request.user)
    departmant_list = Departmant.objects.filter(user_id=request.user)
    academic_degree_list = AcademicDegree.objects.filter(user_id=request.user)
    theses_list = Theses.objects.filter(user_id=request.user)

    professor = list(zip(professor_list, address_list, departmant_list, academic_degree_list, theses_list))

    return render(request, 'user/show_professor_list.html', {'professor': professor})

@never_cache
def update_professor(request, professor_id, address_id, departmant_id, academic_degree_id, theses_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    
    professor = Professor.objects.get(pk=professor_id)
    professorForm = ProfessorForm(request.POST or None, request.FILES or None, instance=professor)
    address = Address.objects.get(pk=address_id)
    addressForm = AddressForm(request.POST or None, instance=address)
    departmant = Departmant.objects.get(pk=departmant_id)
    departmantForm = DepartmantForm(request.POST or None, instance=departmant)
    academic_degree = AcademicDegree.objects.get(pk=academic_degree_id)
    academic_degreeForm = AcademicDegreeForm(request.POST or None, instance=academic_degree)
    theses = Theses.objects.get(pk=theses_id)
    thesesForm = ThesesForm(request.POST or None, instance=theses)

    old_professor_data = {key: getattr(professor, key) for key in professor.__dict__.keys() if not key.startswith('_')}
    old_address_data = {key: getattr(address, key) for key in address.__dict__.keys() if not key.startswith('_')}
    old_departmant_data = {key: getattr(departmant, key) for key in departmant.__dict__.keys() if not key.startswith('_')}
    old_academic_degree_data = {key: getattr(academic_degree, key) for key in academic_degree.__dict__.keys() if not key.startswith('_')}
    old_theses_data = {key: getattr(theses, key) for key in theses.__dict__.keys() if not key.startswith('_')}

    if professorForm.is_valid() and addressForm.is_valid() and departmantForm.is_valid() and academic_degreeForm.is_valid() and thesesForm.is_valid():
            professorForm.save()
            addressForm.save()
            departmantForm.save()
            academic_degreeForm.save()
            thesesForm.save()

            new_professor_data = {key: getattr(professor, key) for key in professor.__dict__.keys() if not key.startswith('_')}
            professor_changes = {k: (v, new_professor_data[k]) for k, v in old_professor_data.items() if new_professor_data.get(k) != v}
            new_address_data = {key: getattr(address, key) for key in address.__dict__.keys() if not key.startswith('_')}
            address_changes = {k: (v, new_address_data[k]) for k, v in old_address_data.items() if new_address_data.get(k) != v}
            new_departmant_data = {key: getattr(departmant, key) for key in departmant.__dict__.keys() if not key.startswith('_')}
            departmant_changes = {k: (v, new_departmant_data[k]) for k, v in old_departmant_data.items() if new_departmant_data.get(k) != v}
            new_academic_degree_data = {key: getattr(academic_degree, key) for key in academic_degree.__dict__.keys() if not key.startswith('_')}
            academic_degree_changes = {k: (v, new_academic_degree_data[k]) for k, v in old_academic_degree_data.items() if new_academic_degree_data.get(k) != v}
            new_theses_data = {key: getattr(theses, key) for key in theses.__dict__.keys() if not key.startswith('_')}
            theses_changes = {k: (v, new_theses_data[k]) for k, v in old_theses_data.items() if new_theses_data.get(k) != v}
            
            # Log the update
            ProfessorUpdateHistory.objects.create(
                user=request.user,
                action='Update',
                details=f'Updated entity with ID {professor_id}: {professor_changes}'
            )
            # Log the update
            AddressUpdateHistory.objects.create(
                user=request.user,
                action='Update',
                details=f'Updated entity with ID {address_id}: {address_changes}'
            )
            # Log the update
            DepartmantUpdateHistory.objects.create(
                user=request.user,
                action='Update',
                details=f'Updated entity with ID {departmant_id}: {departmant_changes}'
            )
            # Log the update
            AcademicDegreeUpdateHistory.objects.create(
                user=request.user,
                action='Update',
                details=f'Updated entity with ID {academic_degree_id}: {academic_degree_changes}'
            )
            # Log the update
            ThesesUpdateHistory.objects.create(
                user=request.user,
                action='Update',
                details=f'Updated entity with ID {theses_id}: {theses_changes}'
            )

            return redirect('user-update_success')
    
    context = {
        'professorForm': professorForm,
        'addressForm': addressForm,
        'departmantForm': departmantForm,
        'academic_degreeForm': academic_degreeForm,
        'thesesForm': thesesForm,
        'professor': professor,
    }
    return render(request, 'user/update_professor.html', context)

@never_cache
def add_scientificJournal(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    submitted = False
    if request.method == "POST":
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            article = articleForm.save(commit=False)
            article.user = request.user
            article.save()
            return HttpResponseRedirect('/add_scientificJournal/?submitted=True')
    else:
        articleForm = ArticleForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'user/add_scientificJournal.html', {'articleForm': articleForm, 'submitted': submitted})

@never_cache
def show_scientificJournal_list(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    scientificJournal_list = Article.objects.filter(user_id=request.user)
    return render(request, 'user/show_scientificJournal_list.html', {'scientificJournal_list': scientificJournal_list})

@never_cache
def update_scientificJournal(request, scientificJournal_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    scientificJournal = Article.objects.get(pk=scientificJournal_id)

    old_scientificJournal_data = {key: getattr(scientificJournal, key) for key in scientificJournal.__dict__.keys() if not key.startswith('_')}

    scientificJournalForm = ArticleForm(request.POST or None, instance=scientificJournal)
    if scientificJournalForm.is_valid():
            scientificJournalForm.save()

            new_scientificJournal_data = {key: getattr(scientificJournal, key) for key in scientificJournal.__dict__.keys() if not key.startswith('_')}
            changes = {k: (v, new_scientificJournal_data[k]) for k, v in old_scientificJournal_data.items() if new_scientificJournal_data.get(k) != v}

            # Log the update
            ArticleUpdateHistory.objects.create(
                user=request.user,
                action='Update',
                details=f'Updated entity with ID {scientificJournal_id}: {changes}'
            )

            return redirect('user-update_success')
    
    return render(request, 'user/update_scientificJournal.html', {'scientificJournalForm': scientificJournalForm})

@never_cache
def add_collection(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    submitted = False
    if request.method == "POST":
        collectionForm = CollectionForm(request.POST)
        if collectionForm.is_valid():
            collection = collectionForm.save(commit=False)
            collection.user = request.user
            collection.save()

            return HttpResponseRedirect('/add_collection/?submitted=True')
        else:
            print("error")
    else:
        collectionForm = CollectionForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'user/add_collection.html', {'collectionForm': collectionForm, 'submitted': submitted})

@never_cache
def show_collection_list(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    collection_list = Collection.objects.filter(user_id=request.user)
    return render(request, 'user/show_collection_list.html', {'collection_list': collection_list})

@never_cache
def update_collection(request, collection_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    collection = Collection.objects.get(pk=collection_id)

    old_collection_data = {key: getattr(collection, key) for key in collection.__dict__.keys() if not key.startswith('_')}

    collectionForm = CollectionForm(request.POST or None, instance=collection)
    if collectionForm.is_valid():
            collectionForm.save()

            new_collection_data = {key: getattr(collection, key) for key in collection.__dict__.keys() if not key.startswith('_')}
            changes = {k: (v, new_collection_data[k]) for k, v in old_collection_data.items() if new_collection_data.get(k) != v}
            
            # Log the update
            CollectionUpdateHistory.objects.create(
                user=request.user,
                action='Update',
                details=f'Updated entity with ID {collection_id}: {changes}'
            )
            return redirect('user-update_success')
    
    return render(request, 'user/update_collection.html', {'collectionForm': collectionForm})

@never_cache
def add_patent(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    submitted = False
    if request.method == "POST":
        patentForm = PatentForm(request.POST)
        if patentForm.is_valid():
            patent = patentForm.save(commit=False)
            patent.user = request.user
            patent.save()

            return HttpResponseRedirect('/add_patent/?submitted=True')
    else:
        patentForm = PatentForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'user/add_patent.html', {'patentForm': patentForm, 'submitted': submitted})

@never_cache
def show_patent_list(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    patent_list = Patent.objects.filter(user_id=request.user)
    return render(request, 'user/show_patent_list.html', {'patent_list': patent_list})

@never_cache
def update_patent(request, patent_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    patent = Patent.objects.get(pk=patent_id)

    old_patent_data = {key: getattr(patent, key) for key in patent.__dict__.keys() if not key.startswith('_')}

    patentForm = PatentForm(request.POST or None, instance=patent)
    if patentForm.is_valid():
        patentForm.save()

        new_patent_data = {key: getattr(patent, key) for key in patent.__dict__.keys() if not key.startswith('_')}
        changes = {k: (v, new_patent_data[k]) for k, v in old_patent_data.items() if new_patent_data.get(k) != v}
        
        # Log the update
        PatentUpdateHistory.objects.create(
            user=request.user,
            action='Update',
            details=f'Updated entity with ID {patent_id}: {changes}'
        )

        return redirect('user-update_success')
    return render(request, 'user/update_patent.html', {'patentForm': patentForm})

@never_cache
def add_dissertation_leading(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    submitted = False
    if request.method == "POST":
        dissertationForm = DissertationForm(request.POST)
        if dissertationForm.is_valid():
            dissertation = dissertationForm.save(commit=False)
            dissertation.user = request.user
            dissertation.save()

            return HttpResponseRedirect('/add_dissertation_leading/?submitted=True')
    else:
        dissertationForm = DissertationForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'user/add_dissertation_leading.html', {'dissertationForm': dissertationForm,'submitted': submitted})

@never_cache
def show_dissertation_leading_list(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    dissertation_leading_list = Dissertation.objects.filter(user_id=request.user)
    return render(request, 'user/show_dissertation_leading_list.html', {'dissertation_leading_list': dissertation_leading_list})

@never_cache
def update_dissertation_leading(request, dissertation_leading_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    dissertation_leading = Dissertation.objects.get(pk=dissertation_leading_id)

    old_dissertation_leading_data = {key: getattr(dissertation_leading, key) for key in dissertation_leading.__dict__.keys() if not key.startswith('_')}

    dissertation_leadingForm = DissertationForm(request.POST or None, instance=dissertation_leading)
    if dissertation_leadingForm.is_valid():
        dissertation_leadingForm.save()

        new_dissertation_leading_data = {key: getattr(dissertation_leading, key) for key in dissertation_leading.__dict__.keys() if not key.startswith('_')}
        changes = {k: (v, new_dissertation_leading_data[k]) for k, v in old_dissertation_leading_data.items() if new_dissertation_leading_data.get(k) != v}
        
        # Log the update
        DissertationUpdateHistory.objects.create(
            user=request.user,
            action='Update',
            details=f'Updated entity with ID {dissertation_leading_id}: {changes}'
        )

        return redirect('user-update_success')
    return render(request, 'user/update_dissertation_leading.html', {'dissertation_leadingForm': dissertation_leadingForm})

@never_cache
def add_conference_participation(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    submitted = False
    if request.method == "POST":
        conferenceParticipationForm = ConferenceParticipationForm(request.POST)
        if conferenceParticipationForm.is_valid():
            conference = conferenceParticipationForm.save(commit=False)
            conference.user = request.user
            conference.save()

            return HttpResponseRedirect('/add_conference_participation/?submitted=True')
    else:
        conferenceParticipationForm = ConferenceParticipationForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'user/add_conference_participation.html', {'conferenceParticipationForm': conferenceParticipationForm, 'submitted': submitted})

@never_cache
def update_conference_participation(request, conference_participation_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    conference_participation = Conference.objects.get(pk=conference_participation_id)

    old_conference_participation_data = {key: getattr(conference_participation, key) for key in conference_participation.__dict__.keys() if not key.startswith('_')}

    conference_participationForm = ConferenceParticipationForm(request.POST or None, instance=conference_participation)
    if conference_participationForm.is_valid():
        conference_participationForm.save()

        new_conference_participation_data = {key: getattr(conference_participation, key) for key in conference_participation.__dict__.keys() if not key.startswith('_')}
        changes = {k: (v, new_conference_participation_data[k]) for k, v in old_conference_participation_data.items() if new_conference_participation_data.get(k) != v}
        
        # Log the update
        ConferenceUpdateHistory.objects.create(
            user=request.user,
            action='Update',
            details=f'Updated entity with ID {conference_participation_id}: {changes}'
        )

        return redirect('user-update_success')
    return render(request, 'user/update_conference_participation.html', {'conference_participationForm': conference_participationForm})

@never_cache
def show_conference_participation_list(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    conference_participation_list = Conference.objects.filter(user=request.user)
    return render(request, 'user/show_conference_participation_list.html', {'conference_participation_list': conference_participation_list})

@never_cache
def add_grant(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    submitted = False
    if request.method == "POST":
        grantForm = GrantForm(request.POST)
        if grantForm.is_valid():
            grant = grantForm.save(commit=False)
            grant.user = request.user
            grant.save()

            return HttpResponseRedirect('/add_grant/?submitted=True')
    else:
        grantForm = GrantForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'user/add_grant.html', {'grantForm': grantForm, 'submitted': submitted})

@never_cache
def update_grant(request, grant_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    grant = Grant.objects.get(pk=grant_id)

    old_grant_data = {key: getattr(grant, key) for key in grant.__dict__.keys() if not key.startswith('_')}

    grantForm = GrantForm(request.POST or None, instance=grant)
    if grantForm.is_valid():
        grantForm.save()

        new_grant_data = {key: getattr(grant, key) for key in grant.__dict__.keys() if not key.startswith('_')}
        changes = {k: (v, new_grant_data[k]) for k, v in old_grant_data.items() if new_grant_data.get(k) != v}
        
        # Log the update
        GrantUpdateHistory.objects.create(
            user=request.user,
            action='Update',
            details=f'Updated entity with ID {grant_id}: {changes}'
        )

        return redirect('user-update_success')
    return render(request, 'user/update_grant.html', {'grantForm': grantForm})

@never_cache
def show_grant_list(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    grant_list = Grant.objects.filter(user_id=request.user)
    return render(request, 'user/show_grant_list.html', {'grant_list': grant_list})

@never_cache
def add_prize(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    submitted = False
    if request.method == "POST":
        prizeForm = PrizeForm(request.POST)
        if prizeForm.is_valid():
            prize = prizeForm.save(commit=False)
            prize.user = request.user
            prize.save()

            return HttpResponseRedirect('/add_prize/?submitted=True')
    else:
        prizeForm = PrizeForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'user/add_prize.html', {'prizeForm': prizeForm, 'submitted': submitted})

@never_cache
def show_prize_list(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    prize_list = Prize.objects.filter(user_id=request.user)
    return render(request, 'user/show_prize_list.html', {'prize_list': prize_list})

@never_cache
def update_prize(request, prize_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    prize = Prize.objects.get(pk=prize_id)

    old_prize_data = {key: getattr(prize, key) for key in prize.__dict__.keys() if not key.startswith('_')}

    prizeForm = PrizeForm(request.POST or None, instance=prize)
    if prizeForm.is_valid():
        prizeForm.save()

        new_prize_data = {key: getattr(prize, key) for key in prize.__dict__.keys() if not key.startswith('_')}
        changes = {k: (v, new_prize_data[k]) for k, v in old_prize_data.items() if new_prize_data.get(k) != v}
        
        # Log the update
        PrizeUpdateHistory.objects.create(
            user=request.user,
            action='Update',
            details=f'Updated entity with ID {prize_id}: {changes}'
        )

        return redirect('user-update_success')
    return render(request, 'user/update_prize.html', {'prizeForm': prizeForm})

@never_cache
def add_education(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    submitted = False
    if request.method == "POST":
        educationForm = EducationForm(request.POST)
        if educationForm.is_valid():
            education = educationForm.save(commit=False)
            education.user = request.user
            education.save()

            return HttpResponseRedirect('/add_education/?submitted=True')
    else:
        educationForm = EducationForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'user/add_education.html', {'educationForm': educationForm, 'submitted': submitted})

@never_cache
def show_education_list(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    education_list = Education.objects.filter(user_id=request.user)
    return render(request, 'user/show_education_list.html', {'education_list': education_list})

@never_cache
def update_education(request, education_id):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    education = Education.objects.get(pk=education_id)

    old_education_data = {key: getattr(education, key) for key in education.__dict__.keys() if not key.startswith('_')}

    educationForm = EducationForm(request.POST or None, instance=education)
    if educationForm.is_valid():
        educationForm.save()

        new_education_data = {key: getattr(education, key) for key in education.__dict__.keys() if not key.startswith('_')}
        changes = {k: (v, new_education_data[k]) for k, v in old_education_data.items() if new_education_data.get(k) != v}
        
        # Log the update
        EducationUpdateHistory.objects.create(
            user=request.user,
            action='Update',
            details=f'Updated entity with ID {education_id}: {changes}'
        )

        return redirect('user-update_success')
    return render(request, 'user/update_education.html', {'educationForm': educationForm})

def base(request):
    return render(request, 'user/base.html')

@never_cache
def default_home_base(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    return render(request, 'user/default_home_base.html')

def registration_success(request):
    return render(request, 'user/registration_success.html')

def welcome(request):
    return render(request, 'user/welcome.html')

@never_cache
def update_success(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    return render(request, 'user/update_success.html')

@never_cache
def default_home(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    
    user = request.user
    return render(request, 'user/default_home.html', {'user': user})

@never_cache
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()          
            return redirect('user-registration_success')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'user/register.html', {'form': form})

@never_cache
def admin_or_user(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    
    return render(request, 'user/admin_or_user.html')

@never_cache
def log_in(request):    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if user.email == "mikayel.avanesyan@rau.am" or user.email == "marina.kalashyan@rau.am" or user.email == "mary.tadevosyan@rau.am" or user.email == "ruzanna.nazaryan@rau.am" or user.email == "naira.gevorgyan@rau.am" or user.email == "alisa.tatosova@student.rau.am":
                    return redirect('admin_or_user')
                elif user.email == "arusyak.zangezuryan@student.rau.am" or user.email == "arman.darbinyan@rau.am":
                    return redirect(reverse('admin:index'))
                else:
                    return redirect('user-default_home')
            else:
                form.add_error(None, "invalid")
                return render(request, 'user/log_in.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'user/log_in.html', {'form': form})

@never_cache
def log_out(request):
    logout(request)
    return redirect('user-log_in') 

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
    
    return render(request, 'user/edit_profile.html', {'form': form})

@never_cache
def change_password(request):
    if not request.user.is_authenticated:
        return redirect('user-log_in') 
    
    current_user = User.objects.get(id=request.user.id) # Assuming user is authenticated
    form = PasswordChangingForm(user=current_user)  # Pass the user object to SetPasswordForm
    if request.method == 'POST':
        form = PasswordChangingForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('user-update_success')

    return render(request, 'user/password.html', {'form': form})
