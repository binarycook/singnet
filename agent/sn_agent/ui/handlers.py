import logging

import aiohttp_jinja2 as aiohttp_jinja2

logger = logging.getLogger(__name__)


@aiohttp_jinja2.template('index.jinja2')
def index(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}

@aiohttp_jinja2.template('mnistclassifier.jinja2')
def tensorflowmnistclassifier(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}

@aiohttp_jinja2.template('index.jinja2')
def facerecognizer(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}

@aiohttp_jinja2.template('index.jinja2')
def textsummarizer(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}

@aiohttp_jinja2.template('index.jinja2')
def videosummarizer(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}

@aiohttp_jinja2.template('index.jinja2')
def entityextracter(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}

@aiohttp_jinja2.template('index.jinja2')
def documentsummarizer(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}

@aiohttp_jinja2.template('simpleadapter.jinja2')
def simpleadapter(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}

@aiohttp_jinja2.template('index.jinja2')
def wordsensedisamnbiguater(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}

@aiohttp_jinja2.template('relexparser.jinja2')
def relexparser(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}

@aiohttp_jinja2.template('aigentsservices.jinja2')
def aigentsservices(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}
