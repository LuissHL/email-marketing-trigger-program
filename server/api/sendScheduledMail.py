import datetime as dt
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mailEditor import getTime,getRecipients,getBody,getSubject,getSegment

#agendamento em UTC
scheduled = getTime()
send_time = dt.datetime(scheduled[0], scheduled[1], scheduled[2], scheduled[3], scheduled[4], scheduled[5]) # set your sending time in UTC
try:
    time.sleep(send_time.timestamp() - time.time())
except:
    print("resuming sending")



server_smtp = "smtp.gmail.com"
port = 587
sender_email = "luiszzsoul@gmail.com"
password = "tfus diwe mdej rioe"
# precisa remover essa senha 
# Daqui e colocar em um arquivo separado por questão de segurança

#mensagem do email
receive_email = getRecipients()
subject = f"{getSubject()} test at {dt.datetime.now()} UTC"
body = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Teste</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f2f2f2;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f2f2f2;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff;">
                    <tr>
                        <td align="center" style="padding: 40px 0;">
                            <img src="https://img.freepik.com/fotos-gratis/paisagem-de-nevoeiro-matinal-e-montanhas-com-baloes-de-ar-quente-ao-nascer-do-sol_335224-794.jpg" alt="Paisagem" width="400" style="display: block; margin: 0 auto;">
                            <p style="margin-top: 20px; text-align: center;">Olá,</p>
                            <p style="text-align: center;">Este é um e-mail de teste com uma imagem anexada.</p>
                            <p style="text-align: center;">Agradecemos por ter recebido este e-mail de teste.</p>
                            <p style="text-align: center;">Este e-mail foi enviado apenas para fins de demonstração e teste.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
'''

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receive_email
message["Subject"] = subject
message.attach(MIMEText(body, "html"))

try:
 server = smtplib.SMTP(server_smtp, port)
 server.starttls()

 server.login(sender_email, password)
 server.sendmail(sender_email, receive_email, message.as_string())
 print("E-mail enviado com sucesso")
except Exception as e:
 print(f"Houve algum erro: {e}")
finally:
 server.quit()


