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

from website.models import Package, Parameter

turbulence_p = Package.objects.get(id='c93f8227-4230-44f7-924b-2338454be100')

'''box_size = Parameter(package=turbulence_p, label='Box Size', name='boxsize', type=Parameter.FLOAT, required=True, display_order=1, default_value=str(0.565487))
box_size.save()'''

num_modes = Parameter(package=turbulence_p, label='Number of Modes', name='nummodes', type=Parameter.INTEGER, required=True, display_order=2, default_value=str(100))
num_modes.save()

grid_res = Parameter(package=turbulence_p, label='Grid Resolution', name='gridres', type=Parameter.INTEGER, required=True, display_order=3, default_value=str(32))
grid_res.save()

deterministic = Parameter(package=turbulence_p, label='Deterministic', name='deterministic', type=Parameter.CHECKBOX, required=True, display_order=4, default_value=True)
deterministic.save()