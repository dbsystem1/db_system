from django.db import models
from django.forms import SelectDateWidget
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from user.fields import validate_phone_number, validate_first_letter_uppercase


class ProfessorUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class AddressUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class DepartmantUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class AcademicDegreeUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class ThesesUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class ArticleUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class CollectionUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class GrantUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class PrizeUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class EducationUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class ConferenceUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class PatentUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class DissertationUpdateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        ordering = ['-timestamp']

class Professor(models.Model):
    first_name = models.CharField('*Անուն', max_length=50, validators=[validate_first_letter_uppercase], null=True)
    last_name = models.CharField('*Ազգանուն', max_length=50, validators=[validate_first_letter_uppercase],null=True)
    patronomic = models.CharField('*Հայրանուն', max_length=50, validators=[validate_first_letter_uppercase],null=True)
    birth_date = models.DateField('*Ծննդյան ամսաթիվ')
    social_card_number = models.CharField('*ՀԾՀ (սոց. քարտ)', max_length=10)
    gender = models.CharField('*Սեռ', max_length=6)
    membership_of_RA_NAS = models.TextField('*ՀՀ ԳԱԱ անդամություն')
    phone = models.CharField('*Բջջ. հեռախոսահամար', max_length=20, validators=[validate_phone_number])
    postalNumber = models.CharField('*Փոստ. հասցե', max_length=10)
    position = models.CharField('*Պաշտոն', max_length=20)
    domain = models.TextField('*Մասնագիտական դասիչ/Բնագավառ հիմնական', null=True)
    work_time = models.CharField('*Դրույքաչափ', max_length=10, null=True)
    profile_image = models.ImageField(null='True', blank='True', upload_to="images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Address(models.Model):
    country = models.CharField('*Երկիր', max_length=50)
    city = models.CharField('*Քաղաք', max_length=50)
    street = models.CharField('*Փողոց', max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)

class Departmant(models.Model):
    general_work_type = models.TextField('*Գերատեսչության տեսակ(հիմնական)', null=True)
    internal_work_type = models.TextField('*Գերատեսչության տեսակ(ներքին համատեղում)', null=True)
    external_work_type = models.TextField('*Գերատեսչության տեսակ(արտաքին համատեղում)', null=True)
    email = models.EmailField('*Գերատեսչության Էլ. փոստի հասցե', null=True)  
    place = models.TextField('*ԲՈւՀ-ի/կազմակերպության վայր (քաղաք, երկիր)', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)

class AcademicDegree(models.Model):
    science = models.CharField('*Գիտություն', max_length=100, null=True)
    degree = models.CharField('*Գիտական աստիճան', max_length=20, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)

class Theses(models.Model):
    title = models.TextField('*Վերջին թեզի վերնագիր', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)

class Article(models.Model):
    publication_repository = models.CharField('*Հրապարակման շտեմարան', max_length=30)
    DOI = models.TextField('*DOI')
    ISSN_print = models.TextField('*ISSN (print)')
    ISSN_electronic = models.TextField('*ISSN (electronic)')
    title = models.TextField('*Հոդվածի վերնագիր')
    magazine_name = models.TextField('*Ամսագրի անվանում')
    year = models.IntegerField('*Տարի')
    pages_count = models.IntegerField('*Էջեր')
    language = models.CharField('*Լեզու', max_length=50)
    link = models.URLField('*Հոդվածի ինտերնետային հղում')
    funding_source = models.CharField('*Ֆինանսավորման աղբյուր', max_length=50)
    volume = models.IntegerField('*Ամսագրի հատոր')
    quartile = models.CharField('*Quartile(квартиль)', max_length=10, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Collection(models.Model):
    post_type = models.CharField('*Հրապարակման տեսակ', max_length=30)
    title = models.TextField('*Մենագրության (գիրք) վերնագիր')
    chapter_title = models.TextField('*Գլխի կամ հոդվածի վերնագիր')
    publisher_name = models.CharField('*Հրատարակչության անվանում', max_length=50)
    country_of_publication = models.CharField('*Հրատարակման երկիր', max_length=50)
    year_of_publication = models.IntegerField('*Հրատարակման տարի')
    pages = models.IntegerField('*Էջեր')
    language = models.CharField('*Լեզու', max_length=30)
    ISBN = models.TextField('*ISBN', max_length=20)
    DOI = models.TextField('DOI')
    link = models.URLField('Հրապարակման ինտերնետային հղում.')
    guarantor = models.CharField('Երաշխավորող', max_length=50)
    funnding_source = models.CharField('*Ֆինանսավորման աղբյուր', max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Grant(models.Model):
    type = models.TextField('Դրամաշնորհի տեսակը')
    status = models.CharField('Կարգավիճակը դրամաշնորհում', max_length=20)
    title = models.TextField('*Դրամաշնորհի վերնագիր', null=True)
    grant_code = models.CharField('*Դրամաշնորհի ծածկագիր', max_length=50)
    grantor= models.TextField('*Դրամաշնորհ հատկացնող պետության կամ կազմակերպության անվանում', null=True)
    start = models.IntegerField('Դրամաշնորհի իրականացման սկիզբ (տարի)')
    duration_months = models.IntegerField('Դրամաշնորհի տևողություն (ամիս)')
    financial_volume = models.TextField('*Դրամաշնորհի ֆինանսական ծավալ (գումար և տարադրամ)')
    link = models.URLField('Հաշվետվության մատչելիություն (կայքի հասցե)')
    publication_num = models.IntegerField('Հրապարակումների քանակ (որտեղ նշված է դրամաշնորհի մասին)')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Prize(models.Model):
    name = models.TextField('*Մրցանակի անվանում')
    branch = models.CharField('Բնագավառ', max_length=50)
    type = models.CharField('*Մրցանակի տեսակ(անհատական/խմբային)', max_length=20)
    giver = models.TextField('*Մրցանակ շնորհող պետություն կամ կազմակերպություն')
    reason = models.TextField('Ինչի համար է շնորհվել (ձեւակերպում)')
    year = models.IntegerField('*Մրցանակի ստացման տարի')
    link = models.URLField('*Ինտերնետային հղում')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Education(models.Model):
    university = models.TextField('*ԲՈւՀ-ի/կազմակերպության անվանում')
    place = models.TextField('*ԲՈւՀ-ի/կազմակերպության վայր (քաղաք, երկիր)')
    faculty = models.TextField('*Ֆակուլտետ')  
    educ_start_year = models.IntegerField('*Ուսման տարիներ: սկիզբ', null=True)
    educ_end_year = models.IntegerField('*Ուսման տարիներ։ ավարտ', null=True)
    degree = models.TextField('*Կրթական/Գիտական ծրագիր')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Conference(models.Model):
    name = models.CharField('*Գիտաժողովի լրիվ անվանում', max_length=150)
    country = models.CharField('*Գիտաժողովի անցկացման երկիր', max_length=100) 
    date = models.DateField('*Գիտաժողովի անցկացման տարի/օր/ամիս')
    authors = models.CharField('*Հեղինակ/հեղինակներ', max_length=150)
    authors_count = models.IntegerField('*Համահեղինակների քանակ (ներառյալ հայտատուին)')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Patent(models.Model):
    authors = models.CharField('*Հեղինակ/հեղինակներ', max_length=150)
    name = models.CharField('*Արտոնագրի անվանում', max_length=150)
    registration_country = models.CharField('*Արտոնագրի գրանցման երկիր', max_length=150)
    registration_organization = models.CharField('*Արտոնագրի գրանցման կազմակերպություն', max_length=150)
    patent_number = models.CharField('*Արտոնագրի համար', max_length=150)
    year = models.IntegerField('Արտոնագրի գրանցման տարի')
    classification_index = models.CharField('*Միջազգային կլասիֆիկատորի ինդեքս', max_length=150)
    authors_count = models.IntegerField('Համահեղինակների քանակ (ներառյալ հայտատուին)')
    link = models.URLField('Ինտերնետային հղում')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Dissertation(models.Model):
    title = models.TextField('*Ատենախոսության վերնագիր')
    code = models.TextField('*Ատենախոսության մասնագիտական կոդ/դասիչ')
    organization = models.CharField('Ատենախոսության իրականացման կազմակերպություն', max_length=100)
    protection_year = models.IntegerField('*Կայացած պաշտպանության տարի')
    confirmation_date = models.DateField('ԲՈԿ-ի կողմից հաստատման ամսաթիվ (օր.ամիս.տարի)')
    name = models.TextField('Մասնագիտական խորհուրդի անվանում՝', null=True)
    password = models.TextField('*Մասնագիտական խորհուրդի ծածկագիր', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
