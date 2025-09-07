

class robots:

    def __init__(self,name):
        self.name = name
        self.position = [0,0]
        print('My Name is', self.name)

    def walk(self, x):
        self.position = self.position[0] + x
        print('New Position is:', self.position)

    def eat(self):
        print('I am Hungry!!')


class robot_dog(robots):

    def make_noise(self):
        print('WOOF WOOF !!')

    def eat(self):
        super().eat()
        print('I ate chicken!!')

    
my_robot_dog = robot_dog('MILO')
my_robot_dog.walk(10)
my_robot_dog.make_noise()
my_robot_dog.eat()
