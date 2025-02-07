# Generated by Django 5.1.6 on 2025-02-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='book_images/', verbose_name='загрузите фото')),
                ('title', models.CharField(max_length=100, verbose_name='укажите название книги ')),
                ('description', models.TextField(blank=True, verbose_name='укажите описание книги ')),
                ('price', models.PositiveIntegerField(default=200, verbose_name='укажите ценну ')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('DRAMA', 'DRAMA'), ('ROMAN', 'ROMAN'), ('FANTASY', 'FANTASY')], default='DRAMA', max_length=10, verbose_name='выберите жанр')),
                ('time', models.TimeField(blank=True, verbose_name='укажите время  ')),
                ('times', models.TimeField(verbose_name='Укажите  время  просмотра ')),
                ('director', models.CharField(default=' Чынгыз Айтматов', max_length=100)),
                ('trailer', models.URLField(verbose_name='укажите ссыльку из Youtube')),
                ('author', models.CharField(max_length=30, verbose_name='укажите автора ')),
                ('mail', models.CharField(max_length=30, verbose_name='укажите почту  автора ')),
            ],
            options={
                'verbose_name': 'книгу',
                'verbose_name_plural': 'книги ',
            },
        ),
    ]
