# Airflow DAG Management Plugin

Advanced DAG schedule management plugin developed for Apache Airflow. This plugin enables you to visualize, manage, and dynamically update DAG schedules through the web interface.

## Features

### Schedule Management
- **Web UI Integration**: Schedule management modal integrated into the Airflow web interface
- **Dynamic Schedule Updates**: Update DAG schedules dynamically through Airflow Variables
- **Schedule Validation**: Cron expression validation and error checking
- **Schedule Clearing**: Support for removing schedules using the "None" option

### Cron Expression Support
- **Single Cron Expression**: Standard cron expression support (`CronTriggerTimetable`)
- **Multiple Cron Expressions**: Use multiple cron expressions for a single DAG (`MultipleCronTriggerTimetable`)
- **Preset Schedules**: Ready-made schedule options (@hourly, @daily, @weekly, @monthly, None)
- **Manual Cron Input**: Direct cron expression input support
- **Visual Cron Builder**: Easy schedule creation with visual cron builder
  - Daily schedule configuration
  - Weekly schedule configuration
  - Custom schedule creation through calendar date selection
  - Multiple date selection support

### Upcoming Runs Preview
- **Calendar View**: Display upcoming DAG runs in calendar format
- **Table View**: List upcoming runs in table format
- **Timezone Support**: Correct time display for different timezones
- **Date Range**: Calculate future runs for 30 days
- **Limit Control**: Maximum 200 run display
- **Real-time Calculation**: Instant run calculation on schedule changes

### Technical Features
- **Custom Timetable Implementation**: Custom timetables integrated into Airflow's timetable system
- **Airflow Variables Integration**: Storage of schedule information through Airflow Variables
- **Cache Mechanism**: Thread-safe cache system for performance optimization
- **Modular Architecture**: Modular code structure following enterprise standards
- **Error Management**: Advanced error handling with custom exception classes
- **Timezone Management**: Timezone reading from Airflow config and environment variable override support
- **Responsive Design**: Interface compatible with mobile and desktop devices
- **CSRF Protection**: Secure API endpoints

### Performance
- **Efficient Run Calculation**: Date range-based run calculation
- **Deduplication**: Automatic cleanup of duplicate runs in multiple cron expressions
- **Caching**: Caching of DAG bag and timezone information
- **Optimized Iteration**: Prevention of unnecessary iterations

### Configuration
- **Environment Variables**: Customize plugin behavior through environment variables
- **Airflow Config Integration**: Use Airflow's default timezone setting
- **Configurable Limits**: Adjustable upcoming runs limit and day count
- **API Route Customization**: Customize API endpoint routes

---

**Note**: This project is actively under development. New features and improvements will be added soon.

https://github.com/user-attachments/assets/ba314a96-bb20-40c7-9860-f581f8368610

