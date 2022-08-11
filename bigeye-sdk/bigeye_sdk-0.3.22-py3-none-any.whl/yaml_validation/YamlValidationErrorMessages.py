from bigeye_sdk.model.protobuf_enum_facade import SimplePredefinedMetricName

DUPLICATE_SAVED_METRIC_ID_EXISTS_ERRMSG = "Duplicate saved_metric_id exists: {saved_metric_id}"
SAVED_METRIC_ID_NOT_EXISTS_IN_SAVED_METRICS_DEFINITION_ERRMSG = \
    "Saved Metric ID does not exist in saved metric definitions: {saved_metric_id}"
DUPLICATE_TAG_EXISTS_ERRMSG = "Duplicate tag exists: {tag_id}"
TAG_ID_NOT_EXISTS_IN_TAG_DEFINITION_ERRMSG = "Tag ID {tag_id} does not exist in Tag Definitions."
FQ_COL_NOT_RESOLVES_TO_COLUMN_ERRMSG = "Fully qualified column selectors must resolve to a column.  Names " \
                                       "must have either 4 elements or 5 elements.  For example: " \
                                       "source.schema.table.column OR " \
                                       "source.database.schema.table.column.  Wild cards are accepted.  " \
                                       "The erroneous fully qualified name given is {fq_column_name}"
WILD_CARDS_NOT_SUPPORT_IN_FQ_TABLE_NAMES_ERRMSG = \
    "Wildcards are not supported in fully qualified table names: {fq_table_name}"
FQ_TABLE_NAME_MUST_RESOLVE_TO_TABLE_ERRMSG = "Fully qualified table names must resolve to a table.  Names " \
                                             "must have either 3 elements or 4 elements.  For example: " \
                                             "source.schema.table OR " \
                                             "source.database.schema.table.  " \
                                             "The erroneous fully qualified name given is {fq_table_name}"
SRC_NOT_EXISTS_FOR_DEPLOYMENT_ERRMSG = "Source does not exist for Deployment: {fq_name}"
FORMATTING_ERRMSG = "Invalid formatting: {s}"
OVERRIDE_METRIC_TYPE_SAVED_METRIC_ERRMSG = \
    "Cannot override the metric_type in a Saved Metric Definition: {config_error_lines}"
MUST_HAVE_METRIC_TYPE_ERRMSG = "Metric definitions must have a metric type if not referencing a saved metric by" \
                               "id: {config_error_lines}"
MUST_HAVE_METRIC_ID_ERRMSG = "Each Saved Metric Definition must contain a saved_metric_id.  " \
                             "Saved Metric: {config_error_lines}"
METRIC_TYPE_NOT_EXISTS_ERRMSG = "Metric does not exist: {metric}\n" \
                                f"Valid Metrics: {', '.join([e.value for e in SimplePredefinedMetricName])}"
INVALID_DECLARED_ATTRIBUTE_ERRMSG = "{cls_name} does not have an attribute {err_attrib}.  {possible_message}"
POSSIBLE_MATCH_ERRMSG = "Possible match {possible_matchs}."
NO_POSSIBLE_MATCH_ERRMSG = "No possible match was found."
