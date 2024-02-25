from django.contrib.auth.models import User

# Replace 'username_of_superuser' with the actual username of your superuser
try:
    user = User.objects.get(username='Sarah')
    user.delete()
    print('User deleted successfully.')
except User.DoesNotExist:
    print('User does not exist.')