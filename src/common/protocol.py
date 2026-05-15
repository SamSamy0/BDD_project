
from enum import Enum

class Message(Enum):
    SIGNIN = "SIGNIN"
    SIGNUP = "SIGNUP"
    DISCONNECTION = "DISCONNECTION"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

#Manager
mapping_actions = {
    Message.SIGNIN: ClientNetworkManager.signin,
    Message.SIGNUP: ClientNetworkManager.signup,
    Message.DISCONNECTION: ClientNetworkManager.disconnection,
}

#Handler
