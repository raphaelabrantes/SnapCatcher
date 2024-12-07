#!.\venv\Scripts\python.exe
from cv2 import VideoCapture, imwrite, CAP_DSHOW, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT
import time
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.base import MIMEBase
from email import encoders

video_device = 0
FROM = "<SENDING_EMAIL>"
TO = "<RECIVING EMAIL>"
SUBJECT = "SnapCatcher: Someone log into your computer."
server_address = "<SMPT Server: depends on your provider>"
server_port = "<SMPT PORT>"
account_passowrd = "<SENDER EMAIL PASSOWRD>"

cam = VideoCapture(video_device)
if not cam.isOpened():
    print("Cannot open camera")
    exit()

result, image = cam.read()

if not result:
    print("Can't receive frame (stream end?). Exiting ...")
    exit()

imwrite("snap.png", image)

msg = MIMEMultipart()
msg['From'] = FROM
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = SUBJECT
part = MIMEBase("application", "octet-stream")
part.set_payload(open('snap.png', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="snap.png"')
msg.attach(part)
server = smtplib.SMTP(server_address, server_port)
server.starttls()
server.login(FROM, account_passowrd)
server.sendmail(FROM, TO, msg.as_string())
server.quit()
