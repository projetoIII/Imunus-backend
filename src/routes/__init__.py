'''
Módulo que contém os endpoints de rotas da API.
'''

from flask_restplus import Namespace

authentication_api = Namespace('authentication', description="Endpoints de login e autenticação")
