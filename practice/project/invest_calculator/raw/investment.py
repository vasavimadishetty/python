"""This is a cli tool to calculate investment returns
Author: shaikkhajaibrahim
"""
import argparse
from investment import lumpsum

def argument_parser():
    """
    This method creates an argument parser
    """
    parser = argparse.ArgumentParser(
        description="Investment Calculator")
    parser.add_argument('lumpsum',type=str)
    parser.add_argument(
        'total_investement', 
        'investment_type',
        type=str,
        choices=['lumpsum'],
        help="investment type"
        )
    parser.add_argument(
        '-p',
        '--principal', 
        type=int,
        required=True,
        help="present value of investment")
    parser.add_argument(
        'intrest_rate',
        '-r',
        '--rate',
        type=int,
        required=True,
        help="rate of intrest")
    parser.add_argument(
        'time_period',
        '-t',
        '--time',
        type=int,
        required=True,
        help="time in years")
    return parser

if __name__ == "__main__":
    args = argument_parser().parse_args()
    result = lumpsum(
        prinicpal= args.total_investement,
        intrest_rate=args.intrest_rate,
        time_in_years=args.time_period
    )
    print(f"Your investment of {args.total_investement} will be {result} in next {args.time_period} years")


    if args.investment_type == 'lumpsum':
        result = lumpsum(
            prinicpal= args.principal,
            intrest_rate=args.rate,
            time_in_years=args.time
        )
        print(f"Your investment of {args.principal} will be {result} in next {args.time} years")