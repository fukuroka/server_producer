Установите rabbitmq

sudo apt-get install -y erlang-base \
                        erlang-asn1 erlang-crypto erlang-eldap erlang-ftp erlang-inets \
                        erlang-mnesia erlang-os-mon erlang-parsetools erlang-public-key \
                        erlang-runtime-tools erlang-snmp erlang-ssl \
                        erlang-syntax-tools erlang-tftp erlang-tools erlang-xmerl


sudo apt-get install rabbitmq-server -y --fix-missing

После установки создайте администратора и дайте ему все разрешения

rabbitmqctl add_user admin admin

rabbitmqctl set_user_tags admin administrator

rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"


Шаги запуска.
1. Откройте терминал и запустите sudo service rabbitmq-server start
2. Запустите rabbitmq management, чтобы отслеживать работу rabbitmq (http://localhost:15672/)
  sudo rabbitmq-plugins enable rabbitmq_management
3. В терминале пайчарма запустите селери celery -A test_project worker --loglevel=info
4. Запустиите джанго сервер

Теперь вы можете дергать ручки
