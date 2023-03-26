"""Compute and print the storage efficiency of a can."""

# Import the standard math module so that
# math.pi can be used in this program.
import math

names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
radius_list = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
height_list = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
cost_list = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

cost_efficiency_list = []
storage_efficiency_list = []

def main():
    best_storage_efficiency = 1
    best_cost_efficiency = 1
    # Give values to the variables name, radius and height to compute the storage efficiency.
    # Calls the funtions to compute the volume, surface area and storage efficiency of the can.
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

        if cost_efficiency_list[i] > best_cost_efficiency:
            best_cost_efficiency = cost_efficiency_list[i]
            
        if storage_efficiency_list[i] > best_storage_efficiency:
            best_storage_efficiency = storage_efficiency_list[i]


    print(f"\nBest storage efficiency: {best_storage_efficiency:.2f}")
    print(f"Best cost efficiency: {best_cost_efficiency:.2f}")



# Computes and return the volume by using the radius and height of the can.
def compute_volume(radius,height):
    volume = math.pi * radius**2 * height
    return volume

# Computes and return the surface area by using the radius and the height of the can.
def compute_surface_area(radius,height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# Computes and return the storage efficiency of the can by using the volume and surface area.
def compute_storage_efficiency(volume,surface_area):
    storage_efficiency = volume / surface_area
    storage_efficiency_list.append(storage_efficiency)
    return storage_efficiency

def compute_cost_efficiency(volume,cost):
    cost_efficiency = volume / cost
    cost_efficiency_list.append(cost_efficiency)
    return cost_efficiency

main()