import logging
import platform

if platform.system() == "Windows":
    from SapGuiLibrary import SapGuiLibrary
else:
    SapGuiLibrary = object


class SAP(SapGuiLibrary):
    """RPA Framework library which is wrapping `SapGuiLibrary` functionality.
    """

    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)
        if platform.system() != "Windows":
            self.logger.warning("SAP requires Windows dependencies to work.")
            return
        SapGuiLibrary.__init__(self, *args, **kwargs)
