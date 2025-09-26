from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.CreateModel(
            name='BatDongSan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_du_an', models.CharField(max_length=200)),
                ('gia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dia_chi', models.CharField(max_length=255)),
                ('ngay_tao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
