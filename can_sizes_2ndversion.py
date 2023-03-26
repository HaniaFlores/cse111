"""Compute and print the storage efficiency of a can."""

# Import the standard math module so that
# math.pi can be used in this program.
import math

# Made four different lists to store the name, radius, height and cost of all 12 can sizes.
names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
radius_list = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
height_list = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
cost_list = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]


def main():
    """
    Stretch Challenge 3: The loop processes the values in the lists.
    Calls the functions and prints the results.
    Each element inside a list will have a unique position that identifies it,
    called the element's index (i). The loop will use that index to give a value
    to the variables.
    """
    for i in range(len(names)):
        name = names[i]
        radius = radius_list[i]
        height = height_list[i]
        cost = cost_list[i]
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, cost)
        print(f"{name} --- {storage_efficiency:.2f} --- {cost_efficiency:.2f}")
        

def compute_volume(radius,height):
    """Compute and return the volume.
    Parameters:
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area(radius,height):
    """Compute and return the surface area.
    Parameters:
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the surface area of the cylinder
    """
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(volume,surface_area):
    """
    Stretch Challenge 1: Compute and return the storage efficiency.
    Parameters:
        volume: the volume of the cylinder
        surface area: the surface area of the cylinder
    Return: the storage efficiency of the can.
    """
    storage_efficiency = volume / surface_area
    return storage_efficiency


def compute_cost_efficiency(volume,cost):
    """
    Stretch Challenge 2: Compute and return the cost efficiency.
    Parameters:
        volume: the volume of the cylinder
        cost: the cost per can.
    Return: the cost efficiency of the can.
    """
    cost_efficiency = volume / cost
    return cost_efficiency

main()