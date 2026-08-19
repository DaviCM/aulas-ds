from flask_restful import Resource
from webargs.flaskparser import use_args
from marshmallow import fields

from src.schemas.user_schemas import *
from src.services.user_services import *
from src.extensions.api import api

class UserRoutes(Resource):
    @use_args(argmap=CreateUserSchema, location="json")
    def post(self, args):
        """
        parameters:
          - name: body
            description: Payload JSON com as informações do usuário a criar.
            in: body
            required: true
            schema:
              $ref: "#/definitions/CreateUser"

        responses:
          201:
            description: O usuário requisitado foi criado com sucesso.
            schema:
              $ref: "#/definitions/ResponseUser"
          400:
            description: As informações de usuário fornecidas são inválidas.
            schema:
              type: object
            properties:
              status_code:
                type: int
              error:
                type: string
              detail:
                type: string
          409:
            description: O usuário já está cadastrado.
            schema:
              type: object
            properties:
              status_code:
                type: int
              error:
                type: string
              detail:
                type: string
        """
        return ResponseUserSchema.dump(create_user(args)), 201


    @use_args(argmap=UpdateUserSchema, location="json")
    def patch(self, args):
        """
        parameters:
          - name: body
            description: Payload JSON com os parâmetros a editar. Parâmetros opcionais.
            in: body
            required: true
            schema:
              $ref: "#/definitions/UpdateUser"

        responses:
          200:
            description: O usuário requisitado foi atualizado com sucesso.
            schema:
              $ref: "#/definitions/ResponseUser"
          400:
            description: As informações de usuário fornecidas são inválidas.
            schema:
              type: object
            properties:
              status_code:
                type: int
              error:
                type: string
              detail:
                type: string
          404:
            description: O usuário requisitado não foi encontrado.
            schema:
              type: object
            properties:
              status_code:
                type: int
              error:
                type: string
              detail:
                type: string
          409:
            description: O usuário já está cadastrado.
            schema:
              type: object
            properties:
              status_code:
                type: int
              error:
                type: string
              detail:
                type: string
        """
        return ResponseUserSchema.dump(update_user(args)), 200


    @use_args(argmap={"id": fields.Int(required=True)}, location="query")
    def delete(self, args):
        """
        parameters:
          - name: target_user_id
            description: ID do usuário alvo.
            in: path
            type: int
            required: true

        responses:
          201:
            description: O usuário requisitado foi excluído com sucesso.
          404:
            description: O usuário requisitado não foi encontrado.
            schema:
              type: object
            properties:
              status_code:
                type: int
              error:
                type: string
              detail:
                type: string
        """
        delete_user(id=args)
        return 204



class UserLogin(Resource):
    @use_args(argmap=LoginUserSchema, location="json")
    def post(self, args):
        """
        parameters:
          - name: body
            description: Payload JSON com informações do usuário para entrada.
            in: body
            required: true
            schema:
              $ref: "#/definitions/LoginUser"

        responses:
          200:
            description: O usuário foi autenticado com sucesso.
            schema:
              $ref: "#/definitions/ResponseUser"
          401:
            description: As credenciais fornecidas são inválidas.
            schema:
              type: object
            properties:
              status_code:
                type: int
              error:
                type: string
              detail:
                type: string
          404:
            description: O usuário requisitado não foi encontrado.
            schema:
              type: object
            properties:
              status_code:
                type: int
              error:
                type: string
              detail:
                type: string
        """
        return ResponseUserSchema.dump(login(args["email"], args["password"])), 200



api.add_resource(UserRoutes, "/users")
api.add_resource(UserLogin, "/auth")