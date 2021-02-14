from observer import Observer


class SMSUsers(Observer):
    def __init__(self, subject, user_info):
        try:
            subject is not None
        except ValueError:
            print("Publisher not found.")
        self._subject = subject
        self._user_info = user_info
        self._desc = None

    def display(self):
        print(f"[{self._user_info}]: {self._desc}")


    def subscribe(self):
        print(f"Subscribing {self._user_info} to {self._subject.subject_details()}")
        self._subject.subscribe_observer(self)
        print("Subscribed successfully.")

    def unsubscribe(self):
        print(f"Unsubscribing {self._user_info} to {self._subject.subject_details()}")
        self._subject.unsubscribe_observer(self)
        print("Unsubscribed successfully.")

    def update(self, desc):
        self._desc = desc
        self.display()
