from time import sleep

class User:

    def __init__(self, username, password, age):
        self.username = username
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.username


class Video:

    def __init__(self, title, duration, now=0, adult=False):
        self.title = title
        self.duration = duration
        self.now = now
        self.adult = adult


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def get_videos(self, title1):
        vids = []
        for i in self.videos:
            if i.title.lower().count(title1.lower()) > 0:
                vids.append(i.title)
        if len(vids) == 0:
            return 'Видеоролик не найден'
        else:
            return vids

    def add(self, *vids):
        for i in vids:
            self.videos.append(i)

    def register(self, name, pwd, age):
        for i in self.users:
            if name == i.username:
                print(f'Пользователь {name} уже существует')
                return
        self.users.append(User(name, pwd, age))
        self.current_user = User(name, pwd, age)

    def log_in(self, name, pwd):
        for i in self.users:
            if name == i.username and hash(pwd) == i.password:
                self.current_user = i

    def log_out(self):
        self.current_user = None

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        exists = False
        for i in self.videos:
            if title == i.title:
                exists = True
                if not (i.adult and self.current_user.age < 18):
                    print(title)
                    for j in range(i.now, i.duration):
                        print(j + 1, end=" . ")
                        sleep(1)
                    print('The end')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
        if not exists:
            print('Нет такого видеоролика')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult=True)

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

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
