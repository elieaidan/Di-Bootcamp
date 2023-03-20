# Generated by Django 4.1.7 on 2023-03-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('action', 'action'), ('adventure', 'adventure'), ('comedy', 'comedy'), ('drama', 'drama'), ('fantasy', 'fantasy'), ('horror', 'horror'), ('musicals', 'musicals'), ('mystery', 'mystery'), ('romance', 'romance'), ('science-fiction', 'science-fiction'), ('sports', 'sports'), ('thriller', 'thriller'), ('Western', 'Western')], max_length=50),
        ),
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(),
        ),
    ]