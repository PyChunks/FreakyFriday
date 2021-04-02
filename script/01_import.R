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


# 4 Exploration

# NOTE: Est-ce que je crée plusieurs base de données pour chaque activité ?

#quote <- my_data %>%
#  filter(activity == "Study")


#for (n in seq_along(levels(my_data$activity))) {
#  activity_n <- levels(my_data$activity)[n]
#  x <- filter(my_data, activity == activity_n)
#  #activity_name <- paste(activity_n, sep = "_", "data")
#  return(x)
#  }

