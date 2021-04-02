# Analyzing data

# This script analyze data and compute some descriptive statistics

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

# 2 Descriptive statistics
#my_data


# -------------------------------------------------------------------------


# Test des statistiques avec la variable Study

# Sous-ensemble d'une activité particulière
study <- my_data %>% filter(activity == "Study")

# Arrangé par date (au cas ou)
study <- study %>% arrange(datetime)

# Fin de l'activité moins le début
start <- study %>% filter(status == "start") %>% pull()
end <- study %>% filter(status == "end") %>% pull()
raw_time <- end - start
# Time difference of 24.21883 secs

# Extract pauses
pause <- study %>% filter(status == "pause") %>% pull()

# Extract unpauses
unpause <- study %>% filter(status == "unpause") %>% pull()

# Length of each vectors

# Testing pause 
if (length(pause) == length(unpause)) {
  pause_time <- sum(unpause - pause)
} else if (length(pause) > length(unpause)) {
  unpause_end <- c(unpause, end)
  pause_time <- sum(unpause_end - pause)
}

# True total time
working_time <- raw_time - pause_time

pause_time

# Example of first descriptive statistics

list(
  travail = c(
    activity = "Study",
    working_time = working_time
    ),
  pause = c(
    n_pause = length(pause),
    mean = mean(unpause_end - pause),
    sd = sd(unpause_end - pause),
    min = min(unpause_end - pause),
    max = max(unpause_end - pause)
  )
)



"----Travail----"

"Activité"
"Study"

"Temps de travail"
"12 minutes"

"Nombre de section de travail"
"3"

"Moyenne"
"Écart type"
"Min"
"Max"

"Temps de pause"
"15 minutes"

"Nombre de pause"
"2"

"Moyenne de la durée des pauses"



list(
  pas
)

