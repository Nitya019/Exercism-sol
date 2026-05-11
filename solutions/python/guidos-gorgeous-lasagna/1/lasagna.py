# Functions used in preparing Guido's gorgeous lasagna.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time in minutes.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    Parameters:
        number_of_layers (int): Total layers in lasagna.

    Returns:
        int: Total preparation time in minutes.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time.

    Parameters:
        number_of_layers (int): Total layers in lasagna.
        elapsed_bake_time (int): Actual baking time elapsed.

    Returns:
        int: Total elapsed cooking time in minutes.
    """
    return (number_of_layers * PREPARATION_TIME) + elapsed_bake_time