# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from marshmallow import fields, INCLUDE

from azure.ai.ml._schema import PatchedSchemaMeta


class RetrySettingsSchema(metaclass=PatchedSchemaMeta):
    timeout = fields.Int()
    max_retries = fields.Int()
