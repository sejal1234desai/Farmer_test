from django.contrib.auth.models import User, Group, Permission
from farmers.models import TeamMember

def create_roles_and_users():
    # Step 1: Create Groups and Assign Permissions
    roles = {
        'Field Executive': [],  
        'Field Manager': [],    
        'Senior Manager': ['add_farmer', 'change_farmer', 'delete_farmer', 'view_farmer']
    }

    for role, permissions in roles.items():
        group, created = Group.objects.get_or_create(name=role)
        if created:
            print(f"Group '{role}' created.")
        else:
            print(f"Group '{role}' already exists.")

        ## Assign permissions to groups##
        for perm_codename in permissions:
            try:
                perm = Permission.objects.get(codename=perm_codename)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                print(f"Permission '{perm_codename}' does not exist.")

    # Step 2: Create Users and Assign Groups
    users = [
        {'username': 'A', 'role': 'Field Executive'},
        {'username': 'B', 'role': 'Field Executive'},
        {'username': 'C', 'role': 'Field Manager'},
        {'username': 'D', 'role': 'Field Manager'},
        {'username': 'E', 'role': 'Senior Manager'},
    ]

    for user_data in users:
        user, created = User.objects.get_or_create(username=user_data['username'])
        if created:
            user.set_password('sejal1234')  # Default password
            user.save()
            print(f"User '{user_data['username']}' created.")
        else:
            print(f"User '{user_data['username']}' already exists.")

        # # Assign user to group##
        group = Group.objects.get(name=user_data['role'])
        user.groups.add(group)
        print(f"User '{user_data['username']}' added to group '{user_data['role']}'.")

        
        TeamMember.objects.get_or_create(user=user, role=user_data['role'])

    print("All users, roles, and permissions created successfully!")
