from django.db import models


from django.db import models
from django.contrib.auth.models import User

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    field_photo = models.ImageField(upload_to='field_photos/')
    plot_location = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TreeSpecies(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name="tree_species")
    species_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.species_name} ({self.quantity})"

class ImplementationDetail(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name="implementations")
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Implementation for {self.farmer.name}"

class TeamMember(models.Model):
    ROLES = (
        ('Field Executive', 'Field Executive'),
        ('Field Manager', 'Field Manager'),
        ('Senior Manager', 'Senior Manager'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES)
   
    def __str__(self):
        return f"{self.user.username} ({self.role})"

