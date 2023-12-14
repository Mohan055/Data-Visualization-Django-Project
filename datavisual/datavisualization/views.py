from django.shortcuts import render
import json
from .models import DataModel




# Create your views here.

def index(request):
    modeldata = DataModel.objects.all()
    with open('jsondata.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            likelihood_value = item.get('likelihood')
            try:
                likelihood_value = int(likelihood_value)  # Attempt to convert to an integer
            except (ValueError, TypeError):
                likelihood_value = 0  # Set a default value for likelihood if the value is not a valid integer


            data_model = DataModel(
                end_year=item.get('end_year') if item.get('end_year') else None,
                intensity=item.get('intensity') if item.get('intensity') else None,
                sector=item.get('sector'),
                topic=item.get('topic'),
                insight=item.get('insight'),
                url=item.get('url'),
                region=item.get('region') if item.get('region') else None,
                start_year=item.get('start_year') if item.get('start_year') else None,
                impact=item.get('impact') if item.get('impact') else None,
                added=item.get('added'),
                published=item.get('published'),
                country=item.get('country') if item.get('country') else None,
                relevance=item.get('relevance') if item.get('relevance') else None,
                pestle=item.get('pestle'),
                source=item.get('source'),
                title=item.get('title'),
                likelihood=likelihood_value,
            )
            data_model.save()

    context = {
        'data': data,
        'modeldata':modeldata,
    }

    return render(request, 'dashboard/index.html', context)


