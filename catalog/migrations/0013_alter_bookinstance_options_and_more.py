# Generated by Django 4.2.1 on 2023-06-27 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0012_remove_book_isbn"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookinstance",
            options={"ordering": ["date_posted"]},
        ),
        migrations.RenameField(
            model_name="bookinstance",
            old_name="swapped_with",
            new_name="user",
        ),
    ]
