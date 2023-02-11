export STRIPE_API_KEY='STRIPE_API_KEY'
export STRIPE_PUBLIC_KEY='STRIPE_PUBLIC_KEY'
export SECRET_KEY='SECRET_KEY'
export DB_NAME='DB_NAME'
export DB_USER='DB_USER'
export DB_PASSWORD='DB_PASSWORD'

cd django_stripe_api || exit
python manage.py runserver
