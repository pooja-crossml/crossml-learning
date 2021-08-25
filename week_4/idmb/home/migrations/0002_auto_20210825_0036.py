# Generated by Django 3.2.6 on 2021-08-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='Date_of_Birth',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='Genure',
            new_name='genure',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='Language',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='Length',
            new_name='length',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='Release_Date',
            new_name='release_Date',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='Movie',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='Rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='Votes',
            new_name='votes',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='Awards',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Awards',
        ),
        migrations.DeleteModel(
            name='Awards',
        ),
        migrations.AddField(
            model_name='artist',
            name='award',
            field=models.ManyToManyField(null=True, to='home.Award'),
        ),
        migrations.AddField(
            model_name='movie',
            name='awards',
            field=models.ManyToManyField(null=True, to='home.Award'),
        ),
    ]
