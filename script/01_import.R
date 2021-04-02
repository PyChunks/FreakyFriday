# Importing dataset

# This script imports, names and exports data

# Packages
library(readr)
library(dplyr)
library(lubridate)
library(ggplot2)

# Functions
# s/o

# Settings
# a. Path used to import rawdata
data_import <- "data/activity.csv"
# b. Path used to export data
data_export <- "data/activity.rds"

# -------------------------------------------------------------------------

# 1 Importing data
my_data <- read_csv(file = data_import, 
                    col_names = FALSE,
                    col_types = cols(
                      X1 = col_factor(),
                      X2 = col_factor(levels = c("start", "pause", "unpause", "end")),
                      X3 = col_datetime(format = "")
                    )
)

# 2 Naming variables
my_data <- 
  my_data %>% 
  rename(activity = X1,
         status = X2,
         datetime = X3)

# 3 Exporting variable
write_rds(my_data, data_export)

