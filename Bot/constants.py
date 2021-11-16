
##################### Do not change those within this ###################################
import datetime
from MsgPack import MsgPack
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ZERO_TIME_DELTA = datetime.timedelta(0)
COMMAND_FORMAT = "`/timer {dd/mm/yyyy} {HH:MM} {Event Name}`"
##################### Do not change those within this ###################################


# Interval to edit the message
POLLING_INTERVAL = 2

# Format for Display
TIMER_FORMAT = "⏳{time}\n<i>**{event_name}**</i>"
EVENT_ENDED_FORMAT = "{event_name} has already ended :("
TIME_FORMAT = "{days} Days, {hours} Hours, {minutes} Minutes {seconds} Seconds left"

START_MSG = 'Welcome to the timer bot, feel free to look around'
HELP_MSG = f'To use the bot just type {COMMAND_FORMAT} and the bot will start to countdown to the given date and time.'
ERROR_MSG = 'This function is not implemented yet. Press back to go back.'
ERROR_CMD_MSG = f'Invalid format, the message is the format: {COMMAND_FORMAT}'


# Menu format (Change this if you know what you are doing)
# Call back 'help' -> MsgPack(helpmsg, help)
# Create your own buttons with `callback_name` `MsgPack(callback_name, callback_data)``

START = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('HELP ❓', callback_data="help")
        ],
    ]
)


HELP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Back ⬅️', callback_data="start")
        ],
    ]
)

ERROR = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Back ⬅️', callback_data="start")
        ],
    ]
)

CALLBACK_DICT = {
    'start': MsgPack(START_MSG, START),
    'help': MsgPack(HELP_MSG, HELP),
    'default': MsgPack(ERROR_MSG, ERROR),
}