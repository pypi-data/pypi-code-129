class TrackerChangelogEvents(enumerate):
    ISSUE_WORKFLOW = "IssueWorkflow"


class TrackerWorkflowTypes(enumerate):
    TRANSITION = "status"
    RESOLVE_ISSUE = "resolution"


class YandexTrackerLanguages(enumerate):
    RU = "ru"
    EN = "en"


class TimeDeltaOut(enumerate):
    SECONDS = "seconds"
    MINUTES = "minutes"

class ClickhouseProto(enumerate):
    HTTPS = "https"
    HTTP = "http"
