import multiprocessing
import requests
from smtplib import SMTP
from email.mime.text import MIMEText

SMTP_SERVER_ADDRESS = 'localhost'

def send_alert_mail(from_addr, to_addr, subject, message):
    """send email"""
    mesg = MIMEText(message)
    mesg['From'] = from_addr
    mesg['To'] = to_addr
    mesg['Subject'] = subject

    smtp = SMTP(SMTP_SERVER_ADDRESS)
    smtp.sendmail(from_addr, to_addr, mesg.as_string())
    smtp.close()


def web_crawler(q):
    """child process"""
    try:
        p_name = multiprocessing.current_process().name
        url = q.get()
        response = requests.get(url)
        print(f'{p_name}: {url}: {response.content[:128]}')
    except requests.exceptions.ConnectionError as error:
        subject= f'{p_name}: {url}: failed http request'
        send_alert_mail('ravijaya@localhost', 'training@localhost', subject, str(error))
        # print(error)


def main():
    urls = ['http://linux.org',
            'http://python.org',
            'http://kernel.org',
            'http://golang.org',
            'httP://perllang.org']

    queue = multiprocessing.Queue()  # empty

    for url in urls:
        multiprocessing.Process(target=web_crawler, args=[queue]).start()
        queue.put(url)

    for child in multiprocessing.active_children():
        child.join()


if __name__ == '__main__':
    main()
