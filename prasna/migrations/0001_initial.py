# Generated by Django 2.0 on 2017-12-21 04:06

import django.contrib.postgres.fields.ranges
import django.contrib.postgres.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='apple.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='QuizItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('age', django.contrib.postgres.fields.ranges.IntegerRangeField(validators=[django.contrib.postgres.validators.RangeMinValueValidator(1)])),
                ('difficulty', models.IntegerField(choices=[(1, 'Medium'), (2, 'High'), (0, 'Low')], default=0)),
                ('q_text', models.TextField()),
                ('q_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('a_text', models.TextField()),
                ('a_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('a_media_url', models.URLField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prasna.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
