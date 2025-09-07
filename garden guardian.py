from engi1020.arduino.api import *
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# 
# def send_sms_via_gmail(phone_number, message):
# 
#     sender_email = "burner1234357567@gmail.com"
#     sender_password = "asbi glye bpqr xhqj"
# 
#     recipient_sms_email = f"{phone_number}@msg.telus.com"
# 
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = recipient_sms_email
#     msg['Subject'] = ""
#     msg.attach(MIMEText(message, 'plain'))
# 
#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, recipient_sms_email, msg.as_string())
#         server.quit()
#         print(f"SMS sent to {phone_number} via {recipient_sms_email}")
#     except Exception as e:
#         print(f"Failed to send SMS: {e}")
# 
# def check_temperature():
#     temp = pressure_get_temp()
#     if temp > 27 or temp < 0:
#         send_sms_via_gmail("7092228154", "check temp in the plantssssssssssss!!!!!!")
#     return temp
# 
# def check_distance():
#     dist = ultra_get_centimeters(2)
#     if dist < 3:
#         send_sms_via_gmail("7092228154", "something blocking the motion sesnor !!!!!!")
#     return dist
# 
# def check_motion():
#     is_motion = digital_read(4)
#     if is_motion:
#         send_sms_via_gmail("7092228154", "movement in the plantssssssssssss!!!!!!") 
#     if is_motion:
#         buzzer_frequency(5, 5000)
#     else:
#         buzzer_stop(5)
#     return is_motion
# 
# def light_check():
#     light = analog_read(6)
#     if light < 30:
#         send_sms_via_gmail("7092228154", "no light in the plantssssssssssss!!!!!!")
#     return light
# 
# oled_clear()
# oled_print("plants are the best G")
while True:
    for angle in range(0, 180, 15):
        servo_set_angle(3, angle)
        print("light:", light_check())
        print("temp:", check_temperature(), "c")
        print("Distance:", check_distance(), "cm")
        print("is there motion? ", check_motion())
        time.sleep(0.04)




