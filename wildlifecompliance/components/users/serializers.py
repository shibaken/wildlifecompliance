from django.conf import settings
from ledger.accounts.models import EmailUser,Address,Profile,EmailIdentity
from wildlifecompliance.components.organisations.models import (   
                                    Organisation,
                                    OrganisationRequest,
                                    OrganisationContact
                                )
from wildlifecompliance.components.organisations.utils import can_admin_org,is_consultant
from rest_framework import serializers
from django.core.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault


class UserOrganisationContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganisationContact
        fields=(
            'user_status',
            'user_role',
            'email',
            )


class UserOrganisationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='organisation.name')
    abn = serializers.CharField(source='organisation.abn')
    email = serializers.SerializerMethodField()
    is_consultant = serializers.SerializerMethodField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta():
        model = Organisation
        fields = (
            'id',
            'name',
            'abn',
            'email',
            'is_consultant',
            'is_admin'
        )

    def get_is_admin(self,obj):
        user =  self.context['request'].user
        # Check if the request user is among the first five delegates in the organisation
        return can_admin_org(obj,user)

    def get_is_consultant(self,obj):
        user =  self.context['request'].user
        # Check if the request user is among the first five delegates in the organisation
        return is_consultant(obj,user)

    def get_email(self,obj):
        request = self.context.get('request')
        email = request.user.email
        # email = request.user.email
        return email


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailUser
        fields = (
            'id',
            'email',
            'phone_number',
            'mobile_number',
        )

    def validate(self, obj):
        if not obj.get('phone_number') and not obj.get('mobile_number'):
            raise serializers.ValidationError('You must provide a mobile/phone number')
        return obj


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'line1',
            'line2',
            'line3',
            'locality',
            'state',
            'country',
            'postcode',
        )


class UserProfileSerializer(serializers.ModelSerializer):
    postal_address = UserAddressSerializer()
    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'name',
            'email',
            'institution',
            'postal_address'
        )

    def create(self, validated_data):
        profile = Profile()
        profile.user = validated_data['user']
        profile.name = validated_data['name']
        profile.email = validated_data['email']
        profile.institution = validated_data.get('institution','')
        postal_address_data = validated_data.pop('postal_address')
        if profile.email:
            if EmailIdentity.objects.filter(email=profile.email).exclude(user=profile.user).exists():
                #Email already used by other user in email identity.
                raise ValidationError("This email address is already associated with an existing account or profile.")
        new_postal_address, address_created = Address.objects.get_or_create(user=profile.user,**postal_address_data)
        profile.postal_address = new_postal_address
        setattr(profile, "auth_identity", True)
        profile.save()
        return profile


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.institution = validated_data.get('institution', instance.institution)
        postal_address_data = validated_data.pop('postal_address')
        if instance.email:
            if EmailIdentity.objects.filter(email=instance.email).exclude(user=instance.user).exists():
                #Email already used by other user in email identity.
                raise ValidationError("This email address is already associated with an existing account or profile.")
        postal_address, address_created = Address.objects.get_or_create(user=instance.user,**postal_address_data)
        instance.postal_address = postal_address
        setattr(instance, "auth_identity", True)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    # wildlifecompliance_organisations = UserOrganisationSerializer(many=True)
    residential_address = UserAddressSerializer()
    personal_details = serializers.SerializerMethodField()
    address_details = serializers.SerializerMethodField()
    contact_details = serializers.SerializerMethodField()

    class Meta:
        model = EmailUser
        fields = (
            'title',
            'id',
            'last_name',
            'first_name',
            'dob',
            'email',
            'residential_address',
            'phone_number',
            'mobile_number',
            'fax_number',
            'character_flagged',
            'character_comments',
            'wildlifecompliance_organisations',
            'personal_details',
            'address_details',
            'contact_details'
        )


    def get_personal_details(self,obj):
        return True if obj.last_name  and obj.first_name  and obj.dob else False

    def get_address_details(self,obj):
        return True if obj.residential_address else False

    def get_contact_details(self,obj):
        if obj.mobile_number and obj.email:
            return True
        elif obj.phone_number and obj.email:
            return True
        elif obj.mobile_number and obj.phone_number:
            return True
        else:
            return False

    def __init__(self,*args,**kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.fields['wildlifecompliance_organisations'] = UserOrganisationSerializer(many=True,context={'request':request})
   

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailUser
        fields = (
            'id',
            'last_name',
            'first_name',
            'dob',
        )


class EmailIdentitySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = EmailIdentity 
        fields = (
			'user',
			'email'
        )


