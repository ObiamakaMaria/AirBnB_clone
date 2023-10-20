#!/usr/bin/python3

from datetime import datetime
import models


def save(self):
    """ update the public instance attribute update_at """
    self.updated_at = datetime.now()
    models.storage.save()
