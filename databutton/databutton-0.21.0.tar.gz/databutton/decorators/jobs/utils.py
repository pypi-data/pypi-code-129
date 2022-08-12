import datetime
import logging

import requests

from databutton.utils import get_auth_token, get_cached_databutton_config

FIRESTORE_BASE_URL = "https://firestore.googleapis.com/v1/projects/databutton/databases/(default)/documents"

logger = logging.getLogger("databutton.scheduler")


def create_job_run(job_id: str, run_id: str, start_time: str):
    try:
        project_id = get_cached_databutton_config().uid
        res = requests.post(
            f"{FIRESTORE_BASE_URL}/projects/{project_id}/runs",
            params={"documentId": run_id},
            headers={"Authorization": f"Bearer {get_auth_token()}"},
            json={
                "fields": {
                    "jobId": job_id,
                    "startTime": {"timestampValue": start_time},
                }
            },
        )
        if res.ok:
            data = res.json()
            return data
        else:
            logger.error("Could not create job run")
        return None
    except Exception:
        import traceback

        logger.error(traceback.format_exc())
        return None


def update_job_run(
    job_id: str, run_id: str, start_time: str, end_time: str, success: bool
):
    try:
        project_id = get_cached_databutton_config().uid
        start = datetime.datetime.utcfromtimestamp(start_time)
        end = datetime.datetime.utcfromtimestamp(end_time)
        durationMillis = int((end - start).microseconds() * 1000)
        fields = {
            "jobId": job_id,
            "startTime": {"timestampValue": start_time},
            "endTime": {"timestampValue": end_time},
            "duration": {"integerValue": durationMillis},
            "success": {"booleanValue": success},
        }
        res = requests.put(
            f"{FIRESTORE_BASE_URL}/projects/{project_id}/runs/{run_id}",
            headers={"Authorization": f"Bearer {get_auth_token()}"},
            json={
                "fields": fields,
            },
        )
        if res.ok:
            data = res.json()
            return data
        else:
            logger.error("Could not create job run")
        return None
    except Exception:
        import traceback

        logger.error(traceback.format_exc())
        return None


def iso_utc_timestamp_now() -> str:
    return datetime.datetime.utcnow().isoformat(timespec="milliseconds") + "Z"


def iso_utc_timestamp(dt: datetime.datetime) -> str:
    return dt.astimezone(datetime.timezone.utc).isoformat(timespec="milliseconds") + "Z"


def push_job_log(run_id: str, msg: bool):
    try:
        project_id = get_cached_databutton_config().uid
        res = requests.post(
            f"{FIRESTORE_BASE_URL}/projects/{project_id}/runs/{run_id}/logs",
            headers={"Authorization": f"Bearer {get_auth_token()}"},
            json={
                "fields": {
                    "startTime": {"timestampValue": iso_utc_timestamp_now()},
                    "msg": {"stringValue": msg},
                }
            },
        )
        if res.ok:
            data = res.json()
            return data
        else:
            logger.error(res.text, res.status_code)
        return None
    except Exception:
        import traceback

        logger.error(traceback.format_exc())
        return None
