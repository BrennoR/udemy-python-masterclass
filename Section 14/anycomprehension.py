import timeit
from data import people, plants_list, plants_dict

# people = []

if bool(people) and all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == 'Grass' for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")


def main():
    if any(plant.plant_type == "Grass" for plant in plants_dict.values()):
        print("This dict contains Grass")
    else:
        print("NO GRASS HERE ")


# alternative way
def alt():
    if any(plants_dict[key].plant_type == "Grass" for key in plants_dict):
        print("This dict contains Grass")
    else:
        print("NO GRASS HERE ")


result_1 = timeit.timeit(main, number=100000)
result_2 = timeit.timeit(alt, number=100000)

print(result_1, result_2)
