# Generated by Django 3.2.9 on 2022-11-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0005_alter_solution_solution_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='solution_category',
            field=models.CharField(choices=[('Network  Solutions', 'Network  Solutions'), ('Digital Marketing ', 'Digital Marketing '), ('Data Analytics', 'Data Analytics'), ('Design & Development', 'Design & Development'), ('Big Data Science & AI', 'Big Data Science & AI'), (' Training and Development', ' Training and Development '), ('Blockchain Technology', 'Blockchain Technology')], default='Network', max_length=9999),
        ),
    ]
