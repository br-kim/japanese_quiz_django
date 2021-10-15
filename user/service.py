from django.contrib.auth.models import User


def register_user(user_id, user_password, user_email):
    user = User.objects.create_user(username=user_id,
                                    email=user_email,
                                    password=user_password)
    user.save()
    return user


def delete_user(user_id, user_password):
    pass

