from sistema_solar_3d import SolarSystem, Sun, Planet
solar_system = SolarSystem(400, projection_2d=True)
sun = Sun(solar_system)
planets = (
    Planet(
        solar_system,
        10,
        position=(0, 120, 0),
        velocity=(-9, 0, 0),
    )
)
while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()


'''
    Planet(
        solar_system,
        10,
        position=(100, 100, 0),
        velocity=(-4, 5, 5),
    )
'''
