# Generated by Django 3.2.23 on 2024-02-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0038_enterpriseoffer_export_timestamp'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='enterpriselearnerenrollment',
            index=models.Index(fields=['enterprise_customer_uuid', 'enterprise_user_id', 'user_current_enrollment_mode'], name='enterprise__enterpr_6b0be8_idx'),
        ),
        migrations.AddIndex(
            model_name='enterpriselearnerenrollment',
            index=models.Index(fields=['enterprise_customer_uuid', 'offer_id', 'budget_id'], name='enterprise__enterpr_66e37f_idx'),
        ),
        migrations.AddIndex(
            model_name='enterpriselearnerenrollment',
            index=models.Index(fields=['enterprise_customer_uuid', 'user_current_enrollment_mode', 'coupon_code', 'offer_type'], name='enterprise__enterpr_1e8e98_idx'),
        ),
    ]
