#!/usr/bin/env python
# -*- coding: utf-8 -*-
import secrets


def get_secretkey():
    yield secrets.token_hex(16)


if __name__ == '__main__':
    print(secrets.token_hex(16))
    print(next(get_secretkey()))
