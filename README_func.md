def get_peer_node(username): #function name is get_peer_node 
    username: This is the username that will show when I chat
    get_peer_node returns the value n, which appears to assign the username to my chat activity

def join_group(node, group): #function name is join_group
    node: My program's connection to the chat
    group: This is the peer chat group I wanted to join
    join_group does not return anything, it appears to connect my program to the chat

def chat_task(ctx, pipe, n, group): #function name is chat_task
    ctx: This is a ZeroMQ Connection Context
    pipe: This is a communications pipe polled by ZeroMQ for messages.
    n: This is the peer to peer node my chat app is connected as
    group: This is the peer chat group I wanted to join
    The chat_task method does not return anything, it appears to be the send/recieve manager.

def get_channel(node, group): #function name is get_channel
    node: My program's connection to the chat
    group: This is the peer chat group I wanted to join
    get_channel returns the value of the function zhelper.zthread_fork(ctx, chat_task, n=node, group=group)
    It looks like this is the channel that the group is assigned to