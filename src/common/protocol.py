from client.manager import Manager

from enum import Enum

class Message(Enum):
    SIGNIN = "SIGNIN"
    SIGNUP = "SIGNUP"
    DISCONNECTION = "DISCONNECTION"

#Manager
mapping_actions = {
    Message.SIGNIN: Manager.signin,
    Message.SIGNUP: Manager.signup,
    Message.DISCONNECTION: Manager.disconnection,
}

#Handler