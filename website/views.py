from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Package, Parameter
import uuid
import json

# Create your views here.
def run(request, package_id):
    try:
        package_uuid = uuid.UUID(package_id)
    except ValueError:
        raise Http404("Package ID is not valid")

    package = get_object_or_404(Package, pk=package_id)
    parameter_dicts = [param.as_dict() for param in package.parameter_set.all()]
    parameter_json = json.dumps({'data': parameter_dicts}, sort_keys=True)

    parameter_type_abbreviations_json = json.dumps(Parameter.type_abbreviations())

    return render(request, 'website/run.html', {
        'package': package,
        'parameter_json': parameter_json,
        'parameter_type_abbreviations_json': parameter_type_abbreviations_json,
        'package_id': package_id
    })


def run_process(request, package_id):
    return HttpResponse()


def setup(request):
    package = Package(label="Test Package", short_description="This is a test package", long_description="This is a test package, which we will use for testing")
    package.save()

    return HttpResponse("<html><body>It done</body></html>")