def area_of_circle(r):
    pi = 3.14
    area = pi * r * r
    return area


# define length of weapons in meters
sword_length = 1.0
spear_length = 2.0
dagger_length = 0.5
whip_length = 3.0
scythe_length = 2.75

# calculate how much area weapons can cover in a 360 degree circle around the player
sword_area_of_attack = area_of_circle(sword_length)
spear_area_of_attack = area_of_circle(spear_length)
dagger_area_of_attack = area_of_circle(dagger_length)
whip_area_of_attack = area_of_circle(whip_length)
scythe_area_of_attack = area_of_circle(scythe_length)

# tell the player the attack radius of these weapons
print("Attack radiuses of various weapon types:\n")

print(
    f"The sword, which is {sword_length} meters long, has an attack radius of {sword_area_of_attack} meters. A dependable, albeit unremarkable weapon. It receives no damage bonuses or damage penalties, whether attacking head on or in an arc.\n"
)
print(
    f"The spear, which is {spear_length} meters in length, has an attack radius of {spear_area_of_attack} meters. However, the spear is most effective when attacking in a single direction. I can hit two foes at once as long as one is directly behind the other. It deals increased damage at short range, slightly increased damage at mid-range, and recieves a damage penalty when used in an arc.\n"
)
print(
    f"The dagger, which is {dagger_length} meters in length, has a small attack radius of {dagger_area_of_attack} meters. It can attack in an arc, but deals significantly less damage. However, if used on a single foe directly adjacent to you, it deals critical damage.\n"
)
print(
    f"The whip, which is {whip_length} meters in length, has a wide attack radius of {whip_area_of_attack} meters. It hits all enemies in its effective range. It deals increased damage against the first foe hit, however, each enemy after that takes less damage than the one before it.\n"
)
print(
    f"The scythe, which is {scythe_length} meters in length, is a rare, deadly weapon with an attack radius of {scythe_area_of_attack} meters. Powerful in almost all cases, capable of consistent damage across all enemies hit (max of 4 at one time). The first foe that is hit recieves increased damage.\n"
)
