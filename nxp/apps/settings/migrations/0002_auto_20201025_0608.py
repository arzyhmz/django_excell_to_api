# Generated by Django 3.1.2 on 2020-10-25 06:08

from django.db import migrations, models
import nxp.core.utils


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='img_value',
            field=models.ImageField(blank=True, null=True, upload_to=nxp.core.utils.FilenameGenerator(prefix='settings')),
        ),
        migrations.AlterField(
            model_name='settings',
            name='name',
            field=models.CharField(choices=[('text_before_service', 'text_before_service'), ('about_us_title', 'about_us_title'), ('about_us_description', 'about_us_description'), ('about_us_img', 'about_us_img'), ('our_portfolio_title', 'our_portfolio_title'), ('our_portfolio_description', 'our_portfolio_description'), ('our_service_title', 'Our Service Title'), ('our_service_description', 'Our Service Description'), ('price_title', 'price_title'), ('price_description', 'price_description'), ('blog_title', 'blog_title'), ('blog_desc', 'blog_desc'), ('map_title', 'map_title'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('contact_us_text', 'contact_us_text'), ('contact_us_description', 'contact_us_description'), ('contact_us_description_2', 'contact_us_description_2'), ('address', 'address'), ('phone', 'phone'), ('email', 'email'), ('website', 'website'), ('logo', 'logo')], max_length=254, unique=True),
        ),
    ]
