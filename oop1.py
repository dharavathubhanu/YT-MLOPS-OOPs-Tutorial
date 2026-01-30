#initiate a class 
class employee:
    #special method/magic method/dunder method
    def __init__(self):
      print("Started executing attributes/data")
      self.id=123
      self.salary=50000
      self.designation="SDE"
      print("attributes/data has been initiated")

    def travel(self,destination):
       print("This travel fucntion was called manually")
       print(f"Employee is now travelling to {destination}")

sam=employee()

print(sam.id)
sam.travel("kerala")


