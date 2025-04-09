import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

CITY_DATA = { 'chicago': 'C:/Users/mark maher/OneDrive - Higher Technological Institute/Desktop/Projects/Second project/chicago (1).csv',
              'new york city': 'C:/Users/mark maher/OneDrive - Higher Technological Institute/Desktop/Projects/Second project/new_york_city (1).csv',
              'washington': 'C:/Users/mark maher/OneDrive - Higher Technological Institute/Desktop/Projects/Second project/washington (1).csv' }

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = input("Would you like to see the data for Chicago, New York City or Washington? ").lower()
    while city not in (CITY_DATA.keys()):
        print("You provided invalid city name")
        city = input("Would you like to see the data for Chicago, New York City or Washington? ").lower()
    filtering = input("Would you like to filter the data by Month, Day, Both, None? ").lower()
    while filtering not in (["month", "day", "both", "none"]):
        print("You put invalid filter, Try again!")
        filtering = input("Would you like to filter the data by month, day, both, none? ").lower()
    
    months = ["january", "february", "march", "april", "may", "june"]
    if filtering == "month" or filtering == "both":
        month = input("Choose month, January, February, March, April, May or June? ").lower()
        while month not in(months):
            print("Invalid month, Try again")
            month = input("Choose month, January, February, March, April, May or June? ").lower()
    else:
        month = 'all'
            
    
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if filtering == "day" or filtering == "both":
        day = input("Choose day, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday? ").title()
        while day not in (days):
            print("Invalid day, Try again")
            day = input("Choose day, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday? ").title()
    else:
        day = 'all'
            

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ["january","february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df =df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    months = ["january", "february", "march", "april", "may", "june"]
    month = df['month'].mode()[0]
    print("The most common month is {}".format(months[month - 1]))
    
    day = df['day_of_week'].mode()[0]
    print("The most common day of week is {}".format(day))


    
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common hour is {}".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    popular_start_station = df['Start Station'].mode()[0]
    print("The most popular start station is {}".format(popular_start_station))

    
    popular_end_station = df['End Station'].mode()[0]
    print("The most popular end station is {}".format(popular_end_station))

    
    popular_trip = df['Start Station'] + ' to ' + df['End Station']
    print("The most popular trip is from {}".format(popular_trip.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    total_travel_duration = (pd.to_datetime(df['End Time']) -pd.to_datetime(df['Start Time'])).sum()
    days = total_travel_duration.days
    hours = total_travel_duration.seconds // (60*60)
    minutes = total_travel_duration.seconds % (60*60) // 60
    seconds = total_travel_duration.seconds % (60*60) % 60
    print("Total travel time is: {} days, {} hours, {} seconds".format(days, hours, seconds))
    
    average_travel_duration = (pd.to_datetime(df['End Time'])- pd.to_datetime(df['Start Time'])).mean()
    days = average_travel_duration.days
    hours = average_travel_duration.seconds // (60*60)
    minutes = average_travel_duration.seconds % (60*60) // 60
    seconds = average_travel_duration.seconds % (60*60) % 60
    print("Average travel time is: {} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    print(df['User Type'].value_counts())


    
    if 'Gender' in (df.columns):
        print(df['Gender'].value_counts())


   
    if 'Birth Year' in (df.columns):
        year = df['Birth Year'].fillna(df['Birth Year'].mean()).astype('int64')
        print("The earliest year of birth is {}, The most recent year of birth is {}, the most common year of birth is {}". format(year.min(),year.max(),year.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def my_plot(df):
    plt.figure(figsize = [15,8])
    sns.countplot(x = 'hour', data=df, palette='CMRmap', hue='Gender')
    plt.show()
def display_raw_data(df):
    raw = input("\nWould you like to display raw data?\n ")
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count : count + 5])
            count += 5
            ask = input("Do you need the next 5 raws? ")
            if ask != 'yes':
                break
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        my_plot(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
