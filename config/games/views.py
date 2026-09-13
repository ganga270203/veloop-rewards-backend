from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Game, Score
from .serializers import GameSerializer, ScoreSerializer


# =========================
# GAME LIST
# =========================

class GameListView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


# =========================
# GAME DETAIL
# =========================

class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


# =========================
# SCORE LIST
# =========================

class ScoreListView(generics.ListCreateAPIView):
    serializer_class = ScoreSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Score.objects.filter(
            user=self.request.user
        ).order_by("-played_at")

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


# =========================
# LOGIN
# =========================

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {
                    "error": "Username and password are required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:
            return Response(
                {
                    "error": "Invalid username or password."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, created = Token.objects.get_or_create(
            user=user
        )

        return Response(
            {
                "message": "Login successful",
                "token": token.key,
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
            },
            status=status.HTTP_200_OK
        )


# =========================
# REGISTER
# =========================

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        username = request.data.get(
            "username",
            ""
        ).strip()

        email = request.data.get(
            "email",
            ""
        ).strip()

        password = request.data.get(
            "password",
            ""
        )

        # Username validation
        if not username:
            return Response(
                {
                    "error": "Username is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Password validation
        if not password:
            return Response(
                {
                    "error": "Password is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check username
        if User.objects.filter(
            username=username
        ).exists():

            return Response(
                {
                    "error": "Username already exists."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check email
        if email and User.objects.filter(
            email=email
        ).exists():

            return Response(
                {
                    "error": "Email already exists."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create token
        token, created = Token.objects.get_or_create(
            user=user
        )

        return Response(
            {
                "message": "Registration successful",
                "token": token.key,
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
            },
            status=status.HTTP_201_CREATED
        )