from django.shortcuts import render, redirect
import bcrypt
from cryptography.fernet import Fernet
from .models import User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']


         # Generate encryption key
        # encryption_key = Fernet.generate_key()
        # cipher = Fernet(encryption_key)

        # Encrypt the password
        # encrypted_password = cipher.encrypt(password.encode('utf-8'))

        # Hash the password
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
       
       
        #create a user
        user = User.objects.create(
            username=username,
            password=hashed_password,
            email=email,
            phone=phone
        )
        user.save()
        return redirect('login')

    return render(request, 'signup.html')    
        

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            hashed_password = user.password

            # Compare the provided password with the hashed password
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                return redirect('home')
            
            else:
                #handle the invalid login attempt
                context = {
                    'error': 'Invalid username or password'
                }
                return render(request, 'login.html', context)

        except User.DoesNotExist:
            context = {
                'error': 'Invalid username or password'
            }
            return render(request, 'login.html', context)

    return render(request, 'login.html')


#i'll get back to this in a bit