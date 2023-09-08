"""Send a notification to a Telegram user or group.

E.g., send a notification triggered by some event in a monitoring system.
"""


__author__ = 'p4irin'
__email__ = '139928764+p4irin@users.noreply.github.com'
__version__ = '0.0.1'


import requests


class Notifier(object):
    """
    Sends notifications.

    Args:
        token: Telegram bot token
    """
    def __init__(self, token: str) -> None:
        self._base_url = f'https://api.telegram.org/bot{token}/'

    def send(self, notification: str, to_chat_id: str) -> requests.Response:
        """Send a text notification.
        
        Args:
            notification: Tell the recipient(s) what happened
            to_chat_id: Identifies a Telegram user or group

        Returns:
            requests.Response: Allow the caller access to and handling the
            response

        Raises:
            SystemExit: On all exceptions
        """
        data = {
            'chat_id': to_chat_id,
            'text': notification
        }
        try:
            r = requests.get(
                f'{self._base_url}sendMessage',
                data=data
            )
            r.raise_for_status()
            return r
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
