#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=R1710,W0621,W0613,C0301

import logging
import pytest
import dnsmock

EXPECTED_VERSION = '0.0.3'


def test_version():
    assert dnsmock.VERSION == EXPECTED_VERSION
