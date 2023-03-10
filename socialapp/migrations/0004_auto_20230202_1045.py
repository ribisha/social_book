# Generated by Django 3.2.15 on 2023-02-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0003_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_images'),
        ),
    ]
