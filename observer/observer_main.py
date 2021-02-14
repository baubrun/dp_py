from sms_users import SMSUsers
from commentary_object import CommentaryObject

def observer_main():
    subject = CommentaryObject("NHL Montreal vs Toronto 21h")
    observer = SMSUsers(subject, "La Presse MTL")
    observer.subscribe()

    observer2 = SMSUsers(subject, "La Gazette MTL")
    observer2.subscribe()

    subject.set_desc("Welcome to live Soccer match")
    subject.set_desc("Current score 0-0")

    observer2.unsubscribe()

    subject.set_desc("It's a goal!!")
    subject.set_desc("Half-time score 1-0")



if __name__ == "__main__":
    observer_main()