def get_planet_name(id):
    # This doesn't work; Fix it!
    if id == 1:
        return 'Mercury'
    if id == 2:
        return 'Venus'
    if id == 3:
        return 'Earth'
    if id == 4:
        return 'Mars'
    if id == 5:
        return 'Jupiter'
    if id == 6:
        return 'Saturn'
    if id == 7:
        return 'Uranus'
    if id == 8:
        return 'Neptune'



if __name__ == "__main__":
    assert get_planet_name(2), 'Venus'
    assert get_planet_name(5), 'Jupiter'
    assert get_planet_name(3), 'Earth'
    assert get_planet_name(4), 'Mars'
    assert get_planet_name(8), 'Neptune'
    assert get_planet_name(1), 'Mercury'