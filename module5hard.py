import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print(f"Вход выполнен успешно как {nickname}")
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Регистрация прошла успешно, вход выполнен как {nickname}")

    def log_out(self):
        self.current_user = None
        print("Выход из аккаунта")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f"Видео {video.title} добавлено")

    def get_videos(self, search_term):
        search_term = search_term.lower()
        result = [video.title for video in self.videos if search_term in video.title.lower()]
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        found_video = None
        for video in self.videos:
            if video.title == title:
                found_video = video
                break

        if found_video is None:
            print("Видео не найдено")
            return

        if found_video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Начинается воспроизведение видео {found_video.title}")
        for i in range(found_video.duration):
            found_video.time_now += 1
            print(f"Прошло {found_video.time_now} секунд...")
            time.sleep(1)
        print("Конец видео")
        found_video.time_now = 0

# Проверка кода
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
class VideoPlayer:
  """
  Класс, представляющий видеоплеер.
  """

  def __init__(self, video_title: str = None) -> None:
    """
    Инициализирует видеоплеер.

    Args:
      video_title: Название видео, которое будет воспроизводиться.
    """
    self.video_title = video_title
    self.current_time = 0
    self.is_playing = False
    self.user_logged_in = False
    self.is_adult = False

  def watch_video(self, video_title: str) -> str:
    """
    Попытка воспроизвести видео.

    Args:
      video_title: Название видео, которое необходимо воспроизвести.

    Returns:
      Строка с сообщением о результате попытки воспроизведения.
    """

    if not self.user_logged_in:
      return "Войдите в аккаунт, чтобы смотреть видео"
    if not self.is_adult:
      return "Вам нет 18 лет, пожалуйста покиньте страницу"

    if video_title == self.video_title:
      self.is_playing = True
      return "1 2 3 4 5 6 7 8 9 10 Конец видео"
    else:
      return "Видео не найдено"

  def __str__(self) -> str:
    """
    Возвращает строковое представление объекта VideoPlayer.

    Returns:
      Строка с описанием видеоплеера.
    """
    return f"VideoPlayer(video_title='{self.video_title}', is_playing='{self.is_playing}')"

  def __repr__(self) -> str:
    """
    Возвращает строку с представлением объекта, подходящую для вывода в консоль.

    Returns:
      Строка с представлением объекта.
    """
    return self.__str__()

  def __contains__(self, video_title: str) -> bool:
    """
    Проверяет, находится ли указанное видео в списке доступных видео.

    Args:
      video_title: Название видео, которое нужно найти.

    Returns:
      True, если видео находится в списке доступных видео, False - в противном случае.
    """
    return self.video_title == video_title

  def __eq__(self, other: object) -> bool:
    """
    Проверяет, равен ли текущий объект другому объекту.

    Args:
      other: Объект для сравнения.

    Returns:
      True, если объекты равны, False - в противном случае.
    """
    if isinstance(other, VideoPlayer):
      return self.video_title == other.video_title and self.is_playing == other.is_playing
    return False


# Тестирование класса
player = VideoPlayer()
print(player) # Output: VideoPlayer(video_title=None, is_playing=False)

print(player.watch_video("Лучший язык программирования 2024 года!")) # Output: Войдите в аккаунт, чтобы смотреть видео
print(player.watch_video("Для чего девушкам парень программист?")) # Output: Вам нет 18 лет, пожалуйста покиньте страницу

player.user_logged_in = True
player.is_adult = True
print(player.watch_video("Лучший язык программирования 2024 года!")) # Output: Видео не найдено

player.video_title = "Лучший язык программирования 2024 года!"
print(player.watch_video("Лучший язык программирования 2024 года!")) # Output: 1 2 3 4 5 6 7 8 9 10 Конец видео

print("Лучший язык программирования 2024 года!" in player) # Output: True
print("Python" in player) # Output: False

player2 = VideoPlayer("Лучший язык программирования 2024 года!")
print(player == player2) # Output: True

player2.is_playing = False
print(player == player2) # Output: False

