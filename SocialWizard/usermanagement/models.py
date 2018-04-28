from django.db import models
from django.contrib.auth.models import User

class UserModel(models.Model):
    ########### Relation Choice Constants and Tuple ##############
    SINGLE = "single"
    COMPLICATED = "complicated"
    SEPERATED = "seperated"
    WINDOW = "widow"
    NOT_MENTION = "not_mention"

    RELATION_CHOICES = (
        (SINGLE, 'Single'),
        (COMPLICATED, 'Complicated'),
        (SEPERATED, 'Seperated'),
        (NOT_MENTION, 'Not Shared')
    )
    ########### END OF Relation Choice Constants and Tuple #########

    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField()
    education = models.TextField(blank = True)
    interests = models.TextField(blank = True)
    relation_status = models.CharField(max_length = 20, choices = RELATION_CHOICES)