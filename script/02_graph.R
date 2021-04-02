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
# a. Directory where to save datasets
data_dir <- "data"
# b. Path used to import rawdata
data_import <- "data/activity.rds"

# -------------------------------------------------------------------------

# 1 Importing data
my_data <- read_rds(data_import)

# 2 Generating data

# TODO