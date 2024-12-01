# Практическая работа 2: Базовая 2D-игра «Инопланетное вторжение» с использованием Pygame
## Цель работы:
Разработать игру «Инопланетное вторжение», в которой игрок управляет кораблём и должен уничтожить флот инопланетян. Работа позволит вам познакомиться с основами разработки игр на Python с помощью библиотеки pygame и
позволит применить эти знания о компьютерной графике, анимации и управлении событиями в дальнейшем

### 1. Настройка окружения  
Для работы игры был использован модуль pygame для создания графического интерфейса и реализации основных игровых механик. Установка библиотеки осуществляется через команду:

```
pip install pygame
```

### 2. Создание игрового окна  
Игровое окно создаётся с помощью метода pygame.display.set_mode(), где задаются размеры экрана и параметры фона.  
- Размер экрана настраивается через объект ai_settings, в котором задаются ширина и высота.  
- Цвет фона определяется в формате RGB с использованием параметра ai_settings.bg_color.  
Экран обновляется в каждом цикле игры, что обеспечивает плавную анимацию.

3. Разработка основного цикла игры
Главный цикл игры реализован с помощью while True, который управляет всеми событиями игры и обновлением экрана. В этом цикле:

Обрабатываются события (например, движение корабля и стрельба).
Обновляется положение объектов на экране (корабль, пули, пришельцы).
Вызываются функции для проверки столкновений (пули с пришельцами, корабль с пришельцами).
Каждый цикл перерисовывает экран для отображения актуального состояния игры

4. Создание класса Ship (Корабль)
Класс Ship реализует объект, управляющийся пользователем — корабль. Для этого:

В классе задается стартовая позиция корабля в центре нижней части экрана.
Реализовано движение корабля вправо и влево с помощью изменения координат на экране, управляемое клавишами стрелок.
Позиция обновляется каждый раз, когда в цикле игры проверяется состояние клавиш.
Реализована логика для управления движением в пределах экрана.

5. Добавление стрельбы
Для реализации стрельбы был создан класс Bullet, который представляет пулю, выстреливаемую из корабля. В нем:

Пуля создается при нажатии на пробел и движется вверх.
Каждая пуля обновляется с каждым кадром (передвижение вверх).
Если пуля выходит за пределы экрана, она удаляется из группы.
Для каждого выстрела воспроизводится звук, создаваемый с помощью pygame.mixer.Sound.

6. Генерация пришельцев
Пришельцы создаются с помощью функции create_alien и располагаются в ряды на экране, заполняя пространство. Каждый пришелец является объектом класса Alien, который обновляется с каждой итерацией цикла игры. Если пришелец достигнет края экрана, флот изменит направление.

Флот пришельцев обновляется по мере того, как игрок уничтожает их. Количество пришельцев в ряду и ряду зависит от размера экрана и размеров самих пришельцев, что позволяет гибко регулировать сложность игры.

7. Добавление конца игры и ограничения:
• Добавьте систему жизней для игрока: при столкновении с инопланетянином или достижении нижней границы игрок теряет корабль. Игра завершается, если игрок теряет все корабли.
• Реализуйте увеличение скорости и сложности игры с каждым уровнем, что можно контролировать с помощью параметров, задаваемых в настройках.

8. Организация структуры кода:
• Разделите код на модули: главный файл alien_invasion.py, модули для настроек (settings.py), для
корабля (ship.py), инопланетян (alien.py), и стрельбы (bullet.py). Такое разбиение на файлы повысит
читаемость и управляемость кода
```
alien_invasion/
│
├── main.py            # Главный файл, запускающий игру
├── settings.py        # Настройки игры
├── ship.py            # Класс для корабля игрока
├── alien.py           # Класс для инопланетян
├── bullet.py          # Класс для пуль
├── button.py          # Класс для кнопки
├── functions.py       # Вспомогательные функции
│
└── images/            # Папка с изображениями
    ├── ship.bmp       # Изображение корабля
    └── alien.bmp      # Изображение инопланетянина
```

