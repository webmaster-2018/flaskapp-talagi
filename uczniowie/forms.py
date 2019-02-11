# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class KlasaForm(FlaskForm):
    id = HiddenField()
    nazwa = StringField('Nazwa: ', validators=[Required(message="blad_1")])
    roknaboru = BooleanField()
    rokmatury = BooleanField()


class UczenForm(FlaskForm):
    id = HiddenField()
    imie = StringField('Imie: ', validators=[Required(message="blad_1")])
    nazwisko = StringField('Nazwisko: ', validators=[Required(message="blad_1")])
    plec = BooleanField()
    klasa = FieldList(FormField(KlasaForm), min_entries=3)
