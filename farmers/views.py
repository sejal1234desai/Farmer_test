from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Farmer, TreeSpecies
from django.http import HttpResponseForbidden
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Farmer, TreeSpecies
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import Farmer


@login_required
def manage_farmers(request):
    role = request.user.teammember.role  
    can_add_farmer = role in ['Field Executive', 'Senior Manager']  
    # Handle adding a farmer ##(only for Field Executives and Senior Managers)
    if request.method == 'POST' and can_add_farmer:
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        field_photo = request.FILES.get('field_photo')
        plot_location = request.POST.get('plot_location')
        tree_species = request.POST.get('tree_species')

        ## Save farmer record
        farmer = Farmer.objects.create(
            name=name,
            contact=contact,
            field_photo=field_photo,
            plot_location=plot_location,
            added_by=request.user 
           
        )

        ## Save tree species details
        for species_data in tree_species.split(','):
            species_name, quantity = species_data.split('-')
            TreeSpecies.objects.create(farmer=farmer, species_name=species_name.strip(), quantity=int(quantity.strip()))

        return redirect('manage_farmers')  
    # Fetch farmers to display based on the user's role
    if role == 'Field Executive':
       farmers = Farmer.objects.filter(added_by=request.user)  # #Show only the logged-in user's farmers
    else:
        farmers = Farmer.objects.all() 

    return render(request, 'farmers/manage_farmers.html', {'farmers': farmers, 'role': role, 'can_add_farmer': can_add_farmer})




def is_senior_user(user):
    return user.is_staff 

@login_required
@user_passes_test(is_senior_user)
def edit_farmer(request, pk):
    farmer = get_object_or_404(Farmer, id=pk)

    if request.method == 'POST':
       
        print(request.POST)
        
        
        farmer.name = request.POST.get('name')
        farmer.contact = request.POST.get('contact')
        field_photo = request.FILES.get('field_photo')
        farmer.plot_location = request.POST.get('plot_location')

        if field_photo:  
            farmer.field_photo = field_photo

        
        print(f"Name: {farmer.name}, Contact: {farmer.contact}, Plot Location: {farmer.plot_location}")

        try:
            farmer.save()
            messages.success(request, 'Farmer details updated successfully.')
            return redirect('manage_farmers')  # Redirect to manage farmers page
        except Exception as e:
            print(f"Error saving farmer: {e}")
            messages.error(request, 'Error updating farmer details.')

    return render(request, 'farmers/edit_farmer.html', {'farmer': farmer})




@login_required
def delete_farmer(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    if request.user.teammember.role != 'Senior Manager':
        return HttpResponseForbidden("You are not authorized to delete this farmer.")
    farmer.delete()
    return redirect('manage_farmers')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                
                auth_login(request, user)
                # Redirect based on role
                role = user.teammember.role
                if role == 'Field Executive':
                    return redirect('manage_farmers')  
                elif role == 'Field Manager':
                    return redirect('manage_farmers')  # Managers can view data
                elif role == 'Senior Manager':
                    return redirect('manage_farmers')  # Senior Manager manages data
            else:
                messages.error(request, "Invalid password")
        except User.DoesNotExist:
            messages.error(request, "User does not exist")
            
    return render(request, 'farmers/login.html')

def custom_logout(request):
    auth_logout(request)
    return redirect('login')