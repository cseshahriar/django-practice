from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from estates.models import Location, Property  # noqa


def estate_property_defer(request):
    property_list = Property.objects.select_related('location').defer(  # column level
        "description",
        'location__state',  # exclude from sql
        'location__country',  # exclude from sql
        'location__zip_code',  # exclude from sql
    )

    # Paginate by 10 per page
    paginator = Paginator(property_list, 10)
    page = request.GET.get('page')

    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        properties = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        properties = paginator.page(paginator.num_pages)

    context = {
        'properties': properties
    }
    template = "estates/index.html"
    return render(request, template, context)


def estate_property_only(request):
    property_list = Property.objects.select_related('location').only(  # column level
        'name',
        'property_type',
        'location',
        'square_feet',
        'bedrooms',
        'bathrooms',
        'location__city'  # sql only select this field from location
    )

    # Paginate by 10 per page
    paginator = Paginator(property_list, 10)
    page = request.GET.get('page')

    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        properties = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        properties = paginator.page(paginator.num_pages)

    context = {
        'properties': properties
    }
    template = "estates/index.html"
    return render(request, template, context)


def estate_property_exclude(request):
    property_list = Property.objects.select_related('location').exclude(  # row level
        property_type='TOWNHOUSE'
    )

    # Paginate by 10 per page
    paginator = Paginator(property_list, 10)
    page = request.GET.get('page')

    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        properties = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        properties = paginator.page(paginator.num_pages)

    context = {
        'properties': properties
    }
    template = "estates/index.html"
    return render(request, template, context)


def estate_property_only_performance(request):
    queryset = Property.objects.select_related('location').only(  # column level
        'name',
        'property_type',
        'location',
        'square_feet',
        'bedrooms',
        'bathrooms',
        'location__city'  # sql only select this field from location
    )
    property_list = []
    for obj in queryset:
        property_list.append({
            'name': obj.name,
            'property_type': obj.property_type,
            'location__city': obj.location__city,
            'square_feet': obj.square_feet,
            'bedrooms': obj.bedrooms,
            'bathrooms': obj.bathrooms,
        })
    # Paginate by 10 per page
    paginator = Paginator(property_list, 10)
    page = request.GET.get('page')

    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        properties = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        properties = paginator.page(paginator.num_pages)

    context = {
        'properties': properties
    }
    template = "estates/index.html"
    return render(request, template, context)
