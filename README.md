# Smart Traffic Monitoring and Adaptive Signal Control Platform

## Project Overview

The Smart Traffic Monitoring and Adaptive Signal Control Platform is a software system designed to monitor traffic conditions and dynamically determine traffic signal timing based on vehicle density.

## Objectives

- Monitor the number of vehicles.
- Classify traffic conditions.
- Dynamically determine green signal duration.
- Store traffic records.
- Provide a simple traffic monitoring dashboard.

## Technology Stack

- HTML
- CSS
- JavaScript
- Python
- Flask
- SQLite
- Git/GitHub
- Docker

## Traffic Control Logic

| Vehicle Count | Traffic Level | Green Signal |
|---|---|---|
| 0–20 | LOW | 30 seconds |
| 21–50 | MEDIUM | 45 seconds |
| 51–80 | HIGH | 60 seconds |
| 81+ | VERY HIGH | 90 seconds |

## Project Structure

```text
Smart-Traffic-Monitoring/
├── backend/
├── frontend/
├── database/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md