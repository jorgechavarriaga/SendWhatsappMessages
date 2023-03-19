import requests, os
from dotenv import load_dotenv
load_dotenv()

api_Key = os.environ.get('API_KEY')
phone_Number = os.environ.get('PHONE_NUMBER')


def whatsapp_send_message(msg):
        try:
                send = f"https://api.callmebot.com/whatsapp.php?phone={phone_Number}&text={msg}&apikey={api_Key}"
                print(send)
                r = requests.post(send)
                resp = r.content.decode("utf-8")
                fail = "Message not sent"
                if fail in resp: 
                        print(f"[+] Whatsapp Message Failed.")
                else:
                        print(f"[+] Whatsapp Message sent successfully to {phone_Number}.")
                return True
        except Exception as e:
                print(f"[-] Error: {e}")
                return False

# msg max 768 caracteres

msg = "Y, viéndole don Quijote de aquella manera, con muestras de tanta tristeza, le dijo: Sábete, Sancho, que no es un hombre más que otro si no hace más que otro. Todas estas borrascas que nos suceden son señales de que presto ha de serenar el tiempo y han de sucedernos bien las cosas; porque no es posible que el mal ni el bien sean durables, y de aquí se sigue que, habiendo durado mucho el mal, el bien está ya cerca. Así que, no debes congojarte por las desgracias que a mí me suceden, pues a ti no te cabe parte dellas. Y, viéndole don Quijote de aquella manera, con muestras de tanta tristeza, le dijo: Sábete, Sancho, que no es un hombre más que otro si no hace más que otro. Todas estas borrascas que nos suceden son señales de que presto ha de serenar el tiemp1234567890"
whatsapp_send_message(msg)
