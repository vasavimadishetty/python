import csv

def write_result(principal, rate, time, result):
    """This functions appends the results to the end of the file
    """
    with open("results.csv", "a") as writer:
        writer.write(f"{principal},{rate},{time},{result}\n")

def  