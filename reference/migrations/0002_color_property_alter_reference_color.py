# Generated by Django 4.1.6 on 2023-03-11 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('header', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reference.reference')),
            ],
        ),
        migrations.AlterField(
            model_name='reference',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reference.color'),
        ),
    ]