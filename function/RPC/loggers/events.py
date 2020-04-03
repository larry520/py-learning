NO_EVENT = -1
SEQUENCE_START = 0
SEQUENCE_END = 1
ITEM_START = 2
ITEM_FINISH = 3
ATTRIBUTE_FOUND = 4
REPORT_ERROR_OCCURRED = 5
UOP_DETECTED = 6
SEQUENCE_LOADED = 7
SFR_STEP_RESULT = 8
SFR_END_RESULT = 9
ROBOT_POS_INFO = 10
SYS_STATE = 11
VISION_ERROR = 12
MOTION_ERROR = 13
WORK_LOG = 14
SYS_LOG = 15
PATH_LINE_NUM = 16
IO_STATUS = 17
INFO_STATUS=18

def get_name(event_type):
    if event_type == NO_EVENT:
        return 'NO_EVENT'
    elif event_type == SEQUENCE_START:
        return 'SEQUENCE_START'
    elif event_type == SEQUENCE_END:
        return 'SEQUENCE_END'
    elif event_type == ITEM_START:
        return 'ITEM_START'
    elif event_type == ITEM_FINISH:
        return 'ITEM_FINISH'
    elif event_type == ATTRIBUTE_FOUND:
        return 'ATTRIBUTE_FOUND'
    elif event_type == REPORT_ERROR_OCCURRED:
        return 'REPORT_ERROR_OCCURRED'
    elif event_type == UOP_DETECTED:
        return 'UOP_DETECTED'
    elif event_type == SEQUENCE_LOADED:
        return 'SEQUENCE_LOADED'
    elif event_type == SFR_STEP_RESULT:
        return 'SFR_STEP_RESULT'
    elif event_type == SFR_END_RESULT:
        return 'SFR_END_RESULT'
    elif event_type == ROBOT_POS_INFO:
        return  'ROBOT_POS_INFO'
    elif event_type == SYS_STATE:
        return 'SYS_STATE'
    elif event_type == VISION_ERROR:
        return "VISION_ERROR"
    elif event_type == MOTION_ERROR:
        return "MOTION_ERROR"
    elif event_type == WORK_LOG:
        return "WORK_LOG"
    elif event_type == SYS_LOG:
        return "SYS_LOG"
    elif event_type == PATH_LINE_NUM:
        return "PATH_LINE_NUM"
    elif event_type == IO_STATUS:
        return "IO_STATUS"
    elif event_type == INFO_STATUS:
        return "INFO_STATUS"
    else:
        return 'UNKNOWN event type: ' + str(event_type)
