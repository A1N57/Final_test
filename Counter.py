class Counter:
    count = 0

    def __init__(self):
        self.open = False

    def __enter__(self):
        self.open = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.open = False

    def add(self):
        if not self.open:
            raise Exception("Ресурс закрыт, невозможно добавить")
        Counter.count += 1


try:
    with Counter() as counter:
        counter.add()
        print("Животное добавлено")
except Exception as e:
    print(e)
