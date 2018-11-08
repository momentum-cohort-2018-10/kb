import csv


class Network:
    def __init__(self, block_size, lat, lng):
        self.block_size = block_size
        self.lat = lat
        self.lng = lng

    def get_ip_count(self):
        return 2**(128 - self.block_size)

    def __str__(self):
        return f"Block: {self.block_size} {self.lat} {self.lng}"

    def __repr__(self):
        return str(self)


data = []

with open('GeoLite2-City-Blocks-IPv6.csv') as file:
    geolite_reader = csv.reader(file)
    for row in geolite_reader:
        data.append((row[0], row[7], row[8]))

data = data[1:]

new_data = []
for row in data:
    network = row[0]
    block_size = int(network.split("/")[1])
    lat = float(row[1])
    lng = float(row[2])
    new_data.append(Network(block_size, lat, lng))

print(new_data[:10])
