#!/usr/bin/env python
# -*- coding: utf=8 -*-

import pickle
import os

import fortytwocli.const as const
import fortytwocli.exception as exception


def openFileToWrite(path, content):
    with open(path, 'wb') as fp:
        pickle.dump(content, fp)


def openFileToRead(path):
    with open(path, 'rb') as fp:
        return pickle.load(fp)


def getConfig():
    return openFileToRead(const.CONFIG_FILE)


def getCache():
    return openFileToRead(const.CACHE_FILE)


def checkConfigExists():
    if not os.path.exists(const.CONFIG_FILE):
        raise exception.NoConfigFoundError(const.MSG_NO_CONFIG_FOUND_ERROR)
