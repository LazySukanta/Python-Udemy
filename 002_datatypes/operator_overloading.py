base_liquid = ["water","milk"]
extra_flavoue = ["ginger"]

full_liquid_mix = base_liquid + extra_flavoue
print(full_liquid_mix)

strong_brew = ["black tea","water"]*3
print(strong_brew)


# from operator import itemgetter

raw_spice_data = bytearray(b"CINNEMON")
raw_spice_data = raw_spice_data.replace(b"CINNE",b"CARD")
print(raw_spice_data)