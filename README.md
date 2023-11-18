# Log-generator-EPS-tester

Overview

for test the SIEM(Security Information and Event Management) input log capacity this Python script has been developed. this script replicate the creation and transmission of logs to a SIEM system or any other syslog server. You can enter log samples, pick the required EPS (events per second), and decide whether to transmit logs to a file or a syslog server using the script.

features:

Interactive Setup: You can enter log samples, specify EPS, and select the log shipping method as the script walks you through the setup process.

File or Syslog: Logs can be sent to a remote Syslog server or a locally stored in a file.

Timestamps: A timestamp that shows the log's generation date is included with every entry.

Application To initiate the script, type python log_sender.py into the terminal.

When prompted, enter the necessary data:

Quantity of sample logs. the actual log samples. The desired events per second, or EPS. Select whether to transmit logs to a syslog server or a file. then inter information about syslog server ip and port. if you choose file, a logs.log file created in the scripts directory. Logs will be sent by the script based on your configuration.

Requirements Python 3.x

Usage Run the script by executing python Log-generator-EPS-tester.py in your terminal.

Enter the required information when prompted: varitety of log samples. Log samples. Desired EPS (events per second). Choose between sending logs to a file or a syslog server.

The script will start sending logs based on your configuration.

To stop log generation, press 'Ctrl+C'.
