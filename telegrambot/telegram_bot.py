#!/usr/bin/env python
import importlib
import pprint
from functools import partial

import click
import telepot
import telepot.loop


bot = telepot.Bot(token='')

def handle(bot, trusted_chat_id, msg):
    """Processes all messages being received by the bot.

    :param msg: Incoming message received by the bot.
    :type msg: dict
    """
    pprint.pprint(msg)
    text = msg.get('text', '').strip()
    if text.startswith('/'):
        parts = text.split(' ', 1)
        command = parts[0]
        arguments = parts[1] if len(parts) == 2 else None
        tokens = command[1:].split('-')
        num_tokens = len(tokens)
        module_name = None
        function_name = None
        func = None
        module_name = tokens[0]
        if num_tokens <= 1:
            function_name = tokens[0]
        else:
            function_name = tokens[1]

        for cmd_path in ['telegrambot.commands', 'telegrambot.private_commands']:
            module_path = '{}.{}'.format(cmd_path, module_name)
            try:
                imported_module = importlib.import_module(module_path)
            except ModuleNotFoundError as error:
                print(error)
            else:
                func = getattr(imported_module, function_name)
            if func:
                break

        if func is None:
            bot.sendMessage(chat_id=msg['from'].get('id', ''), text='Unknown function')
        else:
            func(bot=bot, trusted_chat_id=trusted_chat_id, msg=msg, arguments=arguments)


@click.command()
@click.option('--token', required=True, help='Telegram authentication token for the bot.')
@click.option('--trusted-chat-id', default=None, help='Chat ID for messages that are from a trusted owner.')
def telegram_bot(token, trusted_chat_id):
    bot = telepot.Bot(token=token)
    telepot.loop.MessageLoop(bot=bot, handle=partial(handle, bot, trusted_chat_id)).run_forever()


if __name__ == '__main__':
    telegram_bot()
