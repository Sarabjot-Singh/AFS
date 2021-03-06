# Generated by Django 3.0.7 on 2020-07-14 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_pic', models.ImageField(default='...', upload_to='profile_pics')),
                ('qr_code', models.ImageField(upload_to='qr_codes')),
                ('mobile', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('balance', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
