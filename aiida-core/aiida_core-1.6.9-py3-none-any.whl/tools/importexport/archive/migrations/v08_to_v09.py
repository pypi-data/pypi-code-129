# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida-core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
"""Migration from v0.8 to v0.9, used by `verdi export migrate` command.

The migration steps are named similarly to the database migrations for Django and SQLAlchemy.
In the description of each migration, a revision number is given, which refers to the Django migrations.
The individual Django database migrations may be found at:

    `aiida.backends.djsite.db.migrations.00XX_<migration-name>.py`

Where XX are the numbers in the migrations' documentation: REV. 1.0.XX
And migration-name is the name of the particular migration.
The individual SQLAlchemy database migrations may be found at:

    `aiida.backends.sqlalchemy.migrations.versions.<id>_<migration-name>.py`

Where id is a SQLA id and migration-name is the name of the particular migration.
"""
# pylint: disable=invalid-name
from aiida.tools.importexport.archive.common import CacheFolder

from .utils import verify_metadata_version, update_metadata


def migration_dbgroup_type_string(data):
    """Apply migration 0044 - REV. 1.0.44

    Rename the `type_string` columns of all `Group` instances.
    """
    mapping = {
        'user': 'core',
        'data.upf': 'core.upf',
        'auto.import': 'core.import',
        'auto.run': 'core.auto',
    }

    for attributes in data.get('export_data', {}).get('Group', {}).values():
        for old, new in mapping.items():
            if attributes['type_string'] == old:
                attributes['type_string'] = new


def migrate_v8_to_v9(folder: CacheFolder):
    """Migration of archive files from v0.8 to v0.9."""
    old_version = '0.8'
    new_version = '0.9'

    _, metadata = folder.load_json('metadata.json')

    verify_metadata_version(metadata, old_version)
    update_metadata(metadata, new_version)

    _, data = folder.load_json('data.json')

    # Apply migrations
    migration_dbgroup_type_string(data)

    folder.write_json('metadata.json', metadata)
    folder.write_json('data.json', data)
