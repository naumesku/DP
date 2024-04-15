Платформа для публикации записей пользователями.

Публикация может быть бесплатной, то есть доступной любому пользователю
без регистрации, либо платной, которая доступна только авторизованным 
пользователям, который оплатили разовую подписку. 

Для реализации оплаты подписки используется Stripe. 
Регистрация пользователя должна быть по номеру телефона.

Время жизни токена не более часа, затем он удаляется из БД.
Также токен удаляется из БД при аутентификация.

Права доступа

1)Не авторизованные пользователи:
Просмотр: - бесплатных публикаций
Добавление: - нет

2)Авторизованные пользователи без подписки:
Просмотр:
- бесплатных публикаций,
- платных публикаций,
Добавление:
 - бесплатных публикаций

3)Авторизованные с подпиской:
Просмотр:
- бесплатных публикаций,
- платных публикаций,
Добавление:
- бесплатных публикаций,
- платных публикаций

Ссылки на оплату удаляются из БД после подтверждения платежа.
Для отправки смс исплользуется сервис смс просто : https://sms-prosto.ru/
Создание SU происходит запуском команды: python manage.py csu

Запуск приложения происходит с использованием docker:
    В терминале:
    - Собрать контейнеры:
    docker-compose build
      - Поднять файл:
      docker-compose up