from enum import Enum

# from client.ClientNetworkManager import ClientNetworkManager


class Protocol(Enum):
    SIGNIN = 1
    SIGNUP = 2
    DISCONNECTION = 3
    SUCCESS = 4
    ERROR = 5
    # Store
    BUY = 6
    GET_STORE = 7
    CHECK_ITEM = 8
    CHECK_TRANSACTION_HISTORY = 9
    CHANGE_STATE_OBJ = 10
    # Profile
    GET_PROFILE = 11
    GET_POINT = 12  # In case we want to just display the points
    CHECK_RANKING = 13
    # Course
    ADD_COURSE = 14
    DELETE_COURSE = 15
    CHECK_COURSE = 16
    GET_ALL_COURSES = 17
    GET_USER_COURSES = 18
    GET_RESUME_OF_COURSE = 19
    # Summary
    ADD_SUMMARY = 20
    READ_SUMMARY = 21
    EDIT_SUMMARY = 22
    DELETE_SUMMARY = 23
    ADD_EVAL = 24
    CHECK_EVALUATIONS = 25  # Not sure
    # Stats
    GET_LEADERBOARD = 26
    GET_COURSES_MOST_RESUMES = 27
    GET_RANKING_OBJECT = 28
    GET_RES_IN_AT_LEAST_THREE_COURSES = 29
    GET_RANKING_SPENDER = 30
    GET_BEST_TEN_USERS = 31
    GET_SUMMARY_AVERAGE = 32


