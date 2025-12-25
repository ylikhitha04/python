class car:
    def __init__(self):
        self.name="swift"
        self.price=234567
        self.colour="black"
    def accelerate(self):
        print("i am accelerating")
    def brake(self):
        print("car is stopping")
    def start(self):
        print("car is starting")
c1=car()
c1.accelerate()
c1.brake()
c1.start()
