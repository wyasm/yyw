from django.db import models


class Goods(models.Model):
    goods_name = models.CharField(max_length=128)
    goods_price = models.CharField(max_length=16)
    goods_effect = models.CharField(max_length=256)
    goods_source = models.CharField(max_length=32)
    ratify_number = models.CharField(max_length=128)
    sale_mode = models.PositiveIntegerField()
    goods_explain = models.CharField(max_length=64)
    goods_image = models.CharField(max_length=1028)
    goods_judge_number = models.CharField(max_length=16)
    goods_detail_image = models.CharField(max_length=2056)
    # goods_detail_table = models