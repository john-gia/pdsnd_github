import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # assign variables for use in user input assessment
    filter_choice = ""
    filter_type = ""


    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print('\nPlease enter the city you would like to see data for -')

    while True:
        city = input('Data available for Chicago, New York City or Washington: ')

    # loop to check if substring of city name is used to accept entry
    # allow check to occur if string greater than 2 characters entered

        if len(city) > 2:
            for available_city in CITY_DATA:
                if (city.lower() in available_city):
                    city = available_city.lower()

    # if statement to check entry and ask user to enter again if user input not in CITY_DATA

        if (city.lower() not in CITY_DATA):
            print('\nNo data available for that. Please choose an available city name.\n')
        else:
            break

    # ask user whether they want to filter data


    while True:
        filter_choice = input('\nWould you like to filter the data. Please enter Yes or No: ')
        if filter_choice.lower() not in ('yes', 'no'):
            print('\nNot an approriate choice. Please try again')
        else:
            break



    # get user to input filters for month (all, january, february, ... , june)
    # and day (Sunday, Monday, Tuesday, ........ , Saturday) dpending on selected filter options

    if filter_choice == 'yes':
        while True:
            filter_type = input('\nWould you like to filter by month, day or both? ')
            if filter_type.lower() not in ('month', 'day', 'both'):
                print('\nNot an approriate choice. Please try again\n')
            else:
                break

    if filter_type == 'month':
        while True:
            day = 'all'
            month = input('Which month? January, February, March, April, May or June? ')
            if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june'):
                print('\nNot an approriate choice. Please try again\n')
            else:
                break
    elif filter_type == 'day':
        while True:
            month = 'all'
            day = input('Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday? ')
            if day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
                print('\nNot an approriate choice. Please try again')
            else:
                break
    elif filter_type == 'both':
        while True:
            month = input('Which month? January, February, March, April, May or June? ')
            if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june'):
                print('\nNot an approriate choice. Please try again\n')
            else:
                break
        while True:
            day = input('Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday? ')
            if day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
                print('\nNot an approriate choice. Please try again')
            else:
                break

    # if no filters where requested set moth and day to 'all'

    if filter_choice == 'no':
        month = 'all'
        day = 'all'



    print('-'*80)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    month_labels = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}

    # convert Start Time column to time data variable
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # add new columns in dataframe for start hour of travel
    df["travel_hour"] = (df["Start Time"].dt.hour)

    # TO DO: display the most common month
    mcommon_month = df["month"].mode()
    m_val= int(mcommon_month.to_string(index=False))

    print("Most common Travel Month: {}".format(month_labels.get(m_val)))

    # TO DO: display the most common day of week
    mcommon_day = df["day_of_week"].mode()
    d_val = (mcommon_day.to_string(index=False))

    print("  Most common Travel Day: {}".format(d_val))

    # TO DO: display the most common start hour
    mcommon_st_hour = df["travel_hour"].mode()
    h_val = int(mcommon_st_hour.to_string(index=False))


    print("Most common Travel Start: {:02d}:00 hrs".format(h_val))

    # Calculate code run time and display results.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mc_st_station = df["Start Station"].mode()
    sstation_val = (mc_st_station.to_string(index=False))

    print("Most commonly used Start Station(s): \n{}".format(sstation_val))

    # TO DO: display most commonly used end station
    mc_en_station = df["End Station"].mode()
    estation_val = (mc_en_station.to_string(index=False))

    print("\nMost commonly used End Station(s): \n{}".format(estation_val))

    # TO DO: display most frequent combination of start station and end station trip
    mc_trip = df.groupby(["Start Station", "End Station"]).size().nlargest(1)

    print("\nMost frequent combination(s) of Start Station and End Station: \n\n{}".format(mc_trip))

    # Calculate code run time and display results.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # provide trip count to improve user understanding
    trip_count = (df["Trip Duration"].count())
    print("Total count of trips: {}".format(trip_count))

    # TO DO: display total travel time
    total_t_time = (df["Trip Duration"].sum() / 3600)

    print("Total Travel Time:  {:.2F} hrs".format(total_t_time))
    # TO DO: display mean travel time

    mean_t_time = (df["Trip Duration"].mean() / 60)

    print("Mean Travel Time:  {:.2F} mins".format(mean_t_time))

    # Calculate code run time and display results.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # check for nulls
    if df["User Type"].isnull().sum() > 1:
            df["User Type"].fillna("Unknown", inplace = True)

    user_type_count = df["User Type"].value_counts()
    print("Count of User Types: \n{}".format(user_type_count))


    # TO DO: Display counts of gender
    # Check Gender exists in dataset and update any nulls
    if "Gender" in df.columns:
        if df["Gender"].isnull().sum() > 1:
            df["Gender"].fillna("Unknown", inplace = True)
            gender_count = df["Gender"].value_counts()
            print("\nCount of Gender Types: \n{}".format(gender_count))
    else:
        print("\nNo Gender data available in this dataset.")

    # TO DO: Display earliest, most recent, and most common year of birth

    if "Birth Year" in df.columns:
        min_birth_year = int(df["Birth Year"].min())
        max_birth_year = int(df["Birth Year"].max())
        mode_birth_year = int(df["Birth Year"].mode())
        print("\nUser Birth Year Statistics: \nBirth Year (Earliest): {}".format(min_birth_year))
        print("Birth Year (Most recent): {}".format(max_birth_year))
        print("Birth Year (Most common): {}".format(mode_birth_year))
    else:
        print("\nNo Birth Year data available in this dataset.")

    # Calculate code run time and display results.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def raw_data(df):
    """
    Identifies the total number of rows related to the dataset then
    asks the user if they would like to view 5 rows of raw data.

    Output will continues to display additional 5 rows of raw data if user chooses
    to view an additional data.
    """

    total_rows = len(df)

    print("Total number of rows associated with this dataset: {}".format(total_rows))

    # Ask user if they would like to see 5 rows of data
    while True:
        raw_data_choice = input('\nWould you like to view 5 rows of raw data. Please enter Yes or No: ')
        if raw_data_choice.lower() not in ('yes', 'no'):
            print('\nNot an approriate choice. Please try again')
        else:
            break

    if raw_data_choice == "yes":
        print(df.head())
        start_loc = 5

        # use while loop to keep showing additional 5 rows of data if user does not choose to exit.
        while start_loc < total_rows:
            if input("Enter 'no' to exit or enter to continue viewing data: ") != "no":
                start_loc = start_loc + 5
                print(df.head(start_loc))
            else:
                break

    print('-'*80)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Display user inputs for City, Day and Month chosen by user.
        print("Data Analysis for:\n City: {} \nMonth: {} \n  Day: {}".format(city.title(), month.title(), day.title()))
        print('-'*80)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        # Ask user if they would like to restart and run another analysis.
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
