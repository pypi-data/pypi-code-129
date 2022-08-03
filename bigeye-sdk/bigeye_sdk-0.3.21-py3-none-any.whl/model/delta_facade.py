from __future__ import annotations

from typing import List, Optional

from pydantic import Field
from pydantic_yaml import YamlModel

from bigeye_sdk.exceptions.exceptions import InvalidConfigurationException
from bigeye_sdk.functions.helpers import has_either_ids_or_names
from bigeye_sdk.model.protobuf_message_facade import SimpleNamedSchedule, SimpleColumnMapping, SimpleColumnPair, \
    SimpleMetricType
from bigeye_sdk.serializable import File
from bigeye_sdk.model.protobuf_enum_facade import SimplePredefinedMetricName


class SimpleDeltaConfiguration(YamlModel):
    """
    The Simple Delta Configuration is a Yaml serializable configuration file used to configure and version deltas in as
    a file.  The CLI and SDK client methods accept Simple Delta Configurations either individually or as lists -- see
    SimpleDeltaConfigurationList.

    Attributes:
        delta_id: The system generated Delta ID
        delta_name: The user configurable name of the delta.
        source_table_id: The system generated source table ID.  Either include the ID or the fully qualified name.
        fq_source_table_name: The fully qualified source table name.  Either include theID or the fully qualified name.
        target_table_id: The system generated source table ID.  Either include the ID or the fully qualified name.
        fq_target_table_name: The fully qualified source table name.  Either include theID or the fully qualified name.
        delta_column_mapping: A column mapping, including list of metrics, conforming to the SimpleColumnMapping class.
        all_column_metrics: A list of metrics that will be applied to all columns in the Delta.
        group_bys: A list of group bys conforming to the SimpleColumnPair class
        source_filters: A list of string filters to apply to the source table.
        target_filters: A list of stirng filters to apply to the target table.
        cron_schedule: A cron schedule conforming to the SimpleNamedSchedule class.

    """

    delta_name: str
    delta_id: Optional[int] = None
    source_table_id: Optional[int] = None
    fq_source_table_name: Optional[str] = None
    target_table_id: Optional[int] = None
    fq_target_table_name: Optional[str] = None
    delta_column_mapping: Optional[List[SimpleColumnMapping]] = Field(default_factory=lambda: [])
    all_column_metrics: Optional[List[SimpleMetricType]] = Field(default_factory=lambda: [])
    group_bys: Optional[List[SimpleColumnPair]] = Field(default_factory=lambda: [])
    source_filters: Optional[List[str]] = Field(default_factory=lambda: [])
    target_filters: Optional[List[str]] = Field(default_factory=lambda: [])
    cron_schedule: SimpleNamedSchedule = None

    def __post_init__(self):
        if not has_either_ids_or_names(self.source_table_id, self.fq_source_table_name) \
                or not has_either_ids_or_names(self.target_table_id, self.fq_target_table_name):
            raise InvalidConfigurationException(
                f'Delta name: {self.delta_name} Must include either a fully qualified table name or '
                f'id for both source and target.')


class SimpleDeltaConfigurationFile(File, type='DELTA_CONFIGURATION_FILE'):
    deltas: List[SimpleDeltaConfiguration]
