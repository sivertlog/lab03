import lab_chat as lc

def get_userinfo(message, to_upper=True):
    if to_upper:
        response=input(message).strip().upper()
    else:
        response = input(message).strip()
    return response

def get_username():
    username=get_userinfo("Type your username: ")
    return username

def get_group():
    groupname=get_userinfo("Type your group name: ")
    return groupname

def get_message():
    return get_userinfo("What is your message? ", False)

def initialize_chat():
    user=get_username()
    group=get_group()
    node=lc.get_peer_node(user)
    lc.join_group(node, group)
    channel=lc.get_channel(node, group)
    return channel

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

start_chat()
