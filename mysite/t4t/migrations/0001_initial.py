# Generated by Django 3.2.9 on 2021-12-18 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('tags', models.ManyToManyField(to='t4t.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=255)),
                ('email', models.EmailField(default=' ', max_length=254)),
                ('body', models.TextField(default=' ')),
                ('post', models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='t4t.post')),
            ],
        ),
    ]
