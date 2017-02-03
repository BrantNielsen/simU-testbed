import sys
import django
import os
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))

os.environ['DJANGO_SETTINGS_MODULE'] = 'testproject.settings'
django.setup()

'''from website.models import Package

turbulence_p = Package(label="Comte-Bellot Corrsin Spectrum")
turbulence_p.save()'''

from website.models import Package, Parameter, Option

turbulence_p = Package.objects.get(id='4a3cd725-d660-4ac1-9dd6-4a394acb911a')

'''box_size = Parameter(package=turbulence_p, label='Box Size', name='boxsize', type=Parameter.FLOAT, required=True, display_order=1, default_value=str(0.565487))
box_size.save()

num_modes = Parameter(package=turbulence_p, label='Number of Modes', name='nummodes', type=Parameter.INTEGER, required=True, display_order=2, default_value=str(100))
num_modes.save()

grid_res = Parameter(package=turbulence_p, label='Grid Resolution', name='gridres', type=Parameter.INTEGER, required=True, display_order=3, default_value=str(32))
grid_res.save()

deterministic = Parameter(package=turbulence_p, label='Deterministic', name='deterministic', type=Parameter.CHECKBOX, required=True, display_order=4, default_value=True)
deterministic.save()'''

deterministic = Parameter.objects.get(name='deterministic')
'''deterministic.label = None
deterministic.save()

print(deterministic)'''

deterministic_option = Option(parameter=deterministic, label='Deterministic', value=True, display_order=1, is_default=True)
deterministic_option.save()

test_parameter = Parameter(package=turbulence_p, label='Which would you prefer?', name='preference', type=Parameter.RADIO, display_order=5)
test_parameter.save()

test_option1 = Option(parameter=test_parameter, value='banana', label='Bananas', display_order=1)
test_option1.save()

test_option2 = Option(parameter=test_parameter, value='orange', label='Oranges', is_default=True, display_order=2)
test_option2.save()

test_option3 = Option(parameter=test_parameter, value='mango', label='Mangoes', display_order=3)
test_option3.save()