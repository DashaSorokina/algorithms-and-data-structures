class Cat:
    breed = 'pers'
    def hello(self):
        return print('hi', self)
    

    def show_breed(self):
        print(f'my breed is {self.breed}')

    def show_name(self):
        if hasattr(self,'name'):
            print(f'my name is {self.name}')
        else:
            print('nothing')


    def set_value(self, value):
        self.name = value


        
walt = Cat()
mari = Cat()
tom = Cat()
print(tom.show_name())
tom.set_value('Tom')
print(tom.name)
mari.name = 'mary'
print(mari.show_name())
print(tom.show_name())
walt.breed = 'siam'
print(walt.show_breed())

# if __name__=='__main__':
#     print(Cat.hello)
#     print(bob.hello())
