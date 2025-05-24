from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("students", '0002_remove_student_email'),
    ]
    operations = [
        migrations.AddField(
            model_name="student",
            name='marks',
            field=models.FloatField(default=0),
        ),
        migrations.RemoveField(
            model_name="student",
            name='grade',
        ),
        migrations.AddField(
            model_name="student",
            name="student_class",
            field=models.CharField(default=0),
            preserve_default=False,
        ),
    ]