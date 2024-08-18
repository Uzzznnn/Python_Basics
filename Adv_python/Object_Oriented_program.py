# class Animal: #class always on top
  
#   def what_sound_does_it_make(self,flag):
#     if flag.lower()=='bark':
#       print("it's a dog")
#     else:
#       print("it's a human")
      
# species_1= Animal()
# species_1.what_sound_does_it_make('Bark')

#To make a calculator that must add subtract multiply divide two numbers etc

class Calculator:

    def add(self,x,y):

        print(f"The sum is {x+y}")

    def subtract(self,x,y):

        print(f"The difference is {x-y}")

    def multiply(self,x,y):

        print(f"The product is {x*y}")

    def divide(self,x,y):

        print(f"The division is {x/y}")

instance1 = Calculator()

instance2 = Calculator()

instance1.add(4,9)

instance1.subtract(18,11)

instance2.multiply(6,8)

instance2.divide(98,5)