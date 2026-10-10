class CampusFlowError(Exception):
    """Base class for all expected CampusFlow errors."""


class ValidationError(CampusFlowError):
    """Input is malformed or not allowed."""


class TicketNotFoundError(CampusFlowError):
    """No ticket exists with that ID."""


class InvalidTransitionError(CampusFlowError):
    """A status change or modification is not allowed."""


class StorageError(CampusFlowError):
    """The JSON file could not be read or written safely."""