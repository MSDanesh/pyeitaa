from ..rpc_error import RPCError


class NotAcceptable(RPCError):
    """Not Acceptable"""
    CODE = 406
    """``int``: RPC Error Code"""
    NAME = __doc__


class AuthKeyDuplicated(NotAcceptable):
    """The same authorization key (session file) was used in more than one place simultaneously. You must delete your session file and log in again with your phone number or bot token"""
    ID = "AUTH_KEY_DUPLICATED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilerefUpgradeNeeded(NotAcceptable):
    """The file reference has expired and you must use a refreshed one by obtaining the original media message"""
    ID = "FILEREF_UPGRADE_NEEDED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FreshChangeAdminsForbidden(NotAcceptable):
    """You were just elected admin, you can't add or modify other admins yet"""
    ID = "FRESH_CHANGE_ADMINS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FreshChangePhoneForbidden(NotAcceptable):
    """You can't change your phone number because your session was logged-in recently"""
    ID = "FRESH_CHANGE_PHONE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FreshResetAuthorisationForbidden(NotAcceptable):
    """You can't terminate other authorized sessions because the current was logged-in recently"""
    ID = "FRESH_RESET_AUTHORISATION_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneNumberInvalid(NotAcceptable):
    """The phone number is invalid"""
    ID = "PHONE_NUMBER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhonePasswordFlood(NotAcceptable):
    """You have tried to log-in too many times"""
    ID = "PHONE_PASSWORD_FLOOD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickersetInvalid(NotAcceptable):
    """The sticker set is invalid"""
    ID = "STICKERSET_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickersetOwnerAnonymous(NotAcceptable):
    """This sticker set can't be used as the group's sticker set because it was created by one of its anonymous admins"""
    ID = "STICKERSET_OWNER_ANONYMOUS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserpicUploadRequired(NotAcceptable):
    """You must have a profile picture to publish your geolocation"""
    ID = "USERPIC_UPLOAD_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserRestricted(NotAcceptable):
    """You are limited/restricted. You can't perform this action"""
    ID = "USER_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


