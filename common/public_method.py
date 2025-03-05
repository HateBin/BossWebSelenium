# -*- coding: utf-8 -*-
"""
@Time ： 2025/3/5 21:21
@Auth ： pengjianbin
@File ：public_method.py
"""
import settings


def assembly_fail_texts(texts: list):
    if not settings.IS_ACCEPT_HARDWARE:
        texts += settings.HARDWARE_TEXTS

    if not settings.IS_ACCEPT_BANKING_OR_FINANCE:
        texts += settings.BANKING_OR_FINANCE_TEXTS


def check_pass_text(text: str, check_type: str):
    or_pass_count = 0
    and_pass_count = 0
    if check_type == 'title':

        and_texts: list[str] = settings.PASS_TITLE_TEXTS['and']
        for andText in and_texts:
            if andText.lower() in text.lower():
                and_pass_count += 1
        if and_pass_count != len(and_texts):
            return {'state': False, 'texts': and_texts, 'type': 'and'}

        or_texts: list[str] = settings.PASS_TITLE_TEXTS['or']
        for orText in or_texts:
            if orText.lower() in text.lower():
                or_pass_count += 1

        if or_pass_count == 0:
            return {'state': False, 'texts': or_texts, 'type': 'or'}

        return {'state': True}
