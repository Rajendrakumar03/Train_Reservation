from django.shortcuts import render,get_object_or_404
from rest_framework import generics,viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User,Ticket_Model
from .serializers import TicketSerializer,UserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password


class Registration(viewsets.ViewSet):

    def post(self,request):
        data = request.data 
        email = data.get('email')
        
        check_email = User.objects.filter(email=email).exists()
        if check_email == True:
            return Response("This email_id is already registered")
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)
    
    def login(self,request):
        email = request.data.get("email")
        password = request.data.get("password")
       
        if not email  or not password :            
            return Response("Username and password is required.")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response("User does not exists.")
        
        if user and check_password(password,user.password):
            return Response("Successfully logged in.")
        return Response("Username or password is invalid")



class PurchaseTicketAPI(viewsets.ViewSet):
    queryset = Ticket_Model.objects.all()
    serializer_class = TicketSerializer

    def get(self,request,*args,**kwargs):
        purchases =Ticket_Model.objects.all()
        serializer_purchase = TicketSerializer(purchases,many=True)
        return Response(serializer_purchase.data)
    
    def post(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        # seat_number = request.data.get('seat')
        # seat_exists = Ticket_Model.objects.filter(seat=seat_number).exists()
        # if seat_exists:
        #     return Response({'message': f"Seat {seat_number} is already booked."},status=status.HTTP_400_BAD_REQUEST)
        
        # serializer = TicketSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,status=status.HTTP_201_CREATED)
        # return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

        data = request.data
        # user_id = request.user.id

        seat_number = data['seat']
        section = data['section']
        seat_exists = Ticket_Model.objects.filter(seat=seat_number,section=section).exists()
        if seat_exists:
            return Response({'message': "This seat is already booked."},status=status.HTTP_400_BAD_REQUEST)
        
        serializer = TicketSerializer(data=data)        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ReceiptDetailAPI(viewsets.ViewSet):

    def get(self,request):
        # import pdb;pdb.set_trace()
        user_email = request.GET.get('email')
        email_check = User.objects.filter(email=user_email).values('id')

        if email_check:

            ticket = Ticket_Model.objects.filter(user__in = email_check).values()
            if ticket:
                return Response(ticket)
            else:
                return Response({'message':'User does not have tickets'})
        else:
            return Response({'message': 'User not found'})

        # ticket = Ticket_Model.objects.filter(user__in =email_check)

        # try:
        #     user = User.objects.get(email=user_email)
        #     ticket = Ticket_Model.objects.get(user__email=user_email)
        #     return ticket
        # except (Ticket_Model.DoesNotExist):
        #     return 'nill'
            
    
class UserBySectionAPI(viewsets.ViewSet):
    # serializer_class = TicketSerializer

    def get(self,request):

        section = request.GET.get('section')
        ticket = Ticket_Model.objects.filter(section__in=section)
        serilaizer = TicketSerializer(ticket,many=True)

        print(serilaizer.data)

        return Response(serilaizer.data)
    
    def get_all_users(self,request):
        users_list = User.objects.all()
        if not users_list.exists():
            return Response("Users not found")
        serializer = UserSerializer(users_list,many=True)
        # print(serializer.data,"*******************")
        return Response(serializer.data)
    
# class RemoveUserAPI(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'email'

#     def delete(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()  
#             self.perform_destroy(instance)
#             return Response("User deleted successfully", status=status.HTTP_204_NO_CONTENT)
#         except User.DoesNotExist:
#             return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)

class RemoveUser(viewsets.ViewSet):

    def destroy(self,request):

        user = request.GET.get('id')
        if user:
            delete_user = User.objects.filter(id__in=user).delete()
            return Response("User deleted Successfully",status=status.HTTP_200_OK)
        else:
            return Response("User does not exists")

 

class ModifySeatAPI(viewsets.ViewSet):

    def update(self,request,*args,**kwargs):
        user_id = request.GET.get('id')
        users = User.objects.filter(id=user_id)
        if not users.exists():
            return Response("User not found")
        
        else:
    
            ticket = Ticket_Model.objects.filter(user__in=user_id)
                
            new_seat_number = request.data.get('seat')
            seat_exists = Ticket_Model.objects.filter(seat=new_seat_number).exists()
            if seat_exists:
                return Response({'message': f"Seat {new_seat_number} is already booked."},status=status.HTTP_400_BAD_REQUEST)
            
            else:
                ticket.seat = new_seat_number
                new_seat = Ticket_Model.objects.filter(user__in=user_id).update(seat=new_seat_number)

                return Response("Seat updated Successfully")
    
        