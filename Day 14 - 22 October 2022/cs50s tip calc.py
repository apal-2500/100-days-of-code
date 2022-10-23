#tip caluclator for US
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar = d.replace("$", "")
    return float(dollar)


def percent_to_float(p):
    no_percent = p.replace("%", "")
    convert = float(no_percent) / 100
    return convert

main()
