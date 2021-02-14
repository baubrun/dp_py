from subject import Subject


class CommentaryObject(Subject):
    def __init__(self, subject_details):
        self._observers = []
        self._subject_details = subject_details
        self.desc = None

    def notify_observers(self):
       for obs in self._observers:
           obs.update(self.desc)

    def subscribe_observer(self, observer):
       self._observers.append(observer)

    def unsubscribe_observer(self, observer):
        self._observers.remove(observer)

    def set_desc(self, desc):
        self.desc = desc
        self.notify_observers()


    def subject_details(self):
        return self._subject_details