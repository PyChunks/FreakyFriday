# Generating graph

# This script generate graph

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

# 2 Generating graph
ggplot(my_data, aes(x = datetime, y = activity)) +
  geom_line()

