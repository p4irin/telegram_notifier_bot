import unittest
import os
from dotenv import load_dotenv
from telegram_notifier_bot import Notifier


load_dotenv()


class TestSendNotification(unittest.TestCase):
    """
    Send a notification to a Telegram user or group.
    """
    class _TestData:
            
        telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
        notification = "We're out of coffee! Please fix ASAP!"

    @classmethod
    def setUpClass(cls) -> None:
        cls._notifier = Notifier(cls._TestData.telegram_bot_token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test(self) -> None:
        response = self._notifier.send(
            self._TestData.notification,
            self._TestData.telegram_chat_id
        )
        self.assertTrue(response.status_code == 200)
