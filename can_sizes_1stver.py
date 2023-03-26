"""Compute and print the storage efficiency of a can."""

# Import the standard math module so that
# math.pi can be used in this program.
import math

def main():

    # Give values to the variables name, radius and height to compute the storage efficiency.
    # Calls the funtions to compute the volume, surface area and storage efficiency of the can.
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    cost = 0.28
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.2f} - {cost_efficiency:.2f}")

    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    volume = compute_volume(radius,height)
    surface_area = compute_surface_area(radius,height)
    storage_efficiency = compute_storage_efficiency(volume,surface_area)
    print(f"{name} {storage_efficiency:.2f}")

    name = "#2"
    radius = 8.73
    height = 11.59
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name} {storage_efficiency:.2f}")

    name = "#2.5"
    radius = 10.32
    height = 11.91
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name} {storage_efficiency:.2f}")

    name = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name} {storage_efficiency:.2f}")

    name = "#5"
    radius = 13.02
    height = 14.29
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name} {storage_efficiency:.2f}")

    name = "#6Z"
    radius = 5.40
    height = 8.89
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name} {storage_efficiency:.2f}")

    name = "#8Z short"
    radius = 6.83
    height = 7.62
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name} {storage_efficiency:.2f}")

    name = "#10"
    radius = 15.72
    height = 17.78
    volume = compute_volume(radius,height)
    surface_area = compute_surface_area(radius,height)
    storage_efficiency = compute_storage_efficiency(volume,surface_area)
    print(f"{name} {storage_efficiency:.2f}")

    name = "#211"
    radius = 6.83
    height = 12.38
    volume = compute_volume(radius,height)
    surface_area = compute_surface_area(radius,height)
    storage_efficiency = compute_storage_efficiency(volume,surface_area)
    print(f"{name} {storage_efficiency:.2f}")

    name = "#300"
    radius = 7.62
    height = 11.27
    volume = compute_volume(radius,height)
    surface_area = compute_surface_area(radius,height)
    storage_efficiency = compute_storage_efficiency(volume,surface_area)
    print(f"{name} {storage_efficiency:.2f}")

    name = "#303"
    radius = 8.10
    height = 11.11
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name} {storage_efficiency:.2f}")



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
    return storage_efficiency

def compute_cost_efficiency(volume,cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()