## Подготовка к запуску

### Устанавливаем postgres:
> sudo apt install postgresql postgresql-contrib

### Создаем базу данных:
> sudo -u postgres createdb stripe_db

### Входим в терминал psql:
>sudo -i -u postgres 

>psql

### Создаем юзера для работы с postgres и даем ему права:
> CREATE USER user_name WITH PASSWORD '123';

>GRANT ALL PRIVILEGES ON DATABASE stripe_db to user_name;

>\c stripe_db

>GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO user_name;

>\q

>logout

### Устанавливаем необходимые пакеты
Нужно перейти в корневую директорию проекта, если вы не в ней
>pip install -r requirements.txt

### Проводим миграции для базы данных
Убедитесь, что вы в корневой папке проекта, далее нужно перейти в директорию, в которой расположен manage.py
> cd django_stripe_api 

>python manage.py makemigrations

>python manage.py migrate

### Непосредственно запуск сайта
Осуществляется через run.sh, либо
>export STRIPE_API_KEY='rk_test_51MZWQKA3rxcevihuLuUip5dtSjOSn3Mf2v8BgogMdAbIaXgeT9PKwTI5CCMaVRXlmlJCLz54S6hptCOKZEf0rR2g00lhTLYdSh'

>export STRIPE_PUBLIC_KEY='pk_test_51MZWQKA3rxcevihukSUdGUjubJOiUWDnhWqkRN0JcX7aD2fR2yd4nc2spXm02UI4DNNdj9g8nKG1vZFOkVI0mp5j00HVYEvn57'

>export SECRET_KEY='django-insecure-$j)m^qpj)b8u-m+b*_xf@!t0@2c4t=l%cao_x%@1k(dl%%bw1g'

>export POSTGRES_DB='stripe_db'

>export POSTGRES_USER='user_name'

>export POSTGRES_PASSWORD='123'

>python manage.py runserver
