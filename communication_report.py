import serial
import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime
import time

# Function to parse and clean the data received from Arduino
def parse_and_clean_data(data):
    # Assuming data is in the format: **ntu,Temp,Conductivity,phValue
    if data.startswith("**"):
        data = data[2:]
            
        parts = data.split(',')

        if len(parts) == 4:
            ntu = parts[0]
            temp = parts[1]
            conductivity = parts[2]
            ph_value = parts[3]

            return f"{datetime.now().isoformat()},{ntu},{temp},{conductivity},{ph_value}"
    
    return None

# Function to write data to CSV file
def write_to_csv(data):
    with open('sensor_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.split(','))

# Function to send email
def send_email(file_path):
    sender_email = "[FROM EMAIL]"
    receiver_email = "[TO EMAIL]"
    subject = "Sensor Data Report"
    body = "Hourly Sensor Data Report attached."

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with open(file_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name="sensor_data.csv")
        part['Content-Disposition'] = f'attachment; filename="sensor_data.csv"'
        message.attach(part)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, "[YOUR PASSWORD HERE]")  # Replace with your Gmail password
        server.sendmail(sender_email, receiver_email, message.as_string())

# Run forever listening to serial communication from Arduino:
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0',115200, timeout=1)
    ser.flush()

    next_email_time = time.time() + 60  # Schedule the first email after 1 hour
    
   
    while True:
        
        
        if ser.in_waiting > 0:
            print("Reading!")

            try:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
                cleaned_data = parse_and_clean_data(line)

            except Exception:
                print("OBS!")
                continue

            if cleaned_data:
                print(cleaned_data)
                write_to_csv(cleaned_data)

        # Check if it's time to send an email
        if time.time() >= next_email_time:
            send_email("sensor_data.csv")
            next_email_time = time.time() + 60  # Schedule the next email after 1 hour
            os.rename("sensor_data.csv", f"sensor_data_{datetime.now().isoformat().replace(':','-')}.csv")

        time.sleep(1)  # Add a short delay to avoid high CPU usage