Практическая работа 3 – развитие игры “Инопланетное вторжение”
Цель работы
Дополнить базовую игру “Инопланетное вторжение” функциональностью, которая сделает игровой процесс более
увлекательным и технологичным. В этой работе вы добавите звуковые эффекты, систему уровней, сохранение прогресса и интерактивные объекты с интересными механиками.

1. Звуковые эффекты
Для улучшения игрового опыта были добавлены звуковые эффекты, которые сопровождают ключевые события в игре. Звуки помогают сделать игру более атмосферной и динамичной.

Реализация:
Подготовлены звуковые файлы в формате .wav для следующих событий:

Выстрелы: звук выстрела снаряда.
Уничтожение инопланетян: звук взрыва при уничтожении инопланетянина.
Потеря жизней: звук при столкновении с инопланетянином.
Конец игры: звук завершения игры.

Использован модуль pygame.mixer для работы с аудио:

Звуковые эффекты инициализируются с помощью pygame.mixer.Sound("path_to_sound.wav").
Воспроизведение звуков осуществляется с помощью метода play() объекта звука.
Звуки связаны с событиями игры:

При создании нового снаряда воспроизводится звук выстрела.
При уничтожении инопланетянина вызывается звук взрыва.
Когда игрок теряет жизни или заканчивает игру, проигрывается соответствующий звук.

 Система уровней
Система уровней была реализована таким образом, что с каждым новым уровнем сложность игры увеличивается. Это достигается путем ускорения инопланетян и увеличения их количества.

Реализация:
Для отслеживания текущего уровня была добавлена переменная level.
Скорость движения инопланетян увеличивается с каждым уровнем с помощью множителя:
На каждом новом уровне скорость инопланетян умножается на 1.1 (например, alien_speed *= 1.1).
При уничтожении всего флота инопланетян происходит переход на новый уровень:
Пересоздается новый флот инопланетян с увеличенной скоростью.
Все пули очищаются.

3. Сохранение и загрузка прогресса
Для обеспечения возможности сохранения и загрузки прогресса игры была реализована система сериализации с использованием модуля pickle.

Реализация:
Данные игры (уровень, очки, жизни) сохраняются в структуру данных game_data, которая сериализуется с помощью pickle.
Для сохранения прогресса используется функция save_game(), а для загрузки — функция load_game().
Пользователь может сохранять игру с помощью клавиши S и загружать её с помощью клавиши L.

4. Интерактивные объекты с интересными механиками
 Класс Bonus
Класс Bonus представляет бонусы, которые могут появляться на экране. Каждый бонус может быть одного из двух типов:

life (жизнь)
shield (щит)
Основные особенности:

Тип бонуса: Устанавливается через параметр bonus_type при создании объекта.
Изображение: В зависимости от типа бонуса загружается соответствующее изображение.
Позиция: Бонусы появляются в позиции пришельцев, после их уничтожения.
Скорость: Бонусы падают вниз с фиксированной скоростью, которая задается через настройки игры.

Добавление бонусов в игру
Бонусы создаются при уничтожении пришельцев с определенной вероятностью, заданной в настройках игры (bonus_chance). Для этого был реализован метод create_bonus, который вызывается при попадании пули в пришельца:

 Проверка столкновений с бонусами
Когда бонус падает, происходит его столкновение с кораблем игрока. Это обрабатывается в функции check_bonus_collisions, где проверяется, какой тип бонуса был получен:

life — увеличивает количество оставшихся жизней.
shield — активирует временный защитный щит.

Активирование щита
Когда игрок получает бонус "щита", активируется специальный флаг shield_active, который позволяет игроку игнорировать столкновения с пришельцами. Также для щита отслеживается его продолжительность с помощью таймера:

5. Сборка игры в исполняемый файлен
