from http.client import HTTPResponse, HTTPResponseNotFound, HTTPResponseRedirect
from django.shortcuts import render

# Creo un diccionario con los meses y una descripción sobre que hacer en cada mes
monthly_challenges = {
    'January': 'Disfrutar de la playa y del sol',
    'February': 'Disfrutar de la playa y de paseos frente al mar',
    'March': 'Retomando de a poco los horarios de oficina',
    'April': 'Disfrutar de las vacaciones de turismo',
    'May': 'Ir al cumpleaños de un amigo',
    'June': 'Se vino el frío, debo permanecer en casa',
    'July': 'Sigue el frío, debo permanecer en casa',
    'August': 'Es el cumpleaños de mi hijo, debo ir a verlo',
    'September': 'Empezar el deporte y la dieta',
    'October': 'Es el mes de mi cumpleaños, me encantaría festejarlo',
    'November': 'Empieza a hacer calor nuevamente, ¿por qué no ir a la playa?',
    'December': 'Es el mes de los amigos, after office, fiestas, despedidas, etc',
}

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months) or month < 1:
        return HTTPResponseNotFound('<h1>404</h1><p>No se encontró el mes</p>')
    redirect_month = months[month-1]
    return HTTPResponseRedirect("/challenges/"+redirect_month)
    

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HTTPResponse(challenge_text)
    except:
        return HTTPResponseNotFound('<h1>404</h1><p>No se encontró el mes</p>')

# este es un comentario para ver si funciona el pull request
    
