# Web Page Monitor

## Description

The **Web Page Monitor** is a simple Python script that allows users to monitor specific web pages for changes. By checking the content of a specified URL at regular intervals, the script can notify users when changes are detected. This tool is useful for tracking price changes, new content, or any modifications on web pages of interest.

## Features

- Monitors a specified URL for content changes.
- Checks the page at configurable intervals.
- Prints a message to the console when changes are detected.

## Prerequisites

- Python 3.x
- Required Python libraries: `requests`

## Example Screenshot

![Web Page Monitor](https://github.com/user-attachments/assets/9e326169-c9f7-473e-9b1b-8738607e21e9)

## Conclusion
The "**Web Page Monitor**" project is a straightforward yet effective tool for tracking changes on web pages. By utilizing Python's requests and hashlib libraries, the script efficiently checks for content changes at specified intervals. This basic implementation serves as a foundation for users who want to monitor specific web pages for updates, such as price changes, new content, or other relevant modifications. The simplicity of the project makes it accessible for beginners while providing a practical solution for real-world needs.

## Future Enhancements
While the basic functionality is useful, there are several enhancements that could significantly improve the project:

- **Email Notifications**: Implement an email notification system to alert users when changes are detected.
- **Logging**: Add logging functionality to keep track of when checks are made and when changes are detected.
- **Configurable Settings**: Use a configuration file to allow users to specify multiple URLs and check intervals without modifying the code.
- **Change Summary**: Provide a summary of what changed on the page using the difflib library.
- **Multiple URL Monitoring**: Extend the script to monitor multiple URLs simultaneously.
- **Web Interface**: Create a simple web interface using a framework like Flask or Django.
- **User Authentication**: Implement user authentication for the web interface.
- **Mobile Notifications**: Integrate with services like Twilio to send alerts to mobile devices.
- **Customizable Check Intervals**: Allow users to set different check intervals for different URLs.
- **Error Handling and Resilience**: Improve error handling to manage network issues gracefully.

## License
This project is licensed under the MIT [License](https://github.com/Samuelson777/Web-Page-Monitor/blob/main/LICENSE) - see the LICENSE file for details.
