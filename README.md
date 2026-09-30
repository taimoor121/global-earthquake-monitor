# Global Earthquake Monitor

A small Python program that automatically retrieves the earthquake catalog
for the current UTC day from the USGS Earthquake Catalog and identifies
the earthquake with the largest magnitude.

## Features

- Automatically detects the current UTC date
- Downloads global earthquake data from the USGS
- Counts earthquakes recorded during the day
- Identifies the largest-magnitude earthquake
- Displays:
  - Magnitude
  - Location
  - Depth
  - Latitude
  - Longitude
  - Origin time (UTC)
  - USGS event link
- Handles internet connection and USGS response errors

## Requirements

- Python 3.10 or newer
- Internet connection
- `requests` Python package

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/global-earthquake-monitor.git
cd global-earthquake-monitor

Install the required Python package:

pip install -r requirements.txt
Usage

##Run:

python3 earthquake_monitor.py

The program automatically determines the current UTC date, downloads
the earthquake data from USGS, and identifies the largest earthquake
recorded during that day.

Example Output
=======================================================
             GLOBAL EARTHQUAKE MONITOR
=======================================================

Date (UTC): 30 September 2026
Earthquakes detected: 115

LARGEST EARTHQUAKE
-------------------------------------------------------

Magnitude  : 5.6
Location   : 74 km S of Yonakuni, Japan
Depth      : 10.8 km
Latitude   : 23.8027
Longitude  : 122.9149
Time (UTC) : 2026-09-30 10:00:24

USGS Event:
https://earthquake.usgs.gov/earthquakes/eventpage/...

=======================================================
Data Source

Earthquake data are retrieved from the
USGS Earthquake Catalog.

The program uses the USGS FDSN Event Web Service.

Purpose

This project was developed as a small practical seismology and Python
project for automatically monitoring daily global earthquake activity.

License

This project is provided for educational and research purposes.
