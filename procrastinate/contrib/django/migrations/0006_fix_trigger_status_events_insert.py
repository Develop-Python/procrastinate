from django.db import migrations

from procrastinate.contrib.django.utils import get_sql


class Migration(migrations.Migration):

    dependencies = [("procrastinate_django", "0005_fix_procrastinate_fetch_job")]

    operations = [
        migrations.RunSQL(
            get_sql("delta_0.7.1_001_fix_trigger_status_events_insert.sql")
        ),
    ]
