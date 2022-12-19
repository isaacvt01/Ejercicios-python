def fix_the_meerkat(arr):
    array_corregido = list(reversed(arr))
    return array_corregido







array1 = "tail", "body", "head"




if __name__ == "__main__":
    assert fix_the_meerkat(array1) == ["head", "body", "tail"]
    assert fix_the_meerkat["tails", "body", "heads"] == ["heads", "body", "tails"]
    assert fix_the_meerkat["bottom", "middle", "top"] == ["top", "middle", "bottom"]
    assert fix_the_meerkat["lower legs", "torso", "upper legs"] == ["upper legs", "torso", "lower legs"]
    assert fix_the_meerkat["ground", "rainbow", "sky"] == ["sky", "rainbow", "ground"]