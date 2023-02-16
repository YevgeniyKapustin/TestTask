export STRIPE_API_KEY='rk_test_51MZWQKA3rxcevihuLuUip5dtSjOSn3Mf2v8BgogMdAbIaXgeT9PKwTI5CCMaVRXlmlJCLz54S6hptCOKZEf0rR2g00lhTLYdSh'
export STRIPE_PUBLIC_KEY='pk_test_51MZWQKA3rxcevihukSUdGUjubJOiUWDnhWqkRN0JcX7aD2fR2yd4nc2spXm02UI4DNNdj9g8nKG1vZFOkVI0mp5j00HVYEvn57'
export SECRET_KEY='django-insecure-$j)m^qpj)b8u-m+b*_xf@!t0@2c4t=l%cao_x%@1k(dl%%bw1g'

# данные для db и django
export POSTGRES_DB='stripe_db'
export POSTGRES_USER='user_name'
export POSTGRES_PASSWORD='123'
export POSTGRES_HOST='localhost'
export POSTGRES_PORT=5432

#sudo apt update

## установка и настройка db
#sudo apt install postgresql postgresql-contrib
#sudo -u postgres createdb $POSTGRES_DB
#
#CREATE USER $POSTGRES_USER WITH PASSWORD $POSTGRES_PASSWORD;
#GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB to $POSTGRES_USER;
#\c $POSTGRES_DB
#GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO $POSTGRES_USER;


## установка необходимых пакетов
#cd django_stripe_api || exit
#pip install -r requirements.txt

# запуск сайта

#python manage.py makemigrations
#python manage.py migrate

python manage.py runserver
