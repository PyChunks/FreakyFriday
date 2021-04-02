# Analysing data

# This script analyse data and compute some descriptives statistics

# Packages
library(readr)
library(dplyr)
library(lubridate)
library(ggplot2)

# Functions
# s/o

# Settings
# a. Path used to import rawdata
data_import <- "data/activity.rds"

# -------------------------------------------------------------------------

# 1 Importing data
my_data <- read_rds(data_import)

# 2 Descriptives statistics
my_data


# TO BE CONTINUED

workout <- my_data %>% filter(activity == "Workout")

workout %>% filter(status == "start") %>% pull() - workout %>% filter(status == "end") %>% pull()

workout$status == "start" - workout$status == "end"

