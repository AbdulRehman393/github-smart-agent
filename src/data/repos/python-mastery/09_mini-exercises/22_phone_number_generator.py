# Phone Number Generator

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=92, area=319, first=456, last=7267)

print(phone_num)