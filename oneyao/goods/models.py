from django.db import models


class CatalogIdItem(models.Model):
    name = models.CharField(max_length=16, null=True)
    catalogId = models.IntegerField(null=True)
    fatherId = models.IntegerField(null=True)

    class Meta:
        db_table = 'catalogId'


class CatalogIdItem_1(models.Model):
    name = models.CharField(max_length=16, null=True)
    catalogId = models.IntegerField(null=True)
    fatherId = models.IntegerField(null=True)

    class Meta:
        db_table = 'catalogId_1'


class CatalogIdItem_2(models.Model):
    name = models.CharField(max_length=16, null=True)
    catalogId = models.IntegerField(null=True)
    fatherId = models.IntegerField(null=True)
    icon_url = models.CharField(max_length=256, null=True)

    class Meta:
        db_table = 'catalogId_2'


class GoodsItem(models.Model):
    activity = models.CharField(max_length=16, null=True)
    activityDesc = models.CharField(max_length=128, null=True)
    attrLabels = models.CharField(max_length=8, null=True)
    boughtFlag = models.IntegerField(null=True)
    brandId = models.IntegerField(null=True)
    brandName = models.CharField(max_length=64, null=True)
    buyType = models.IntegerField(null=True)
    byName = models.CharField(max_length=8, null=True)
    comments = models.IntegerField(null=True)
    gift = models.CharField(max_length=512, null=True)
    goldMedalScore = models.IntegerField(null=True)
    goodsUserGrade = models.IntegerField(null=True)
    goodsUserGradeRate = models.CharField(max_length=64, null=True)
    groupId = models.IntegerField(null=True)
    goodsid = models.IntegerField(null=True)
    img = models.CharField(max_length=256, null=True)
    isGoldMedal = models.IntegerField(null=True)
    isHaiTao = models.IntegerField(null=True)
    itemId = models.CharField(max_length=16, null=True)
    marketPrice = models.IntegerField(null=True)
    materialtype = models.CharField(max_length=16, null=True)
    morePrice = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=128, null=True)
    norms = models.CharField(max_length=128, null=True)
    pcSalePrice = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    prescription = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    productNo = models.CharField(max_length=128, null=True)
    promotionTypes = models.CharField(max_length=8, null=True)
    saleType = models.IntegerField(null=True)
    salesCount = models.IntegerField(null=True)
    sellType = models.IntegerField(null=True)
    showPic = models.IntegerField(null=True)
    skuId = models.IntegerField(null=True)
    specialStatus = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    store = models.CharField(max_length=16, null=True)
    tcDefId = models.IntegerField(null=True)
    tcFlag = models.IntegerField(null=True)
    userGrade = models.IntegerField(null=True)
    venderId = models.CharField(max_length=64, null=True)
    venderName = models.CharField(max_length=128, null=True)
    venderType = models.IntegerField(null=True)
    fatherid = models.IntegerField(null=True)

    class Meta:
        db_table = 'goods'

class ProductItem(models.Model):
    productNo = models.CharField(max_length=128, null=True)
    mainimg5 = models.CharField(max_length=128, null=True)
    showPic = models.IntegerField(null=True)
    mainimg4 = models.CharField(max_length=128, null=True)
    mainimg3 = models.CharField(max_length=128, null=True)
    mainimg2 = models.CharField(max_length=128, null=True)
    approvalnum = models.CharField(max_length=64, null=True)
    mainimg6 = models.CharField(max_length=128, null=True)
    venderId = models.CharField(max_length=32, null=True)
    seriesIsMain = models.IntegerField(null=True)
    interceptCount = models.IntegerField(null=True)
    secondCatalogName = models.CharField(max_length=64, null=True)
    mainimg1 = models.CharField(max_length=128, null=True)
    brandId = models.IntegerField(null=True)
    brandName = models.CharField(max_length=64, null=True)
    recommendPrice = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    saleType = models.IntegerField(null=True)
    skuId = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    secondCatalogId = models.IntegerField(null=True)
    firstCatalogName = models.CharField(max_length=64, null=True)
    sellType = models.IntegerField(null=True)
    originalPrice = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    catalogId = models.IntegerField(null=True)
    gift = models.CharField(max_length=512, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    prescription = models.IntegerField(null=True)
    seriesDisplayMode = models.IntegerField(null=True)
    pcSalePrice = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    storeSchemeId = models.IntegerField(null=True)
    sellPoint = models.CharField(max_length=128, null=True)
    userGradecount = models.IntegerField(null=True)
    saleArea = models.IntegerField(null=True)
    h5GitLink = models.CharField(max_length=128, null=True)
    limitCount = models.IntegerField(null=True)
    giftLinkTxt = models.CharField(max_length=128, null=True)
    userGrade = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    materialtype = models.CharField(max_length=64, null=True)
    itemId = models.IntegerField(null=True)
    hasCombo = models.IntegerField(null=True)
    catalogName = models.CharField(max_length=32, null=True)
    seriesAttrs = models.CharField(max_length=128, null=True)
    areaItemId = models.IntegerField(null=True)
    specialStatus = models.IntegerField(null=True)
    drugLevel = models.IntegerField(null=True)
    frightTemplateId = models.IntegerField(null=True)
    firstCatalogId = models.IntegerField(null=True)
    isHaiTao = models.IntegerField(null=True)
    seriesId = models.IntegerField(null=True)
    productName = models.CharField(max_length=128, null=True)
    supplier = models.CharField(max_length=256, null=True)

    class Meta:
        db_table = 'product'