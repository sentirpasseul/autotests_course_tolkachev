from exam import Exam

if __name__ == '__main__':
    try:
        app = Exam()
        app.start()

    except:
        TypeError: print("Ошибка TypeError")
