#
# This file is part of the PyRDP project.
# Copyright (C) 2018 GoSecure Inc.
# Licensed under the GPLv3 or later.
#

from enum import IntEnum


class DeviceRedirectionComponent(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc241324.aspx
    """
    RDPDR_CTYP_CORE = 0x4472
    RDPDR_CTYP_PRN = 0x5052


class DeviceRedirectionPacketID(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc241324.aspx
    """
    PAKID_CORE_SERVER_ANNOUNCE = 0x496E
    PAKID_CORE_CLIENTID_CONFIRM = 0x4343
    PAKID_CORE_CLIENT_NAME = 0x434E
    PAKID_CORE_DEVICELIST_ANNOUNCE = 0x4441
    PAKID_CORE_DEVICE_REPLY = 0x6472
    PAKID_CORE_DEVICE_IOREQUEST = 0x4952
    PAKID_CORE_DEVICE_IOCOMPLETION = 0x4943
    PAKID_CORE_SERVER_CAPABILITY = 0x5350
    PAKID_CORE_CLIENT_CAPABILITY = 0x4350
    PAKID_CORE_DEVICELIST_REMOVE = 0x444D
    PAKID_PRN_CACHE_DATA = 0x5043
    PAKID_CORE_USER_LOGGEDON = 0x554C
    PAKID_PRN_USING_XPS = 0x5543


class MajorFunction(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc241327.aspx
    """

    IRP_MJ_CREATE = 0x00000000
    IRP_MJ_CLOSE = 0x00000002
    IRP_MJ_READ = 0x00000003
    IRP_MJ_WRITE = 0x00000004
    IRP_MJ_DEVICE_CONTROL = 0x0000000E
    IRP_MJ_QUERY_VOLUME_INFORMATION = 0x0000000A
    IRP_MJ_SET_VOLUME_INFORMATION = 0x0000000B
    IRP_MJ_QUERY_INFORMATION = 0x00000005
    IRP_MJ_SET_INFORMATION = 0x00000006
    IRP_MJ_DIRECTORY_CONTROL = 0x0000000C
    IRP_MJ_LOCK_CONTROL = 0x00000011


class MinorFunction(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc241327.aspx
    """
    IRP_MN_QUERY_DIRECTORY = 0x00000001
    IRP_MN_NOTIFY_CHANGE_DIRECTORY = 0x00000002


class IOOperationSeverity(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc231200.aspx
    """
    STATUS_SEVERITY_SUCCESS = 0x0
    STATUS_SEVERITY_INFORMATIONAL = 0x1
    STATUS_SEVERITY_WARNING = 0x2
    STATUS_SEVERITY_ERROR = 0x3


class FileAccess(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc246802.aspx
    """

    FILE_READ_DATA = 0x00000001
    FILE_WRITE_DATA = 0x00000002
    FILE_APPEND_DATA = 0x00000004
    FILE_READ_EA = 0x00000008
    FILE_WRITE_EA = 0x00000010
    FILE_DELETE_CHILD = 0x00000040
    FILE_EXECUTE = 0x00000020
    FILE_READ_ATTRIBUTES = 0x00000080
    FILE_WRITE_ATTRIBUTES = 0x00000100
    DELETE = 0x00010000
    READ_CONTROL = 0x00020000
    WRITE_DAC = 0x00040000
    WRITE_OWNER = 0x00080000
    SYNCHRONIZE = 0x00100000
    ACCESS_SYSTEM_SECURITY = 0x01000000
    MAXIMUM_ALLOWED = 0x02000000
    GENERIC_ALL = 0x10000000
    GENERIC_EXECUTE = 0x20000000
    GENERIC_WRITE = 0x40000000
    GENERIC_READ = 0x80000000


class CreateOption(IntEnum):
    FILE_DIRECTORY_FILE = 0x00000001
    FILE_WRITE_THROUGH = 0x00000002
    FILE_SEQUENTIAL_ONLY = 0x00000004
    FILE_NO_INTERMEDIATE_BUFFERING = 0x00000008
    FILE_SYNCHRONOUS_IO_ALERT = 0x00000010
    FILE_SYNCHRONOUS_IO_NONALERT = 0x00000020
    FILE_NON_DIRECTORY_FILE = 0x00000040
    FILE_COMPLETE_IF_OPLOCKED = 0x00000100
    FILE_NO_EA_KNOWLEDGE = 0x00000200
    FILE_RANDOM_ACCESS = 0x00000800
    FILE_DELETE_ON_CLOSE = 0x00001000
    FILE_OPEN_BY_FILE_ID = 0x00002000
    FILE_OPEN_FOR_BACKUP_INTENT = 0x00004000
    FILE_NO_COMPRESSION = 0x00008000
    FILE_OPEN_REMOTE_INSTANCE = 0x00000400
    FILE_OPEN_REQUIRING_OPLOCK = 0x00010000
    FILE_DISALLOW_EXCLUSIVE = 0x00020000
    FILE_RESERVE_OPFILTER = 0x00100000
    FILE_OPEN_REPARSE_POINT = 0x00200000
    FILE_OPEN_NO_RECALL = 0x00400000
    FILE_OPEN_FOR_FREE_SPACE_QUERY = 0x00800000


class DeviceType(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc241326.aspx
    """

    RDPDR_DTYP_SERIAL = 0x00000001
    RDPDR_DTYP_PARALLEL = 0x00000002
    RDPDR_DTYP_PRINT = 0x00000004
    RDPDR_DTYP_FILESYSTEM = 0x00000008
    RDPDR_DTYP_SMARTCARD = 0x00000020

    @staticmethod
    def getPrettyName(deviceType: 'DeviceType'):
        if deviceType == DeviceType.RDPDR_DTYP_FILESYSTEM:
            return "Filesystem"
        elif deviceType == DeviceType.RDPDR_DTYP_SMARTCARD:
            return "Smart card"
        elif deviceType == DeviceType.RDPDR_DTYP_PRINT:
            return "Printer"
        elif deviceType == DeviceType.RDPDR_DTYP_PARALLEL:
            return "Parallel port"
        elif deviceType == DeviceType.RDPDR_DTYP_SERIAL:
            return "Serial port"
        else:
            return str(deviceType)


class RDPDRCapabilityType(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc241325.aspx
    """
    CAP_GENERAL_TYPE = 0x0001
    CAP_PRINTER_TYPE = 0x0002
    CAP_PORT_TYPE = 0x0003
    CAP_DRIVE_TYPE = 0x0004
    CAP_SMARTCARD_TYPE = 0x0005


class GeneralCapabilityVersion(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc241349.aspx
    """
    GENERAL_CAPABILITY_VERSION_01 = 0x00000001
    GENERAL_CAPABILITY_VERSION_02 = 0x00000002


class ExtendedPDUFlags(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc241349.aspx
    """
    RDPDR_DEVICE_REMOVE_PDUS = 0x00000001
    RDPDR_CLIENT_DISPLAY_NAME_PDU = 0x00000002
    RDPDR_USER_LOGGEDON_PDU = 0x00000004
