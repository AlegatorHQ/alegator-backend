from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=20, required=False, allow_blank=True)
    _has_phone_field = True

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.phone_number = self.validated_data.get('phone_number')
        user.save()
        return user