# Generated by Django 5.0.3 on 2024-03-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('is_available', models.BooleanField(default=True)),
                ('is_borrowed', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('cover_page', models.ImageField(upload_to='book_covers/')),
                ('categories', models.ManyToManyField(to='library.category')),
            ],
        ),
    ]
