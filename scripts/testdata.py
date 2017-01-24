import binascii
import hashlib

import sys
import django
import os
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))

from django.conf import settings as django_settings
from testproject import settings as app_settings

#django_settings.configure(app_settings)
os.environ['DJANGO_SETTINGS_MODULE'] = 'testproject.settings'
django.setup()
#print(sys.path)

from django.apps import apps

#print(apps.get_app_configs())

from website.models import HashTest

'''testvalue = "Beware of the man who speaks in hands"

testhash = hashlib.sha1()
testhash.update(testvalue.encode())

testmodel = HashTest(value=testvalue, value_hash=testhash.digest())

testmodel.save()'''

testvalue = "Beware of the man who speaks in hands"

testhash = hashlib.sha1()
testhash.update(testvalue.encode())

print(testhash.hexdigest())

result_set = HashTest.objects.filter(value_hash=testhash.digest())

for result in result_set:
    print(result.value)
    print(bytes(result.value_hash).hex())