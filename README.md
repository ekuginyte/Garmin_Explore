---
title: "💤 Sleep! Dashboard"
date: "`r Sys.Date()`"
output:
  html_document:
    theme: flatly
    highlight: tango
    toc: true
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE, warning = FALSE, message = FALSE)
library(ggplot2)
library(dplyr)
library(readr)
library(plotly)
library(lubridate)
```

### Project Aim
The goal of this project is to analyse my sleep patterns and identify areas for improvement.
Examine sleep stages - deep, light, REM, awake, and total sleep — to see whether I meet recommended targets for my age and gender.

### Data downloaded from my personal Garmin account

```
# Load and process data
sleep_data <- read_csv("data/sleep_data.csv") %>%
  mutate(
    date = as.Date(calendarDate),
    deep = deepSleepSeconds / 3600,
    light = lightSleepSeconds / 3600,
    rem = remSleepSeconds / 3600,
    awake = awakeSleepSeconds / 3600,
    total = deep + light + rem + awake
  )
head(sleep_data)
```

```
# Define targets
stages <- tibble(
  key = c("deep", "light", "rem", "awake", "total"),
  label = c("Deep Sleep", "Light Sleep", "REM Sleep", "Awake", "Total Sleep"),
  min = c(1.2, 2.8, 1.6, 0, 7.5),
  max = c(2, 4, 2, 0, 8.5),
  color = c("#1f3b4d","#7a5195","#ef5675","#ffa600","#2ca02c")
)

# Compute max y for uniform axes
max_y <- max(sleep_data$total)*1.05
```
