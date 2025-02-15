"""This is an arithmetic operations library supporting dynamic inputs."""

def add(*args):
    """
    Adds multiple numbers together.

    Parameters:
        *args (float|int): Numbers to be added.

    Returns:
        float|int: The sum of all input numbers.
    """
    return sum(args)


def sub(*args):
    """
    Subtracts multiple numbers in sequence.

    Parameters:
        *args (float|int): Numbers to be subtracted.

    Returns:
        float|int: The result after sequential subtraction.
    
    Raises:
        ValueError: If no arguments are provided.
    """
    if not args:
        raise ValueError("At least one number is required")
    
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def mul(*args):
    """
    Multiplies multiple numbers together.

    Parameters:
        *args (float|int): Numbers to be multiplied.

    Returns:
        float|int: The product of all input numbers.
    
    Raises:
        ValueError: If no arguments are provided.
    """
    if not args:
        raise ValueError("At least one number is required")
    
    result = 1
    for num in args:
        result *= num
    return result


def div(*args):
    """
    Divides multiple numbers in sequence.

    Parameters:
        *args (float|int): Numbers to be divided.

    Returns:
        float|int: The result after sequential division.
    
    Raises:
        ValueError: If no arguments are provided.
        ZeroDivisionError: If division by zero is attempted.
    """
    if not args:
        raise ValueError("At least one number is required")
    
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        result /= num
    return result
