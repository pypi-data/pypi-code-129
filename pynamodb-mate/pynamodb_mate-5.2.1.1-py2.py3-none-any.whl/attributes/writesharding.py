# -*- coding: utf-8 -*-

import typing

from pynamodb.attributes import (
    UnicodeAttribute,
)

from pynamodb.models import Model

class WriteShardingHashKeyAttribute(UnicodeAttribute):
    high_cardinality_field = None
    _divider = "____"

    def serialize(self, value: bytes) -> str:
        fingerprint = sha256(value)
        s3_bucket = self.bucket_name
        s3_key = self.get_s3_key(fingerprint)
        s3_uri = join_s3_uri(s3_bucket, s3_key)
        if not is_s3_object_exists(self.s3_client, s3_bucket, s3_key):
            self.s3_client.put_object(
                Bucket=s3_bucket,
                Key=s3_key,
                Body=gzip.compress(value),
            )
        return s3_uri