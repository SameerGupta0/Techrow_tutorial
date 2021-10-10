import datetime

class Parkinglot:
    def __init__(self,parking_spots):
        self.available_parking_spots=parking_spots
        self.occupied_parking_spots=[]

    def park(self,vehicle):
        if(len(self.available_parking_spots)>0):
            spot=self.available_parking_spots.pop()
            spot.status=1
            vehicle.spot=spot 
            self.occupied_parking_spots.append(spot)
            
            print("Please park your vehicle at Spot id: "+str(spot.id))
        else:
            print("Parking lot full.")
            
    def exit(self,vehicle):
        spot=vehicle.spot
        print("Vehicle exiting spot id: "+str(spot.id))
        spot.status=0
        self.occupied_parking_spots.pop()
        self.available_parking_spots.append(spot)


class ParkingSpot:
    def __init__(self,id):
        self.id=id
        
        #Parking satus empty=0 or occupied=1
        self.status=0


class Vehicle:
    def __init__(self,license,user,type_of_vehicle):
        self.license=license
        self.user=user
        self.type_of_vehicle=type_of_vehicle
        self.entry_time=datetime.datetime.now()
        self.spot=None

spots=[]
spot0=ParkingSpot(0)
spot1=ParkingSpot(1)
spots.append(spot0)
spots.append(spot1)

parkinglot=Parkinglot(spots)
vehicle1=Vehicle(155548,"Roshan","sedan")
parkinglot.park(vehicle1)

vehicle2=Vehicle(155555,"RoshanS","SUV")
parkinglot.park(vehicle2)

vehicle3=Vehicle(1555445,"Roshan","sedan")
parkinglot.park(vehicle3)

parkinglot.exit(vehicle1)
parkinglot.exit(vehicle2)















