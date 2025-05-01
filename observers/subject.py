class Subject:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def notify_all(self, data):
        for observer in self._observers:
            observer.notify(data)
