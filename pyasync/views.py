from django.shortcuts import render
import time, asyncio
from django.http import HttpResponse
from asgiref.sync import sync_to_async
from .models import Movie, Story



# helpers func
def get_movies():
    print('prepare to get the movies...')
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print('got all movies...')

def get_stories():
    print('prepare to get the stories...')
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print('got all stories...')


@sync_to_async
def get_movies_async():
    print('prepare to get the movies...')
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print('got all movies...')

@sync_to_async
def get_stories_async():
    print('prepare to get the stories...')
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print('got all stories...')

# views
def home_view(request):
    return HttpResponse('test')

def main_view(request):
    """
    prepare to get the movies...
    <QuerySet [<Movie: The Wheel of Time>, <Movie: Afterlife of the Party>]>
    got all movies...
    prepare to get the stories...
    <QuerySet [<Story: Story 1>, <Story: Story2>]>
    got all stories...
    sync total  7.071028709411621
    [05/Sep/2021 17:50:48] "GET /sync/ HTTP/1.1" 200 4
    """
    start_time = time.time()
    get_movies()
    get_stories()
    total = (time.time() - start_time)
    print('sync total ', total) #   4.106471061706543
    return HttpResponse('sync')


async def main_view_async(request):
    """ 
    prepare to get the movies...
    <QuerySet [<Movie: The Wheel of Time>, <Movie: Afterlife of the Party>]>
    got all movies...
    prepare to get the stories...
    <QuerySet [<Story: Story 1>, <Story: Story2>]>
    got all stories...
    async total  7.0133442878723145
    """
    start_time = time.time()
    # task1 and task2 bot running same time, thats async
    task1 = asyncio.ensure_future(get_movies_async())
    task2 = asyncio.ensure_future(get_stories_async())
    await asyncio.wait([task1, task2])
    total = (time.time() - start_time)
    print('async total ', total) #  4.006905794143677
    return HttpResponse('async')
