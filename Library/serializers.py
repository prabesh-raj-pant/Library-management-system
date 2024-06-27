from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

class MemberSerializer(serializers.ModelSerializer):
    Member_id=serializers.IntegerField(required=True)
    class Meta:
        models=Member
        fields="__all__"

class LoanSerializer(serializers.ModelSerializer):
    Member_id=serializers.IntegerField(required=True)
    class meta:
        models=Loan
        fields="__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        models=Author
        fields="__all__"

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        models=Librarian
        fields="__all__"

