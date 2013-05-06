from django.contrib.auth.models import User


def get_random_user(max_id=None):
    if not max_id:
        raise Exception('No max id given!')
    return User.objects.raw('SELECT * FROM auth_user OFFSET floor(random()*%(max_id)d) LIMIT 1;').format(max_id=max_id).get()


def get_max_id():
    return User.objects.all().count()

# from django.contrib.auth.models import AbstractBaseUser


# class TuitterUserProfile(AbstractBaseUser):
#     username = models.CharField(max_length=40, unique=True, db_index=True)
#     email = models.EmailField(max_length=254, unique=True)
#     picture = models.CharField(max_length=1024)

#     USERNAME_FIELD = username
