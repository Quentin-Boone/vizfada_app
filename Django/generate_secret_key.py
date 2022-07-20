from django.core.management.utils import get_random_secret_key

key=get_random_secret_key()

with open(".env", "w") as f:
	f.write("SECRET_KEY='%s'\n" %(key))
	f.close()

