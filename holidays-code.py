import pandas as pd
import holidays

# Define the years and the countries/states
years = range(2015, 2021)
countries = ['US', 'PR']

# Initialize a dictionary to store holiday data
holiday_data = {}

# Iterate through years and countries to collect holiday data
for year in years:
    for country in countries:
        # Create a holiday instance for the specified country and year
        country_holidays = holidays.CountryHoliday(country, years=year)
        for date, name in sorted(country_holidays.items()):
            if date in holiday_data:
                holiday_data[date]['Country'].append(country)
            else:
                holiday_data[date] = {'Date': date, 'Name': name, 'Country': [country], 'Year': year}


holiday_data_list = list(holiday_data.values())
df = pd.DataFrame(holiday_data_list)
df['Country'] = df['Country'].apply(lambda x: ', '.join(x))

df.to_excel('US-PR-holidays.xlsx', index=False)
