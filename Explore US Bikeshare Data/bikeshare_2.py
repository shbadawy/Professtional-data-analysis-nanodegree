#!/usr/bin/env python
# coding: utf-8

# In[59]:


import time
import pandas as pd
import numpy as np


# In[60]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[61]:


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
    # # This project is done by Eng.Shimaa Badawy @shbadawy
    city = input ("Please enter the city (chicago, new york city, washington):").lower()
    
    while (city not in CITY_DATA.keys()):
        city = input ("Please enter the city (chicago, new york city, washington):").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april", "may", "june"]
    month = input ("Please enter the month (all, january, february, march, april, may, june):").lower()
    
    while (month not in months) and (month != "all"):
        month = input ("Please enter the month (all, january, february, march, april, may, june):").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    ## This project is done by Eng.Shimaa Badawy @shbadawy
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = input ("Please enter the day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday):").lower()
    
    while (day not in days) and (day != "all"):
        day = input ("Please enter the day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday):").lower()

    print('-'*40)
    return city, month, day


# In[62]:


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

    if city == "new york city":
        city = "new_york_city"
        
    df = pd.read_csv("{}.csv".format(city)) 

    return df


# In[63]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    dates = pd.to_datetime(arg= df["Start Time"],dayfirst=True)
    df["month"] = [dates[i].month for i in range (len (dates))]
    df["day"] = [dates[i].day for i in range (len (dates))]
    df["hour"] = [dates[i].hour for i in range (len (dates))]
    MCMonth = df["month"].value_counts(sort=True , ascending=False).keys()[0]
    MCDay = df["day"].value_counts(sort=True , ascending=False).keys()[0]
    MCHour = df["hour"].value_counts(sort=True , ascending=False).keys()[0]
    # display the most common month
    # This project is done by Eng.Shimaa Badawy @shbadawy
    
    print ("The most common month: {}".format (MCMonth) )
    
    # display the most common day of week
    ## This project is done by Eng.Shimaa Badawy @shbadawy

    print ("The most common day: {}".format (MCDay) )

    # display the most common start hour
    # This project is done by Eng.Shimaa Badawy @shbadawy
    print ("The most common start hour: {}".format (MCHour) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[64]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    MCstart = df["Start Station"].value_counts(sort=True , ascending=False).keys()[0]
    print ("The most commonly used start station: {}".format(MCstart))
    
    # display most commonly used end station
    # This project is done by Eng.Shimaa Badawy @shbadawy
    MCEnd = df["End Station"].value_counts(sort=True , ascending=False).keys()[0]
    print ("The most commonly used end station: {}".format(MCEnd))
    
    # display most frequent combination of start station and end station trip
    df ["trip combination"] = df["Start Station"]+" - "+df["End Station"]
    MCstartEnd = df["trip combination"].value_counts(sort=True , ascending=False).keys()[0]
    print ("The most frequent combination of start station and end station trip: {}".format(MCstartEnd))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[65]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totalDuration = df["Trip Duration"].sum()
    print ("The total travel time: {}".format(totalDuration))

    # display mean travel time
    totalDuration = df["Trip Duration"].mean()
    print ("The mean travel time: {}".format(totalDuration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[66]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print ("Counts of user types")
    usersTypes = df["User Type"].value_counts(sort=True , ascending=False)
    for types in usersTypes.keys():
        print ("{}:{}".format (types,usersTypes[types]))
        
    print ("-"*40)

    # Display counts of gender
    print ("Counts of gender")
    usersGender = df["Gender"].value_counts(sort=True , ascending=False)
    for types in usersGender.keys():
        print ("{}:{}".format (types,usersGender[types]))
    
    print ("-"*40)
    # Display earliest, most recent, and most common year of birth
    # This project is done by Eng.Shimaa Badawy @shbadawy
    birthData = df["Birth Year"].dropna().sort_values(ignore_index=True)
    MCBirthYear = birthData.value_counts(sort=True , ascending=False).keys()[0]
    print ("The earliest common year of birth: {}".format (birthData[0]))
    print ("The most recent common year of birth: {}".format (birthData[len(birthData)-1]))
    print ("The most common year of birth: {}".format (MCBirthYear))
    
    print ("-"*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[70]:


def display_data (df):
    showData = input("Do you want to see 5 rows of the data? (yes/no)").lower()
    i = 1
    while (showData != "yes" and showData != "No"):
        showData = input("Do you want to see 5 rows of the data? (yes/no)").lower()
    
    while (showData == "yes"):
        print (df.iloc[(i-1)*5:(i*5)-1])
        
        showData = input("Do you want to see more 5 rows of the data? (yes/no)").lower()

        while (showData != "yes" and showData != "no"):
            showData = input("Do you want to see more 5 rows of the data? (yes/no)").lower()
        i+=1
    


# In[71]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


# In[72]:


if __name__ == "__main__":
    main()


# In[ ]:




