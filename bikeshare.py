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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=('chicago','new york city','washington')
    while True:
        city = input('Would you like to see data for Chicago, New York City or Washington ').lower()
        if city in cities:
            break 
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june']
    month=input('By wich month do you like to filter the data?january,february,march,april,may or june?'.format(months)).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day=input('By wich day of week would you like to filter?monday,tuesday,wednesday,thursday,friday,saturday or sunday?'.format(days)).lower()
    print('-'*40)
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
    try:
        df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time'])
        
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        if month != 'all':
           
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1

          
            df = df[df['month'] == month]

      
        if day != 'all':
            
            df = df[df['day_of_week'] == day.title()]



        return df
  
    except ValueError as e:
        print(e.args)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    try:

        # TO DO: display the most common month
        print('Most common month is',df['month'].value_counts().idxmax())

        # TO DO: display the most common day of week
        print('Most common day of week is',df['day_of_week'].value_counts().idxmax())
  
        # TO DO: display the most common start hour
        print('Most common start hour is',df['Start Time'].value_counts().idxmax())

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    
    except ValueError as e:
        print(e.args)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    try:
      # TO DO: display most commonly used start station
      print('most commonly used start station is',df['Start Station'].value_counts().idxmax())

      # TO DO: display most commonly used end station
      print('most commonly used end station is',df['End Station'].value_counts().idxmax())


      # TO DO: display most frequent combination of start station and end station trip
      print('most requent combination of start station and end station trip is',df.groupby(['Start Station','End Station']).size().idxmax())

    except Exception as e:
        pass
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    try:
      # TO DO: display total travel time
      print('total travel time:',sum(df['Trip Duration']))

      # TO DO: display mean travel time
      print('mean travel time:',df.loc[:, "Trip Duration"].mean())
    except ValueError as e:
        print(e.args)
    except Exception as e:
        print(e.args)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
      # TO DO: Display counts of user types
      print(' User Types Data :',df['User Type'].value_counts())

      # TO DO: Display counts of gender
      print(' Gender Type Stats :',df['Gender'].value_counts())

      # TO DO: Display earliest, most recent, and most common year of birth
      print('Earliest Birth Year, Most Recent Birth Year,Most Common Birth Year ->',df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].value_counts().idxmax)

    except KeyError as e:
        print(e.args)
    except Exception as e:
        print(e.args)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    choice=input(' do you want to see raw data? yes/no?').lower()
    if choice=='yes' or choice=='y' or choice=='yus':
       choice=True
    elif choice=='no' or choice=='n'  or choice=='nope':
        choice=False
    else: 
       print('not vaild choice. Try again')
       display_data(df)
       return 
    if choice:
          while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            choice = input('do you want to see more 5 lines of raw data? yes/no ').lower()
            if choice=='yes' or choice=='y' or choice=='yus':
                continue
            elif choice=='no' or choice=='n'  or choice=='nope':
                break
            else:
                print('not valid choice')
                return
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
 

if __name__ == "__main__":
	main()
