from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, mobile, email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email
    
    def details(self):
        return f'Name: {self.first_name} {self.last_name}, Mobile: {self.mobile}, Email: {self.email}'
    
class Driver(Person):
    def __init__(self, first_name, last_name, mobile, email, v_make, v_model, v_colour, v_type):
        super().__init__(first_name, last_name, mobile, email)
        self.v_make = v_make
        self.v_model = v_model
        self.v_colour = v_colour
        self.v_type = v_type
    
    def details(self):
        return f'Driver info: \n{super().details()}, Vehicle: {self.v_colour} {self.v_make} {self.v_model} {self.v_type}'

class Rider(Person):
    def __init__(self, first_name, last_name, mobile, email):
        super().__init__(first_name, last_name, mobile, email)

    def details(self):
        return f'Rider info: \n{super().details()}'

class Route:
    def __init__(self, origin, midway_stop, destination):
        self.origin = origin
        self.midway_stop = midway_stop
        self.destination = destination

    def details(self):
        return f'Origin: {self.origin}, Midway stop: {self.midway_stop}, Destination: {self.destination}'
    
class Trip(Route):
    def __init__(self, origin, midway_stop, destination, leaving_time, stop_time, arrival_time):
        super().__init__(origin, midway_stop, destination)
        self.leaving_time = leaving_time
        self.stop_time = stop_time
        self.arrival_time = arrival_time

    def details(self):
        return f'Trip Details: \n{super().details()}, Leaving Time = {self.leaving_time}, Stop Time: {self.stop_time}, Arrival Time: {self.arrival_time}'
    
def run():
    driver1 = Driver('Kazuma', 'Kiryu', '902-222-6666', 'kazzy@tojo.com', 'Harley Davidson', 'Fatboy', 'Blue', 'Motorcycle')
    rider1 = Rider('Goro', 'Majima', '902-222-5656', 'gorogorogoro@tojo.com')
    trip1 = Trip('Kamurocho', 'Isezaki Ijincho', 'Sotenbori', datetime(2024,2,15,7,0), datetime(2024,2,15,7,30), datetime(2024,2,15,8,0))
    journey1 = [driver1, rider1, trip1]

    for i in journey1:
        print(i.details())

if __name__ == "__main__":
    run()