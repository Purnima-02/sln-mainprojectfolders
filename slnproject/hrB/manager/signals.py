from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee, franchisesales

@receiver(post_save, sender=Employee)
def create_franchisesales_entry(sender, instance, created, **kwargs):
    if created:
        if instance.franchisecode == 'SLNBR001' and instance.employee_type == 'sales':
            franchisesales.objects.create(
                Employe=instance,
                registerid=instance.employee_id,
                franchiseCode=instance.franchisecode,  
                name=instance.username,  
                email=instance.email,
                phone=instance.phone_number,
            )
