# Data import

# This script imports, cleans and exports data in a rds format

# Note: 
# Pour l'instant, je créé des données bidons pour commencer tout de suite à coder

# Packages
library(readr)
library(dplyr)
library(lubridate)

# Functions
# s/o

# Settings

# 0. Creating fake dataset
now_time <- Sys.time()

# 0.1 Separing each datatime element of now_time
my_year <- year(now_time)
my_month <- month(now_time)
my_day <- day(now_time)
my_hour <- hour(now_time)
my_minute <- minute(now_time)
my_second <- second(now_time)

# 0.2 Creating tibble
my_tibble <- tibble(year = my_year,
                    month = my_month,
                    day = my_day,
                    hour = my_hour,
                    minute = my_minute,
                    second = my_second)

# 0.3 Expanding tibble
random_day <- sample(1:20, 5)

# Brouillon...
x <- ymd_hms(Sys.time())
x + ddays(5)
typeof(x)


