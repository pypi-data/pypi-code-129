"""Misc utils to download chemRxiv dump"""
import json
import logging
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional

from requests.exceptions import SSLError
from requests.models import HTTPError
from tqdm import tqdm

from .chemrxiv_api import ChemrxivAPI

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

today = datetime.today().strftime("%Y-%m-%d")


def get_author(author_list: List[Dict]) -> str:
    """Parse ChemRxiv dump entry to extract author list

    Args:
        author_list (list): List of dicts, one per author.

    Returns:
        str: ;-concatenated author list.
    """

    return "; ".join(
        [" ".join([a["firstName"], a["lastName"]]) for a in author_list]
    )


def get_categories(category_list: List[Dict]) -> str:
    """Parse ChemRxiv dump entry to extract the categories of the paper

    Args:
        category_list (list): List of dicts, one per category.

    Returns:
        str: ;-concatenated category list.
    """

    return "; ".join([a["name"] for a in category_list])


def get_date(datestring: str) -> str:
    """Get the date of a chemrxiv dump enry.

    Args:
        date (str): String in the format: 2021-10-15T05:12:32.356Z

    Returns:
        str: Date in the format: YYYY-MM-DD.
    """
    return datestring.split("T")[0]


def get_metrics(metrics_list: List[Dict]) -> Dict:
    """
    Parse ChemRxiv dump entry to extract the access metrics of the paper.

    Args:
        metrics_list (List[Dict]): A list of single-keyed, dictionaries each
            containing key and value for exactly one metric.

    Returns:
        Dict: A flattened dictionary with all metrics and a timestamp
    """
    metric_dict = {m["description"]: m["value"] for m in metrics_list}

    # This assumes that the .jsonl is constructed at roughly the same date
    # where this entry was obtained from the API
    metric_dict.update({"timestamp": today})


def parse_dump(source_path: str, target_path: str) -> None:
    """
    Parses the dump as generated by the chemrXiv API and this repo:
    https://github.com/cthoyt/chemrxiv-summarize
    into a format that is equal to that of biorXiv and medRxiv.

    NOTE: This is a lazy parser trying to store all data in memory.

    Args:
        path (str): Path to the source dump
    """

    dump = []
    # Read source dump
    for file_name in tqdm(os.listdir(source_path)):

        if not file_name.endswith(".json"):
            continue
        filepath = os.path.join(source_path, file_name)
        with open(filepath, "r") as f:
            source_paper = json.load(f)

        target_paper = {
            "title": source_paper["title"],
            "doi": source_paper["doi"],
            "published_doi": (
                source_paper["vor"]["vorDoi"] if source_paper["vor"] else "N.A."
            ),
            "published_url": (
                source_paper["vor"]["url"] if source_paper["vor"] else "N.A."
            ),
            "authors": get_author(source_paper["authors"]),
            "abstract": source_paper["abstract"],
            "date": get_date(source_paper["statusDate"]),
            "journal": "chemRxiv",
            "categories": get_categories(source_paper["categories"]),
            "metrics": get_metrics(source_paper["metrics"]),
            "license": source_paper["license"]["name"],
        }
        dump.append(target_paper)
        os.remove(filepath)
    # Write dump
    with open(target_path, "w") as f:
        for idx, target_paper in enumerate(dump):
            if idx > 0:
                f.write(os.linesep)
            f.write(json.dumps(target_paper))
    logger.info("Done, shutting down")


def download_full(save_dir: str, api: Optional[ChemrxivAPI] = None) -> None:
    if api is None:
        api = ChemrxivAPI()

    os.makedirs(save_dir, exist_ok=True)
    for preprint in tqdm(api.all_preprints()):

        path = os.path.join(save_dir, f"{preprint['item']['id']}.json")
        if os.path.exists(path):
            continue
        preprint = preprint["item"]
        preprint_id = preprint["id"]
        try:
            preprint = api.preprint(preprint_id)
        except HTTPError:
            logger.warning(f"HTTP API Client error for ID: {preprint_id}")
        except SSLError:
            logger.warning(f'SSLError for ID: {preprint_id}')

        with open(path, "w") as file:
            json.dump(preprint, file, indent=2)
