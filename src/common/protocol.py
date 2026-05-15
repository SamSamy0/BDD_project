from enum import Enum

from client.ClientNetworkManager import ClientNetworkManager


class Message(Enum):
    SIGNIN = "SIGNIN"
    SIGNUP = "SIGNUP"
    DISCONNECTION = "DISCONNECTION"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"
    # Store
    BUY = "BUY"
    GET_STORE = "GET_STORE"
    CHECK_ITEM = "CHECK_ITEM"
    # Profile
    GET_PROFILE = "GET_PROFILE"
    CHECK_RANKING = "CHECK_RANKING"
    # Course
    ADD_COURSE = "ADD_COURSE"
    DELETE_COURSE = "DELETE_COURSE"
    CHECK_COURSE = "CHECK_COURSE"
    GET_ALL_COURSES = "GET_ALL_COURSES"
    GET_RESUME_OF_COURSE = "GET_RESUME_OF_COURSE"
    # Resume
    ADD_RESUME = "ADD_RESUME"
    READ_RESUME = "READ_RESUME"
    EDIT_RESUME = "EDIT_RESUME"
    DELETE_RESUME = "DELETE_RESUME"
    ADD_EVAL = "ADD_EVAL"
    CHECK_EVALUATIONS = "CHECK_EVALUATIONS"


# Manager
mapping_actions = {
    Message.SIGNIN: ClientNetworkManager.signin,
    Message.SIGNUP: ClientNetworkManager.signup,
    Message.DISCONNECTION: ClientNetworkManager.disconnection,
}

# Handler
