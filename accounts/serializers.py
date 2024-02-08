from rest_framework import serializers
from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "username",
            "is_superuser",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        if validated_data["is_superuser"] is False:
            new_user = Account.objects.create_user(**validated_data)
        else:
            new_user = Account.objects.create_superuser(**validated_data)
        return new_user
