# Generated by Django 4.1.6 on 2023-02-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0005_alter_bb_rubric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=models.SET(0), to='bboard.rubric', verbose_name='Рубрика'),
        ),
    ]
