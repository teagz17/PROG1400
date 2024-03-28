# from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, mobile, email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email
    
    def make_trip(self,route):
        print(f'{self.first_name} {self.last_name} is making a trip along the route: {route}')

    def get_stops(self, route):
        for stops in range(len(route)):
            if stops[0] or stops[len(route) - 1] == False:
                return stops

class Driver(Person):
    def __init__(self, first_name, last_name, mobile, email, v_make, v_model, v_colour, v_type):
        super().__init__(first_name, last_name, mobile, email)
        self.v_make = v_make
        self.v_model = v_model
        self.v_type = v_type
        self.v_colour = v_colour

    def get_stops(self, route):
        return super().get_stops(route)
    
    def make_trip(self, route):
        print(f'{self.first_name} {self.last_name} is driving a {self.v_colour} {self.v_make} {self.v_model} {self.v_type}, leaving {route[0]}, stopping at {route.get_stops()}, end arriving at {route[len(route) - 1]}.')

class Rider(Person):
    def __init__(self, first_name, last_name, mobile, email):
        super().__init__(first_name, last_name, mobile, email)
    
    def make_trip(self, route):
        print(f'{self.first_name} {self.last_name}, {driver1.first_name} {driver1.last_name} will pick you up at {route[1]}.')

class Route:
    def __init__(self, stops):
        self.stops = stops

driver1 = Driver('teagan', 'stewart', '902-888-8888', 'teag@hotmail.com', 'harley davidson', 'fatboy', 'blue', 'motorcycle')
rider1 = Rider('kazuma', 'kiryu', '902-888-9999', 'kazzy@tojo.com')

route = ['antigonish', 'tim hortons', 'big stop', 'strait area']

def make_trip():
    
    pass

driver1.make_trip(route)
# rider1.make_trip(route)