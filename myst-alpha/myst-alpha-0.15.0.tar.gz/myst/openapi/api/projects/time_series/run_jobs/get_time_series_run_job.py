from myst.client import Client
from myst.openapi.models.node_run_job_get import NodeRunJobGet


def request_sync(client: Client, project_uuid: str, time_series_uuid: str, uuid: str) -> NodeRunJobGet:
    """Get a run job for time series."""

    return client.request(
        method="get",
        path=f"/projects/{project_uuid}/time_series/{time_series_uuid}/run_jobs/{uuid}",
        response_class=NodeRunJobGet,
    )
