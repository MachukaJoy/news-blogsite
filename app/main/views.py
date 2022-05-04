from flask import render_template
from . import main
from ..requests import get_source
from ..requests import get_articles

@main.route('/')
def index():
    general_news=get_source('general')
    articles=get_articles()
    return render_template('home.html',general_news=general_news,articles=articles)

@main.route('/source')
def source():
    general_news=get_source('general')
    return render_template('source.html',general_news=general_news)   


@main.route('/article')
def article():
    # title= 'Articles'
    articles=get_articles()
    return render_template('article.html',articles= articles)