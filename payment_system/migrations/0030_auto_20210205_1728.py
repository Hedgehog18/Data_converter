# Generated by Django 3.0.7 on 2021-02-05 17:28

from django.db import migrations, models


def set_requests(apps, schema):
    Subscription = apps.get_model('payment_system', 'subscription')
    ProjectSubscription = apps.get_model('payment_system', 'ProjectSubscription')
    for sub in Subscription.objects.all():
        if sub.name.lower() == 'enterprise':
            sub.is_custom = True
        if sub.is_default:
            sub.requests_limit = 20
            sub.platform_requests_limit = 200
        else:
            sub.platform_requests_limit = 1000000
        sub.save()

    for p2s in ProjectSubscription.objects.all():
        sub = p2s.subscription
        p2s.requests_left = sub.requests_limit
        p2s.platform_requests_left = sub.platform_requests_limit
        p2s.save()


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0029_invoice_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsubscription',
            name='platform_requests_left',
            field=models.IntegerField(default=1000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectsubscription',
            name='platform_requests_used',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='subscription',
            name='platform_requests_limit',
            field=models.IntegerField(default=1000000, help_text='Limit for API requests from the project via platform'),
            preserve_default=False,
        ),
        migrations.RunPython(
            code=set_requests,
            reverse_code=migrations.RunPython.noop,
        )
    ]
