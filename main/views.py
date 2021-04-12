from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

#def home(response):
#    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters').json()
#    return render(response, 'main/lists.html', {'response':response})

def home(response):
    tBCS = 1
    tBB = 1
    sBCS = [1]
    sBB = [1]
    eBCS = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    eBB = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    
    for e in eBB:
        if int(e["season"]) > tBB:
            tBB = int(e["season"])
            sBB.append(tBB)
    for c in eBCS:
        if int(c["season"]) > tBCS:
            tBCS = int(c["season"])
            sBCS.append(tBCS)
    
    #for i in range(1, tBCS+1):
    #    sBCS.append(i)
    #for i in range(1, tBB+1):
    #    sBB.append(i)
    
    seasons = {"BB": sBB, "BCS": sBCS}

    return render(response, "main/home.html", {'seasons': seasons})

#def aux(response):
#    personajes = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters').json()
#    return render(response, 'main/lists.html', {'personajes': personajes})

def bbad(response, s):
    caps_1 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    caps1 = []
    for capitulo in caps_1:
        if int(capitulo["season"]) == int(s):
            caps1.append(capitulo)

    return render(response, "main/breakingbad.html", {'caps1': caps1})

def bcsaul(response, s):
    caps_2 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    #print(type(caps_2))
    caps2 = []
    for capitulo in caps_2:
        if int(capitulo["season"]) == int(s):
            caps2.append(capitulo)
    return render(response, "main/bettercallsaul.html", {'caps2': caps2})

def episodes(response, id):
    episodio = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes/{}'.format(id)).json()
    
    aux = []
    data = {"episodio": [], "personajes": []}

    for per in episodio[0]["characters"]:
        aux_2 = per
        aux_3 = aux_2.replace(' ', '+')
        aux.append([aux_2, aux_3])
    
    for char in aux:
        info = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={}'.format(char[1])).json()
        info_2 = info[0]
        char.append(info_2["char_id"])

    data["episodio"] = episodio
    data["personajes"] = aux

    return render(response, "main/episodes.html", {'data': data})

def characters(response, cid):
    personaje = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters/{}'.format(cid)).json()
    aux_quote = personaje[0]["name"]
    aux_quote2 = aux_quote.replace(' ', '+')
    quotes = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/quote?author={}'.format(aux_quote2)).json()

    return render(response, "main/characters.html", {'personaje': personaje, 'quotes': quotes})