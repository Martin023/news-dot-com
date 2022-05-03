# Render temp that renders our views

from flask import render_template
from app import app
from .requests import get_sources,get_article


@app.route('/')

def home():
    
    '''
    View root page function that returns the index page and its data
    '''

    # Getting news articles
    sources = get_sources()
    title = 'news.com'

    return render_template('index.html',title = title, sources = sources)


@app.route('/articles/<sources_id>')
def articles(sources_id):
    '''
    View articles page function that returns the  article details page and its data
    '''
    articles = get_article(sources_id)
    
    return render_template('articles.html',articles = articles)