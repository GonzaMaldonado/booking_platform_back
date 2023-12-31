# Generated by Django 4.2.2 on 2023-06-09 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/images/'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'U'), ('company', 'C')], default='', max_length=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
