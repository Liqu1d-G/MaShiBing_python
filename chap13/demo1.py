class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("汽车已启动。。。")


car = Car('宝马x5')
car.start()
print(car.brand)
