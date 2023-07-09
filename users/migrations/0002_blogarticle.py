# Generated by Django 4.2.1 on 2023-07-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blog')),
                ('views', models.PositiveIntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]