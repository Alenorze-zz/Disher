from django.contrib.auth import get_user_model

User = get_user_model()

random_ = User.objects.last()

random_.profile.followers.all()

random_.is_following.all() 