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
    GET_USER_OBJECT = 14
    # Course
    ADD_COURSE = 15
    DELETE_COURSE = 16
    CHECK_COURSE = 17
    GET_ALL_COURSES = 18
    GET_USER_COURSES = 19
    GET_RESUME_OF_COURSE = 20

    ADD_USER_COURSE = 21

    # Summary
    ADD_SUMMARY = 22
    READ_SUMMARY = 23
    EDIT_SUMMARY = 24
    DELETE_SUMMARY = 25
    ADD_EVAL = 26
    CHECK_EVALUATIONS = 27  # Not sure
    READ_SUMMARIES = 35
    # Stats
    GET_LEADERBOARD = 28
    GET_COURSES_MOST_RESUMES = 29
    GET_RANKING_OBJECT = 30
    GET_RES_IN_AT_LEAST_THREE_COURSES = 31
    GET_RANKING_SPENDER = 32
    GET_BEST_TEN_USERS = 33
    GET_SUMMARY_AVERAGE = 34
