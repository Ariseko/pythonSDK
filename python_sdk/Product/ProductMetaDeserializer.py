from ProductMeta import *
from python_sdk.entities.Meta import Meta

def SerializeProductMeta(rawProductMeta):
    #newProductMeta = ProductMeta()
    newProductMetaOrigin = Meta()

    newProductMetaOrigin.href = rawProductMeta.href
    newProductMetaOrigin.type = rawProductMeta.type
    newProductMetaOrigin.mediaType = rawProductMeta.mediaType
    newProductMetaOrigin.limit = rawProductMeta.limit
    newProductMetaOrigin.offset = rawProductMeta.offset
    newProductMetaOrigin.nextHref = rawProductMeta.nextHref
    newProductMetaOrigin.size = rawProductMeta.size

    return newProductMetaOrigin
