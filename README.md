# dockerfile
Набір інструкцій для будування образу

```dockerfile
# вказуємо з чого саме збирати базовий образ
FROM python:3.10-buster

# робоча папка
WORKDIR /app

# копіюємо локальні файли у образ
COPY . .

# встановлюємо модулі з requirements.txt
RUN pip3 install -r requirements.txt

# запускаємо сервіс
CMD [ "python","./main.py" ]
```

# docker build

Для створення образу з докер файлу: 
```commandline
docker build . -t base-python-img
```
Перший аргумент дорога до папки з докерфайлом в данному прикладі це ``.`` тобто поточна папка.

``-t base-python-img`` - вказується назва для образу.

# docker run

Для запуску образу:
```commandline
docker run --name "base-python-1" --env ENV_TYPE=test --volume "/var/www/docker/base:/app/" -p "7766:6677" base-python-img
```

``--name "base-python-1"`` - назва контейнеру

``--env ENV_TYPE=test`` - змінні оточення

``--volume "/var/www/docker/base:/app/"`` - залінковані локальні файли з контейнером

``-p "7766:6677"`` - відкритий назові порт в данному випадку порт з контейнера 6677 -> порт назовні 7766

# docker start
Команда для запуску зупиненного контейнеру
```commandline
docker start flask
```
# docker stop
Команда для зупинки контейнеру
```commandline
docker stop flask
```
# docker logs
Команда для відображення логів з контейнера, ``-f`` - для того щоб постійно відслідковувати
```commandline
docker logs -f flask
```
# docker restart
Команда для перезапуску контейнера
```commandline
docker restart flask
```

# docker rm
Команда для видалення контейнеру
```commandline
docker rm flask
```
# docker rmi
Команда для видалення образу
```commandline
docker rm flask-image
```
# docker compose

```yml
version: "3.9" # версія докеру

services:
  flask:  # назва секції/сервісу
    build: # інструкції для збірки образу
      context: ./flask # шлях до папки з докерфайлом
    container_name: 'flask' # назва контейнеру після запуску
    image: 'flask-image' # назва образу після збірки
    ports: # порти які ми бажаємо відкрити з контейнера 
      - "7766:6677" # вказємо шо 6677 порт в контейнері це 7766 порт зовні
#    network_mode: host # якшо вказуємо цю опцію то прибираємо ports, всі запущені сервіси в сенсі мережі вважаються запущеним на локальній машині
    volumes: # можливо вказати які саме папки з'єднати з контейнером
      - ./flask/:/app/ # приєднує папку ./flask в папку /app контейнеру
    environment:  # змінні оточення
      - ENV_TYPE=compose
    env_file: # окремий файлик з зміннами оточення
      - secrets.env # шлях до файла з зміниими оточеннями
```

Команда для запуску сервіса з docker-compose.yml
```commandline
docker compose up -d --force-recreate flask
```

``-d`` - не зв'язувати консоль контейнера з запущенною консолью

``--force-recreate`` - перестворювати контейнер у будь якому випадку

``flask`` - назва сервісу для запуску
