from django.utils.translation import pgettext_lazy
from rest_framework import serializers

from apps.application_user.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]

    def validate_email(self, email):
        email = email.lower()
        user_exists = User.objects.filter(email__iexact=email)
        if user_exists.exists():
            raise serializers.ValidationError(
                pgettext_lazy(
                    "Serializer validation error", "This email already exists"
                )
            )
        return email

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError(
                pgettext_lazy(
                    "Serializer validation error",
                    "The password needs to length more than 8 characters",
                )
            )
        return password

    def create(self, validated_data):
        user = User(**validated_data)
        user.username = user.email
        user.is_active = True
        user.is_staff = True
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email"]
