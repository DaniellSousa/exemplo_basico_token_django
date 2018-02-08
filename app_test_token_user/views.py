from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from models import *

from rest_framework.decorators import api_view, permission_classes, authentication_classes


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def _cadastrar_user(request):
    try:
        nome = request.data.get("nome")
        email = request.data.get("email")
        senha = request.data.get("senha")

        user = UserApp()
        user.first_name = nome
        user.username = str(nome).replace(" ", "")
        user.password = senha

        user.nome = nome
        user.email_app = email
        user.email = email
        user.senha = senha

        user.save()

        t = Token(user=user)
        t.save()

        return Response({"status": 200, "success": True, "message": "sucessoCadastro"})
    except Exception, e:
        return Response({"status": 300, "success": False, "message": "failInternoCadastro"})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def _login_user(request):
    try:
        email = request.data.get("email")
        senha = request.data.get("senha")

        if UserApp.objects.filter(email_app=email, senha=senha).count() <= 0:
            return Response({"status": 500, "success": False, "message": "naoTem", "user": None})

        u = UserApp.objects.get(email=email, senha=senha)

        t = Token.objects.get(user=u)

        objUser = {
            "id": u.id,
            "nome": u.nome,
            "email": u.email_app,
            "senha": u.senha,
            "token": str(t.key)
        }

        return Response({"status": 200, "success": True, "message": "show", "user": objUser})
    except Exception, e:
        return Response({"status": 300, "success": False, "message": "show", "user": None})


@api_view(["POST"])
@permission_classes([IsAuthenticated, ])
def _edit_nome_user(request):
    try:
        novo_nome = request.data.get("nn")
        id_u = request.data.get("id_u")

        u = UserApp.objects.get(id=id_u)
        u.nome = novo_nome
        u.first_name = novo_nome

        u.save()

        return Response({"status": 200, "success": True, "message": "sucessoEditCadastro"})
    except Exception, e:
        return Response({"status": 200, "success": True, "message": "failInternoEditCadastro"})