LOG_FORMAT = '[STATAM-REPORT] '


class Logger:
    """
    Logging utils class.
    """

    @staticmethod
    def enable(enable):
        """
        Enable/Disable logger.
        :param enable: True to enable, False to disable
        """
        Logger.ENABLED = enable

    @staticmethod
    def log(msg, spaceBefore=False, spaceAfter=False):
        """
        Log the message if the logger is enabled.
        :param msg: message to log
        """
        if not Logger.ENABLED: return

        if spaceBefore: print('\n')
        print(LOG_FORMAT + msg)
        if spaceAfter: print('\n')


Logger.ENABLED = False
