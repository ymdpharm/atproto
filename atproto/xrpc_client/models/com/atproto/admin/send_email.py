##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


import typing as t
from dataclasses import dataclass

from atproto.xrpc_client.models import base


@dataclass
class Data(base.DataModelBase):

    """Input data model for :obj:`com.atproto.admin.sendEmail`."""

    content: str  #: Content.
    recipientDid: str  #: Recipient did.
    subject: t.Optional[str] = None  #: Subject.


@dataclass
class Response(base.ResponseModelBase):

    """Output data model for :obj:`com.atproto.admin.sendEmail`."""

    sent: bool  #: Sent.
