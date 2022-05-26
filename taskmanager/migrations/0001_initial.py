from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('deadline', models.DateField(verbose_name='deadline')),
                ('color', models.CharField(choices=[('black', 'black'), ('yellow', 'yellow'), ('blue', 'blue'), ('green', 'green'), ('pink', 'pink')], max_length=8, verbose_name='color')),
                ('repeating_days', models.CharField(blank=True, choices=[('mo', 'mo'), ('tu', 'tu'), ('we', 'we'), ('th', 'th'), ('fr', 'fr'), ('sa', 'sa'), ('su', 'su')], max_length=2, null=True, verbose_name='repeating_days')),
                ('is_archive', models.BooleanField(verbose_name='is_archive')),
                ('is_favorite', models.BooleanField(verbose_name='is_favorite')),
                ('temp_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanager.temporaryuser')),
            ],
            options={
                'verbose_name': 'task',
            },
        ),
    ]
