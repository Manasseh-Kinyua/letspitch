from flask import Blueprint,render_template,request,flash,jsonify
from flask_login import login_required,current_user
from .models import Pitch
from . import db
import json

views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        pitch = request.form.get('pitch')

        if len(pitch) < 1:
            flash('Pitch is too short', category='error')
        else:
            new_pitch = Pitch(data=pitch, user_id=current_user.id)
            db.session.add(new_pitch)
            db.session.commit()
            flash('Pitch Created!', category='success')
    return render_template('home.html', user=current_user)

@views.route('/delete-pitch', methods=['POST'])
def delete_pitch():
    pitch = json.loads(request.data)
    pitchId = pitch['pitchId']
    pitch = Pitch.query.get(pitchId)
    if pitch:
        if pitch.user_id == current_user.id:
            db.session.delete(pitch)
            db.session.commit()
    return jsonify({})