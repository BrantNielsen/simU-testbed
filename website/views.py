from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Package, Parameter, Option
import uuid
import json

# Create your views here.
def run(request, package_id):
    try:
        package_uuid = uuid.UUID(package_id)
    except ValueError:
        raise Http404("Package ID is not valid")

    package = get_object_or_404(Package, pk=package_id)

    parameters = package.parameter_set.all()

    parameter_dicts = [param.as_dict() for param in parameters]
    parameter_json = json.dumps({'data': parameter_dicts}, sort_keys=True)

    parameter_options = Option.objects.filter(parameter__in=parameters)

    parameter_option_dicts = [option.as_dict() for option in parameter_options]
    parameter_option_json = json.dumps({'data': parameter_option_dicts}, sort_keys=True)

    parameter_type_abbreviations_json = json.dumps(Parameter.type_abbreviations())

    return render(request, 'website/run.html', {
        'package': package,
        'parameter_json': parameter_json,
        'parameter_type_abbreviations_json': parameter_type_abbreviations_json,
        'parameter_options_json': parameter_option_json,
        'package_id': package_id
    })


def run_process(request, package_id):
    return HttpResponse()


def setup(request):
    package = Package(label="Test Package", short_description="This is a test package", long_description="This is a test package, which we will use for testing")
    package.save()

    return HttpResponse("<html><body>It done</body></html>")