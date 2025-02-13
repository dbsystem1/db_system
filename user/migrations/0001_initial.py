# Generated by Django 5.0.7 on 2024-07-25 09:03

import django.db.models.deletion
import user.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDegreeUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='AddressUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_repository', models.CharField(max_length=30, verbose_name='*Հրապարակման շտեմարան')),
                ('DOI', models.TextField(verbose_name='*DOI')),
                ('ISSN_print', models.TextField(verbose_name='*ISSN (print)')),
                ('ISSN_electronic', models.TextField(verbose_name='*ISSN (electronic)')),
                ('title', models.TextField(verbose_name='*Հոդվածի վերնագիր')),
                ('magazine_name', models.TextField(verbose_name='*Ամսագրի անվանում')),
                ('year', models.IntegerField(verbose_name='*Տարի')),
                ('pages_count', models.IntegerField(verbose_name='*Էջեր')),
                ('language', models.CharField(max_length=50, verbose_name='*Լեզու')),
                ('link', models.URLField(verbose_name='*Հոդվածի ինտերնետային հղում')),
                ('funding_source', models.CharField(max_length=50, verbose_name='*Ֆինանսավորման աղբյուր')),
                ('volume', models.IntegerField(verbose_name='*Ամսագրի հատոր')),
                ('quartile', models.CharField(max_length=10, null=True, verbose_name='*Quartile(квартиль)')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(max_length=30, verbose_name='*Հրապարակման տեսակ')),
                ('title', models.TextField(verbose_name='*Մենագրության (գիրք) վերնագիր')),
                ('chapter_title', models.TextField(verbose_name='*Գլխի կամ հոդվածի վերնագիր')),
                ('publisher_name', models.CharField(max_length=50, verbose_name='*Հրատարակչության անվանում')),
                ('country_of_publication', models.CharField(max_length=50, verbose_name='*Հրատարակման երկիր')),
                ('year_of_publication', models.IntegerField(verbose_name='*Հրատարակման տարի')),
                ('pages', models.IntegerField(verbose_name='*Էջեր')),
                ('language', models.CharField(max_length=30, verbose_name='*Լեզու')),
                ('ISBN', models.TextField(max_length=20, verbose_name='*ISBN')),
                ('DOI', models.TextField(verbose_name='DOI')),
                ('link', models.URLField(verbose_name='Հրապարակման ինտերնետային հղում.')),
                ('guarantor', models.CharField(max_length=50, verbose_name='Երաշխավորող')),
                ('funnding_source', models.CharField(max_length=50, verbose_name='*Ֆինանսավորման աղբյուր')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='*Գիտաժողովի լրիվ անվանում')),
                ('country', models.CharField(max_length=100, verbose_name='*Գիտաժողովի անցկացման երկիր')),
                ('date', models.DateField(verbose_name='*Գիտաժողովի անցկացման տարի/օր/ամիս')),
                ('authors', models.CharField(max_length=150, verbose_name='*Հեղինակ/հեղինակներ')),
                ('authors_count', models.IntegerField(verbose_name='*Համահեղինակների քանակ (ներառյալ հայտատուին)')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='DepartmantUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Dissertation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='*Ատենախոսության վերնագիր')),
                ('code', models.TextField(verbose_name='*Ատենախոսության մասնագիտական կոդ/դասիչ')),
                ('organization', models.CharField(max_length=100, verbose_name='Ատենախոսության իրականացման կազմակերպություն')),
                ('protection_year', models.IntegerField(verbose_name='*Կայացած պաշտպանության տարի')),
                ('confirmation_date', models.DateField(verbose_name='ԲՈԿ-ի կողմից հաստատման ամսաթիվ (օր.ամիս.տարի)')),
                ('name', models.TextField(null=True, verbose_name='Մասնագիտական խորհուրդի անվանում՝')),
                ('password', models.TextField(null=True, verbose_name='*Մասնագիտական խորհուրդի ծածկագիր')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DissertationUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.TextField(verbose_name='*ԲՈւՀ-ի/կազմակերպության անվանում')),
                ('place', models.TextField(verbose_name='*ԲՈւՀ-ի/կազմակերպության վայր (քաղաք, երկիր)')),
                ('faculty', models.TextField(verbose_name='*Ֆակուլտետ')),
                ('educ_start_year', models.IntegerField(null=True, verbose_name='*Ուսման տարիներ: սկիզբ')),
                ('educ_end_year', models.IntegerField(null=True, verbose_name='*Ուսման տարիներ։ ավարտ')),
                ('degree', models.TextField(verbose_name='*Կրթական/Գիտական ծրագիր')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EducationUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(verbose_name='Դրամաշնորհի տեսակը')),
                ('status', models.CharField(max_length=20, verbose_name='Կարգավիճակը դրամաշնորհում')),
                ('title', models.TextField(null=True, verbose_name='*Դրամաշնորհի վերնագիր')),
                ('grant_code', models.CharField(max_length=50, verbose_name='*Դրամաշնորհի ծածկագիր')),
                ('grantor', models.TextField(null=True, verbose_name='*Դրամաշնորհ հատկացնող պետության կամ կազմակերպության անվանում')),
                ('start', models.IntegerField(verbose_name='Դրամաշնորհի իրականացման սկիզբ (տարի)')),
                ('duration_months', models.IntegerField(verbose_name='Դրամաշնորհի տևողություն (ամիս)')),
                ('financial_volume', models.TextField(verbose_name='*Դրամաշնորհի ֆինանսական ծավալ (գումար և տարադրամ)')),
                ('link', models.URLField(verbose_name='Հաշվետվության մատչելիություն (կայքի հասցե)')),
                ('publication_num', models.IntegerField(verbose_name='Հրապարակումների քանակ (որտեղ նշված է դրամաշնորհի մասին)')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GrantUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authors', models.CharField(max_length=150, verbose_name='*Հեղինակ/հեղինակներ')),
                ('name', models.CharField(max_length=150, verbose_name='*Արտոնագրի անվանում')),
                ('registration_country', models.CharField(max_length=150, verbose_name='*Արտոնագրի գրանցման երկիր')),
                ('registration_organization', models.CharField(max_length=150, verbose_name='*Արտոնագրի գրանցման կազմակերպություն')),
                ('patent_number', models.CharField(max_length=150, verbose_name='*Արտոնագրի համար')),
                ('year', models.IntegerField(verbose_name='Արտոնագրի գրանցման տարի')),
                ('classification_index', models.CharField(max_length=150, verbose_name='*Միջազգային կլասիֆիկատորի ինդեքս')),
                ('authors_count', models.IntegerField(verbose_name='Համահեղինակների քանակ (ներառյալ հայտատուին)')),
                ('link', models.URLField(verbose_name='Ինտերնետային հղում')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatentUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='*Մրցանակի անվանում')),
                ('branch', models.CharField(max_length=50, verbose_name='Բնագավառ')),
                ('type', models.CharField(max_length=20, verbose_name='*Մրցանակի տեսակ(անհատական/խմբային)')),
                ('giver', models.TextField(verbose_name='*Մրցանակ շնորհող պետություն կամ կազմակերպություն')),
                ('reason', models.TextField(verbose_name='Ինչի համար է շնորհվել (ձեւակերպում)')),
                ('year', models.IntegerField(verbose_name='*Մրցանակի ստացման տարի')),
                ('link', models.URLField(verbose_name='*Ինտերնետային հղում')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrizeUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True, validators=[user.fields.validate_first_letter_uppercase], verbose_name='*Անուն')),
                ('last_name', models.CharField(max_length=50, null=True, validators=[user.fields.validate_first_letter_uppercase], verbose_name='*Ազգանուն')),
                ('patronomic', models.CharField(max_length=50, null=True, validators=[user.fields.validate_first_letter_uppercase], verbose_name='*Հայրանուն')),
                ('birth_date', models.DateField(verbose_name='*Ծննդյան ամսաթիվ')),
                ('social_card_number', models.CharField(max_length=10, verbose_name='*ՀԾՀ (սոց. քարտ)')),
                ('gender', models.CharField(max_length=6, verbose_name='*Սեռ')),
                ('membership_of_RA_NAS', models.TextField(verbose_name='*ՀՀ ԳԱԱ անդամություն')),
                ('phone', models.CharField(max_length=20, validators=[user.fields.validate_phone_number], verbose_name='*Բջջ. հեռախոսահամար')),
                ('postalNumber', models.CharField(max_length=10, verbose_name='*Փոստ. հասցե')),
                ('position', models.CharField(max_length=20, verbose_name='*Պաշտոն')),
                ('domain', models.TextField(null=True, verbose_name='*Մասնագիտական դասիչ/Բնագավառ հիմնական')),
                ('work_time', models.CharField(max_length=10, null=True, verbose_name='*Դրույքաչափ')),
                ('profile_image', models.ImageField(blank='True', null='True', upload_to='images/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Departmant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_work_type', models.TextField(null=True, verbose_name='*Գերատեսչության տեսակ(հիմնական)')),
                ('internal_work_type', models.TextField(null=True, verbose_name='*Գերատեսչության տեսակ(ներքին համատեղում)')),
                ('external_work_type', models.TextField(null=True, verbose_name='*Գերատեսչության տեսակ(արտաքին համատեղում)')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='*Գերատեսչության Էլ. փոստի հասցե')),
                ('place', models.TextField(null=True, verbose_name='*ԲՈւՀ-ի/կազմակերպության վայր (քաղաք, երկիր)')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, verbose_name='*Երկիր')),
                ('city', models.CharField(max_length=50, verbose_name='*Քաղաք')),
                ('street', models.CharField(max_length=50, null=True, verbose_name='*Փողոց')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.professor')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('science', models.CharField(max_length=100, null=True, verbose_name='*Գիտություն')),
                ('degree', models.CharField(max_length=20, null=True, verbose_name='*Գիտական աստիճան')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.professor')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Theses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True, verbose_name='*Վերջին թեզի վերնագիր')),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.professor')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThesesUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
