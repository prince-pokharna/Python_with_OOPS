
class EmailService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def _connect(self):
        print("Connecting to email server..")

    def _authenticate(self):
        print("Authenticating user.")

    def _disconnect(self):
        print("Disconnecting from email server.")

    def send_email(self, recipient, message):
        self._connect()
        self._authenticate()

        print(f"Sending email to {recipient}")
        print(f"Message: {message}")

        self._disconnect()


email = EmailService("max@gmail.com", "password123")

email.send_email(
    "alex@gmail.com",
    "Hello Alex, how r u?"
)
