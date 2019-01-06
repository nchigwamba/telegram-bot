def hello(bot, trusted_chat_id, msg):
    """
    Sends a greeting message in response to an incoming message.
    """
    params = {
        'first_name': msg['from'].get('first_name', ''),
        'last_name': msg['from'].get('last_name', ''),
        'chat_id': msg['from'].get('id', '')
    }
    text = 'Hello {first_name} {last_name}! Your chat ID is: {chat_id}'.format(**params)
    bot.sendMessage(chat_id=params['chat_id'], text=text)
