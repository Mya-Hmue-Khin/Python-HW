def send_messages(messages, sent_messages):
    while messages:
        sending_messages = messages.pop()
        print(f'sending "{sending_messages}"')
        sent_messages.append(sending_messages)


def show_sent_messages(sent_messages):
    print(f'The following texts have been sent.')
    for message in sent_messages:
        print(message)


messages = ['The quieter you become, the more you are able to hear.',
            'Order gives us comfort, but ambiguity gives us room to build.', 'We suffer more often in imagination than in reality.']
sent_messages = []

send_messages(messages[:], sent_messages)
show_sent_messages(sent_messages)
