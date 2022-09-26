# Сообщение при запуске бота
RUN_BOT_MESSAGE = "Бот запущен"

# Кнопки встроенного меню (commands)
START_COMMAND = "Запустить бота"
SUPPORT_COMMAND = "Написать сообщение техподдержку"
HELP_COMMAND = "Помощь"

# Приветствие юзера
START_GREETING_MESSAGE = (
    "Вас приветствует служба технической поддержки сайта Newsland.com"
)

# Кнопки keyboards
SUPPORT_ANSWER_BUTTON = "Ответить пользователю"
USER_QUESTION_BUTTON = "Задать вопрос оператору"
END_BUTTON = "Завершить сеанс"

# Автоматические сообщения в чат
NO_FREE_OPERATORS_MESSAGE = (
    "К сожалению, сейчас нет свободных операторов. Попробуйте позже."
)
WAIT_OPERATOR_MESSAGE = "Вам ответит первый освободившийся оператор."
USER_REQUEST_MESSAGE = "С вами хочет связаться пользователь {user}"
USER_REFUSE_MESSAGE = "К сожалению, пользователь уже передумал."
START_DIALOG_WITH_USER_MESSAGE = "Начало диалога."
START_DIALOG_WITH_OPERATOR_MESSAGE = "Здравствуйте, техподдержка на связи! Задавайте свой вопрос. Чтобы завершить общение нажмите на кнопку."
WAIT_FOR_OPERATOR_MESSAGE = "Дождитесь ответа оператора или отмените сеанс."
END_DIALOG_FOR_USER_MESSAGE = "Сеанс тех.поддержки завершен."
OPERATOR_END_DIALOG_MESSAGE = "Сеанс завершен. "

# Ответ юзеру без состояния
ECHO_ANSWER = (
    "Ваше сообщение отправлено вне чата. Нажмите /start и ждите ответа оператора."
)

# Сообщения для логгирования
GET_OPERATOR = "Выбран оператор - {operator_name}"
NO_FREE_OPERATORS = (
    "Свободный оператор не найден, статусы операторов: {checked_operators}"
)
USER_GET_START = "Юзер {user} нажал /start"
END_DIALOG = (
    "Сеанс тех.поддержки завершен. Юзер - {user}, chat_instance - {chat_instance}."
)
START_DIALOG_USER = 'Юзер нажал "задать вопрос", chat_instance - {chat_instance}.'
START_DIALOG_OPERATOR = 'Оператор {chat_instance} нажал "ответить пользователю".'

# Сообщения об ошибках
ERROR_TOKEN = "Отсутствует обязательный токен: {error}"
ERROR_EDIT_MESSAGE = "Неудалось отредактировать сообщение, ошибка: {error}"
