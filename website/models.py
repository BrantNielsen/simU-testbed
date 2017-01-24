import uuid
from django.db import models

# Create your models here.
class HashTest(models.Model):
    value = models.CharField(max_length=50)
    value_hash = models.BinaryField(db_index=True)


class Package(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    label = models.CharField(max_length=100)
    short_description = models.CharField(max_length=2000, null=True)
    long_description = models.TextField(null=True)


class Parameter(models.Model):
    INTEGER = 'INT'
    STRING = 'STR'
    FLOAT = 'FLT'
    FILE = 'FLE'
    SELECT = 'SCT'
    RADIO = 'RDO'
    CHECKBOX = 'CHK'

    TYPE_CHOICES = (
        (INTEGER, 'Integer'),
        (STRING, 'String'),
        (FLOAT, 'Float'),
        (FILE, 'File'),
        (SELECT, 'Select'),
        (RADIO, 'Radio'),
        (CHECKBOX, 'Checkbox')
    )

    package = models.ForeignKey('Package', on_delete=models.CASCADE)
    parent_option = models.ForeignKey('Option', on_delete=models.CASCADE, related_name='parent_option')
    name = models.CharField(max_length=50)

    type = models.CharField(max_length=3, choices=TYPE_CHOICES)

    required = models.BooleanField()
    help = models.CharField(max_length=300, null=True, blank=True)
    display_order = models.IntegerField()

    default_value = models.CharField(max_length=300, null=True, blank=True)

    min_value = models.FloatField(null=True)
    max_value = models.FloatField(null=True)


class Option(models.Model):
    parameter = models.ForeignKey('Parameter', on_delete=models.CASCADE)
    value = models.CharField(max_length=50)
    label = models.CharField(max_length=100)


class Run(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    package = models.ForeignKey('Package', on_delete=models.CASCADE)

    argument_hash = models.BinaryField(db_index=True)

    queue_time = models.DateTimeField(null=True)
    run_start_time = models.DateTimeField(null=True)
    run_end_time = models.DateTimeField(null=True)

    error = models.NullBooleanField()


class RunArgument(models.Model):
    run = models.ForeignKey('Run', on_delete=models.CASCADE)
    parameter = models.ForeignKey('Parameter')
    value = models.CharField(max_length=300, blank=True, null=True)
    file_hash = models.BinaryField()


def run_file_path(instance, filename):
    filename_parts = filename.split('.')
    # Ternary operations in Python are freaking off-the-wall weird. What were they thinking?
    file_extension = '.' + filename[-1] if len(filename_parts) > 1 else ''

    return 'runfiles/' + bytes(instance.hash).hex() + file_extension


class RunFile(models.Model):
    hash = models.BinaryField(db_index=True, unique=True)
    file = models.FileField(upload_to=run_file_path)
    size = models.IntegerField()
    mime_type = models.CharField(max_length=100)


class RunFileAssociation(models.Model):
    run = models.ForeignKey('Run')
    run_file = models.ForeignKey('RunFile')
    path = models.CharField(max_length=300)