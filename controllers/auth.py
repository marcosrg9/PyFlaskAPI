from flask import session, request, Response, json

def login():
    response = Response()
    body = request.get_json()

    if (body['user'] or body['pass']) is None:
        response.status_code = 404
        resp = {
            "Error": "Usuario o contraseña vacíos"
        }
        return resp

    if body['user'] == 'Marcos':
        if body['pass'] == '1234':
            resp = {
                "name": "Marcos",
                "surnames": "Rodríguez Yélamo",
                "birthdate": "19/09/1999",
                "fav_col": "turquoise"
            }
            session['name'] = 'Marcos'
            session['email'] = 'marcosylrg@gmail.com'

            return resp

    else:
        response.status_code = 404
        response.content_type = 'application/json'
        return '{ "Error": "Usuario no encontrado" }'

def getSession():
    if session['name'] is None:
        return 'Null'
    else:
        resp = {
            "name": session['name'],
            "email": session['email']
        }
        return resp