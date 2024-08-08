import argparse
from datetime import datetime, timedelta

def date_difference(date1, date2):
    format = "%Y-%m-%d"  # format des dates (année-mois-jour)
    d1 = datetime.strptime(date1, format)
    d2 = datetime.strptime(date2, format)
    return abs((d2 - d1).days)

def add_days_to_date(date, days):
    format = "%Y-%m-%d"
    d = datetime.strptime(date, format)
    return (d + timedelta(days=days)).strftime(format)

def subtract_days_from_date(date, days):
    format = "%Y-%m-%d"
    d = datetime.strptime(date, format)
    return (d - timedelta(days=days)).strftime(format)


parser = argparse.ArgumentParser(description='Date calculation tool')

subparsers = parser.add_subparsers(dest='command', help='Sub-command help')

diff_parser = subparsers.add_parser('diff', help='Calculate the difference in days between two dates')
diff_parser.add_argument('date1', type=str, help='The first date in YYYY-MM-DD format')
diff_parser.add_argument('date2', type=str, help='The second date in YYYY-MM-DD format')

add_parser = subparsers.add_parser('add', help='Add days to a date')
add_parser.add_argument('date', type=str, help='The date in YYYY-MM-DD format')
add_parser.add_argument('days', type=int, help='The number of days to add')

sub_parser = subparsers.add_parser('sub', help='Subtract days from a date')
sub_parser.add_argument('date', type=str, help='The date in YYYY-MM-DD format')
sub_parser.add_argument('days', type=int, help='The number of days to subtract')

args = parser.parse_args()

if args.command == 'diff':
    result = date_difference(args.date1, args.date2)
    print(f"Différence en jours : {result}")

elif args.command == 'add':
    result = add_days_to_date(args.date, args.days)
    print(f"Nouvelle date après ajout de {args.days} jours : {result}")

elif args.command == 'sub':
    result = subtract_days_from_date(args.date, args.days)
    print(f"Nouvelle date après soustraction de {args.days} jours : {result}")
