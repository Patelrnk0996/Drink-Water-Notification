import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
        title = "Please drink water",
        message = "The National Academies of Sciences,Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 Cups",
        # app_icon = "C:\Users\Ronak\PycharmProjects\My_Project\icon.ico",
        timeout = 2
        )
        time.sleep(6)