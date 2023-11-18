import time
import socket
import os

def generate_log_samples(num_samples):
    logs = []
    for i in range(1, num_samples + 1):
        log = input(f"Enter log sample {i}: ")
        logs.append(log)
    return logs

def get_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def send_to_file(logs, eps):
    print("Sending logs to file. Press 'Ctrl+C' to stop.")
    try:
        while True:
            for log in logs:
                timestamped_log = f"{log} - {get_timestamp()}"
                with open("Logs.log", "a") as f:
                    f.write(timestamped_log + "\n")
                time.sleep(1 / eps)
    except KeyboardInterrupt:
        print("\nLog sending stopped.")

def send_to_syslog(logs, eps, syslog_server_ip, syslog_server_port):
    print("Sending logs to syslog. Press 'Ctrl+C' to stop.")
    syslog_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        while True:
            for log in logs:
                timestamped_log = f"{log} - {get_timestamp()}"
                syslog_socket.sendto(timestamped_log.encode(), (syslog_server_ip, syslog_server_port))
                time.sleep(1 / eps)
    except KeyboardInterrupt:
        print("\nLog sending stopped.")

def main():
    print("Log Sender Script")

    try:
        print("Choose the number of log samples:")
        print("1. One log sample")
        print("2. Two log samples")
        print("3. Three log samples")
        print("4. Four log samples")
        print("5. Five log samples")

        num_samples_choice = input("Enter the number of your choice: ")

        num_samples_options = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
        }

        num_samples = num_samples_options.get(num_samples_choice)

        if num_samples is None:
            print("Invalid choice. Please enter a number between 1 and 5.")
            return

        logs = generate_log_samples(num_samples)

        eps = float(input("Enter the desired EPS(events per second)(input integer): "))

        print("Choose the method to send logs:")
        print("1. File")
        print("2. Syslog")

        method_choice = input("Enter the number of your choice: ")

        if method_choice == "1":
            send_to_file(logs, eps)
        elif method_choice == "2":
            syslog_server_ip = input("Enter syslog server IP: ")
            syslog_server_port = int(input("Enter syslog server port: "))
            send_to_syslog(logs, eps, syslog_server_ip, syslog_server_port)
        else:
            print("Invalid choice. Please enter '1' for File or '2' for Syslog.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
