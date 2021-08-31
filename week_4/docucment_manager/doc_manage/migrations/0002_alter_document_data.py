# Generated by Django 3.2.6 on 2021-08-30 19:36

from django.db import migrations, models
import doc_manage.validators


class Migration(migrations.Migration):

    dependencies = [
        ('doc_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='data',
            field=models.FileField(upload_to='media', validators=[doc_manage.validators.validate_file_extension]),
        ),
    ]