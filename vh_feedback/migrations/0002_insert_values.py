#0002_insert_values.py
from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    FeedbackType = apps.get_model("vh_feedback", "FeedbackType")
    db_alias = schema_editor.connection.alias
    if len(FeedbackType.objects.using(db_alias).filter(code='FeedBack')) == 0:
    	fbt = FeedbackType.objects.using(db_alias).create(code="FeedBack", title='Сообщение обратной связи')
    	fbt.save()
    if len(FeedbackType.objects.using(db_alias).filter(code='FeedBackCall')) == 0:
    	fbt = FeedbackType.objects.using(db_alias).create(code="FeedBackCall", title='Запрос на обратный звонок')
    	fbt.save()
    

def reverse_func(apps, schema_editor):
    # forwards_func() creates two FeedbackType instances,
    # so reverse_func() should delete them.
    FeedbackType = apps.get_model("vh_feedback", "FeedbackType")
    db_alias = schema_editor.connection.alias
    FeedbackType.objects.using(db_alias).filter(code="FeedBack").delete()
    FeedbackType.objects.using(db_alias).filter(code="FeedBackCall").delete()

class Migration(migrations.Migration):

    dependencies = [('vh_feedback', '0001_initial'),]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]