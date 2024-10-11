from rest_framework import serializers
from .models import User,Ticket_Model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class NestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket_Model
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    nested_field = NestedSerializer(read_only=True)

    class Meta:
        model = Ticket_Model
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(TicketSerializer,self).__init__(*args,**kwargs)

        request = self.context.get("request")
        if request:
            method = request.method
            self.adjust_fields_based_on_method(method)
    
    def set_fields(self,exclude_fields_list=None):
        for field in exclude_fields_list:
            self.fields.pop(field)
    
    def adjust_fields_based_on_method(self, method):

        perform_action = self.context.get("perform_action", None)
        
        if method == "PUT" and perform_action is None:
            exclude_fields_list = ["user","price_paid","from_location","to_location"]
            self.set_fields(exclude_fields_list=exclude_fields_list)


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)  
        ticket = Ticket_Model.objects.create(user=user, **validated_data)
        return ticket
    
    
