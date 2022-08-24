

EXPECTED_BAKE_TIME = 40
preparation_time_in_minutes = 2


def bake_time_remaining(elapsed_bake_time):
    """
    this will calculate the time remaining after the time elapsed.

    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    calculates how many minutes we spend preparing the layers
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
        Return elapsed cooking time.

        This function takes two numbers representing the number of layers & the time already spent 
        baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time