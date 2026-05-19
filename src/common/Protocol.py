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
    # Summary
    ADD_SUMMARY = 21
    READ_SUMMARY = 22
    EDIT_SUMMARY = 23
    DELETE_SUMMARY = 24
    ADD_EVAL = 25
    CHECK_EVALUATIONS = 26  # Not sure
    READ_SUMMARIES = 34
    # Stats
    GET_LEADERBOARD = 27
    GET_COURSES_MOST_RESUMES = 28
    GET_RANKING_OBJECT = 29
    GET_RES_IN_AT_LEAST_THREE_COURSES = 30
    GET_RANKING_SPENDER = 31
    GET_BEST_TEN_USERS = 32
    GET_SUMMARY_AVERAGE = 33
