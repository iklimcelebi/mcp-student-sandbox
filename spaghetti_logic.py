def calculate_total(value, rate=1.15):
    """
    Calculate the total value by multiplying with a rate.

    Args:
        value (float): The base value.
        rate (float): The multiplication rate. Default is 1.15.

    Returns:
        float: The calculated total.
    """
    return value * rate


def format_total(total):
    """
    Format the total value as a string.

    Args:
        total (float): The total value.

    Returns:
        str: Formatted string.
    """
    return f"Total: {total:.2f}"


def log_results(results, filename="log.txt"):
    """
    Log the results to a file.

    Args:
        results (list): List of results to log.
        filename (str): The log file name. Default is 'log.txt'.
    """
    with open(filename, "a") as f:
        f.write(str(results) + "\n")


def process_data(data, rate=1.15):
    """
    Process the data: calculate totals, print formatted strings, log results.

    Args:
        data (list): List of values to process.
        rate (float): The rate for calculation. Default is 1.15.

    Returns:
        list: List of calculated totals.
    """
    results = []
    for value in data:
        total = calculate_total(value, rate)
        formatted = format_total(total)
        print(formatted)
        results.append(total)
    log_results(results)
    return results
