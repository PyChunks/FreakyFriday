# Data import

# This script imports, cleans and exports data in a rds format

# Packages
library(readr)
library(dplyr)
library(lubridate)

# Functions
# s/o

# Settings
# a. Directory where to save datasets
data_dir <- "data"
# b. Path to save datasets
data_path <- "data/data_fake.rds"

# 0. Creating fake dataset (for now)
# 0.1 Taking actual datetime
now_time <- Sys.time()

# 0.2 Generating random duration between 1 day (86400 seconds) 
#     and 2 weeks (1209600 seconds)
random_duration <- sort(
  sample(86400:1209600, 10)
)

# 0.3 Initiating a dataset of fake dates
data_fake <- tibble(button_pushed = now_time + random_duration)

# 0.4 Writing fake dataset
if (dir.exists(data_dir) == FALSE) {dir.create(data_dir)}
write_rds(data_fake, "data/data_fake.rds")
