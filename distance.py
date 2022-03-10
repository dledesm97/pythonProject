from geopy.distance import geodesic

def find_distance():
    print("-----Your Location------")
    location_la = float(input("Enter the latitude: "))
    location_lo = float(input("Enter the longitude: "))
    location = (location_la, location_lo)
    print("-----Your Destination-----")
    destination_la = float(input("Enter the latitude: "))
    destination_lo = float(input("Enter the longitude: "))
    destination = (destination_la,destination_lo)
    print("-----Destinace Between In Miles-----")
    print(geodesic(location,destination).miles)
