# Support-bot - telegram-bot тех.поддержки.
![Aiogram](https://img.shields.io/badge/telegram-aiogram-blue) ![Docker](https://img.shields.io/badge/-Docker-yellowgreen)

**Support-bot** - telegram-bot технической поддержки на библиотеки aiogram.

### Запуск проекта в Docker

Запустить контейнер
```
docker-compose up -d --build
```
### Настройки виртуального окружения .env
BOT_TOKEN - токен бота
ADMIN - токены тг-аккаунтов, которые будут получать админские сообщения
OPERATOR_IDS - токены тг-аккаунтов сотрудников поддержки. В .env файл записываются в виде: 
OPERATOR_IDS=123456789,987654321...

#### Автор - [Екатерина Серова](https://github.com/EISerova/)
Если у вас есть предложения или замечания, пожалуйста, свяжитесь со мной - [katyaserova@yandex.ru]

Лицензия:
[MIT](https://choosealicense.com/licenses/mit/)
