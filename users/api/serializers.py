from rest_framework.serializers import ModelSerializer, CharField, Serializer


# Serializer for the User model
class UserSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ("username", "email", "password", "date_joined")
        write_only_fields = ("password")


# Serializer for updating passwords
class PasswordSerializer(Serializer):

    old_password = CharField(required=True)
    new_password = CharField(required=True)