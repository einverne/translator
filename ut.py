#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from translator import *


class TestTranslator(unittest.TestCase):

    ZH = '网站还提供书影音推荐、线下同城活动、小组话题交流等多种服务功能.'
    EN = 'The Verge is an American technology news and media network operated by Vox Media.'
    KO = '네이버 메인에서 다양한 정보와 유용한 컨텐츠를 만나 보세요.'
    JP = 'YouTubeは、アメリカ合衆国・カリフォルニア州サンブルーノに本社を置く世界最大の動画共有サービス。Youは「あなた」、Tubeは「ブラウン管」という意味である。'

    def test_google(self):
        gt = GoogleTranslator()
        # r = gt.translate('auto', 'auto', 'Hello, World !!')
        # r = gt.translate('auto', 'auto', '你吃饭了没有?')
        # r = gt.translate('auto', 'auto', '长')
        # r = gt.translate('auto', 'auto', 'long')
        # r = gt.translate('auto', 'auto', 'kiss')
        # r = gt.translate('auto', 'auto', '亲吻')
        import pprint
        # print(r['translation'])
        r = gt.translate('auto', 'auto', TestTranslator.JP)
        print(r['translation'])
        # pprint.pprint(r['info'])
        return 0

    def test_youdao(self):
        y = YoudaoTranslator()
        r = y.translate("AUTO", "AUTO", TestTranslator.EN)
        print(r['translation'])

    def test_yandex(self):
        y = YandexTranslator()
        # EN auto to ZH
        r = y.translate('auto', 'auto', TestTranslator.EN)
        print(r['translation'])
        # ZH auto to EN
        r = y.translate('auto', 'auto', TestTranslator.ZH)
        print(r['translation'])
        # specific KO to ZH
        r = y.translate('ko', 'zh', TestTranslator.KO)
        print(r['translation'])
        r = y.translate('auto', 'zh', TestTranslator.JP)
        print(r['translation'])


if __name__ == '__main__':
    unittest.main()