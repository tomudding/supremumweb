from flask import render_template, jsonify, abort, Response
from . import infima_bp as infima

from app.infima.forms import SubmitForm, SearchForm
from app.supremum.models import Supremum
from app.infima.models import Infimum

import re
from datetime import datetime

@infima.route('/', methods=['GET', 'POST'])
def infima_overview():
    form = SearchForm()

    # Get search results if present.
    search_results = []
    if form.validate_on_submit():
        infima = Infimum.search(form.search_term.data)
        search_results = [inf.format_public() for inf in infima]

    # Get editions
    suprema = Supremum.get_all_published_editions()
    editions = [sup.format_public() for sup in suprema]

    return render_template('infima_overview.html', editions=editions,
        form=form, search_results=search_results), 200


@infima.route('/<string:edition>')
def infima_for_edition(edition):
    # Retrieve supremum based on edition information.
    try:
        res = re.match('(?P<volume_nr>\d*).(?P<edition_nr>\d)\Z', edition)
        volume_nr, edition_nr = res.group('volume_nr'), res.group('edition_nr')
        supremum = Supremum.get_supremum_by_volume_and_edition(volume_nr, edition_nr)
        if supremum is None:
            raise ValueError("This edition does not exist")
    except Exception as e:
        return abort(Response(str(e)))

    # Retrieve infima
    results = Infimum.get_infima_with_supremum_id(supremum.id)
    infima = [inf.format_public() for inf in results]

    return render_template('infima_edition.html', infima=infima,
        volume_nr=volume_nr, edition_nr=edition_nr), 200

@infima.route('/submit', methods=['GET', 'POST'])
def submit():
    form = SubmitForm()
    if form.validate_on_submit():
        content = form.infimum_text.data
        submission_date = datetime.now()
        Infimum.create(content=content, submission_date=submission_date, rejected=False)
        return render_template('submit.html', success=True), 200
    return render_template('submit.html', form=form), 200

@infima.route('/random_infimum')
def get_random_infimum():
    random_infimum = Infimum.get_random_infimum()
    if random_infimum is None:
        return jsonify({"msg": "No eligible infimum was found"}), 404

    formatted_infimum = random_infimum.format_public()
    return jsonify(formatted_infimum), 200