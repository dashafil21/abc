# class Camera:
#     def take_photo(self):
#         print("Сделана фотография")
#
#
# class Phone:
#     def make_call(self):
#         print("Совершён вызов")
#
#
# class SmartPhone(Camera, Phone):
#     def browse_internet(self):
#         print("Доступ в интернет")
#
#
# sm = SmartPhone()
# sm.take_photo()
# sm.make_call()
# sm.browse_internet()



class Logger():
    def log(self, message):
        print(f"Логирование: {message}")


class ErrorHandler():
    def log(self, message):
        print(f"обработка ошибки: {message}")


class Application(Logger,ErrorHandler):
    def log(self, message):
        print(f"Приложение: {message}")
        super().log(message)


ap = Application()
ap.log("Привет")




