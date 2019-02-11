# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import Flask
from flask import render_template, request, redirect, url_for, abort, flash
from modele import Klasa, Uczen*
from forms import *

app = Flask(__name__)

@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')
    
@app.route("/lista")
def lista():
    uczniowie = Uczen.select()
    return render_template('lista.html', uczniowie=uczniowie)
   
def flash_errors(form):
    """Odczytanie wszystkich błędów formularza i przygotowanie komunikatów"""
    for field, errors in form.errors.items():
        for error in errors:
            if type(error) is list:
                error = error[0]
            flash("Błąd: {}. Pole: {}".format(
                error,
                getattr(form, field).label.text))
    
@app.route("/dodaj", methods = ['GET', 'POST'])
def dodaj():
    
    form = DodajForm()
    form.kategoria.choices = [(k.id, k.nazwa) for k in Klasa.select()]
    
    if form.validate_on_submit():
        print(form.data)
        u = Uczen(imie=form.imie.data, nazwisko=form.nazwisko.data, plec=form.plec.data, u_id=form.klasa.data)
        u.save()
        
            
        flash("Dodano ucznia: {}".format(form.imie.data, form.nazwisko.data))
        return redirect(url_for('lista'))
    
    elif request.method == 'POST':
        flash_errors(form)
    
    return render_template('dodaj.html', form=form)
    
@app.route("/dodaj_klasy", methods = ['GET', 'POST'])
def dodaj_klasy():
    
    form = DodajKlasaForm()
    
     if form.validate_on_submit():
        print(form.data)
        k = Klasa(nazwa=form.nazwa.data, roknaboru=form.nazzwa.data, rokmatury=form.nazwa.data)
        u.save()
    
    
    
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


