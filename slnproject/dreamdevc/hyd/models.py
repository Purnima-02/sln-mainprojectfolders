from django.db import models
from django.core.exceptions import ValidationError
import re


def validate_only_letters(value):
    if not re.match('^[A-Za-z ]*$', value):  # Regex to match only letters and spaces
        raise ValidationError('Only letters and spaces are allowed.')

def validate_related_application_number(value):
    # Regular expression that allows only uppercase letters and numbers
    if not re.match("^[A-Z0-9]+$", str(value)):
        raise ValidationError("Related application number must contain only uppercase letters and numbers.")





def validate_mobile_number(value):
    pattern = r'^\+?[1-9]\d{1,14}$'
    if not re.match(pattern, value) or len(value) < 10:
        raise ValidationError('Invalid mobile number format. Must be at least 10 digits long.')
    if len(value) > 15:
        raise ValidationError('Mobile number cannot be more than 15 digits long.')



import re
from django.core.exceptions import ValidationError

def validate_email(value):
    # Pattern to ensure:
    # - Starts with at least one letter (a-zA-Z)
    # - Followed optionally by any combination of letters and/or numbers
    # - Ends with @gmail.com
    pattern = r'^[a-zA-Z]+[a-zA-Z0-9]*@gmail\.com$'

    # Validate against the pattern
    if not re.match(pattern, value):
        raise ValidationError('Invalid email format. The email must start with letters, followed by any combination of letters and numbers, and must end with @gmail.com.')

    # Check for minimum length (5 characters, which is very small, but let's keep it)
    if len(value) < 5:
        raise ValidationError('Email is too short. It must have at least 5 characters.')

    # Check for maximum length (254 characters)
    if len(value) > 254:
        raise ValidationError('Email is too long. Maximum allowed length is 254 characters.')


# Ticket Model
class Ticket(models.Model):
    TICKET_STATUS_CHOICES = [
        ('New', 'New'),
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]
    
    ISSUE_CHOICES = [
        ('personal loan', 'Personal Loan'),
        ('educational loan', 'Educational Loan'),
        ('car loan', 'Car Loan'),
        ('Home Loan', 'Home Loan'),
        ('Gold Loan', 'Gold Loan'),
        ('business loan', 'Business Loan'),
        ('Loan Against Property', 'Loan Against Property'),
        ('CreditCard', 'Credit Card'),
        ('Insurance', 'Insurance'),
        ('Other Loan', 'Other Loan'),
    ]

    ticket_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, validators=[validate_only_letters])
    phone_number = models.CharField(max_length=15, validators=[validate_mobile_number])
    email = models.EmailField(max_length=254, unique=True, validators=[validate_email])
    issue_type = models.CharField(max_length=100, choices=ISSUE_CHOICES) # Use snake_case
    description = models.TextField()
    related_application_number = models.CharField(max_length=100, blank=False, null=False,validators=[validate_related_application_number])
    status = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f'Ticket #{self.ticket_id} - {self.issue_type}'

# DSA Ticket Model
class DSATicket(models.Model):
    ISSUE_TYPE_CHOICES = [
        ('Technical', 'Technical'),
        ('Billing', 'Billing'),
        ('General', 'General'),
        ('Personal', 'Personal'),
        ('Others', 'Others'),
    ]
    
    TICKET_STATUS_CHOICES = [
        ('New', 'New'),
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    
    ticket_id = models.AutoField(primary_key=True)
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, default='New', choices=TICKET_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=25, validators=[validate_only_letters])
    phone_number = models.CharField(max_length=15, validators=[validate_mobile_number])
    email = models.EmailField(max_length=254, unique=True, validators=[validate_email])

    def _str_(self):
        return f'Ticket {self.ticket_id} - {self.issue_type}'

# Franchisee Ticket Model
class FranchiseeTicket(models.Model):
    ISSUE_TYPE_CHOICES = [
        ('Technical', 'Technical'),
        ('Billing', 'Billing'),
        ('General', 'General'),
        ('Personal', 'Personal'),
        ('Others', 'Others'),
    ]
    
    TICKET_STATUS_CHOICES = [
        ('New', 'New'),
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    
    ticket_id = models.AutoField(primary_key=True)
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, default='New', choices=TICKET_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, validators=[validate_only_letters])
    phone_number = models.CharField(max_length=15, validators=[validate_mobile_number])
    email = models.EmailField(max_length=254, unique=True, validators=[validate_email])

    def _str_(self):
        return f'Ticket {self.ticket_id} - {self.issue_type}'


class custmer(models.Model):
    franchise_id = models.CharField(max_length=100, null=True,blank=True)
    name=models.CharField(max_length=100)
    password = models.CharField(max_length=100)
