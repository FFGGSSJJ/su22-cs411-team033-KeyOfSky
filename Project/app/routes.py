""" Specifies routing for the application"""
from flask import render_template, request, jsonify, session
from app import app
from app import database as db_helper


@app.route("/delete/<int:movie_id>", methods=['POST'])
def delete(movie_id):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_movie_by_id(movie_id)
        result = {'success': True, 'response': 'Removed movie'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:movie_id>", methods=['POST'])
def update(movie_id):
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        db_helper.update_movie_entry(movie_id, data)
        result = {'success': True, 'response': 'Movie Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.insert_new_movie(data)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/search_movie", methods=['POST'])
def search_movie():
    """ search movie"""
    data = request.get_json()
    searched_list = db_helper.search_movie_by_title(data)
    session['movie_list'] = searched_list
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/search_result")
def search_result():
    """ display search result """
    searched_list = session.get('movie_list', None)
    return render_template("search.html", items=searched_list)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_movie()
    return render_template("index.html", items=items)
    # return render_template("index.html")


@app.route("/advancedop")
def rootpage():
    """ returns rendered rootpage """
    return render_template("root.html")
