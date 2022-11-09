#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, DictSchemaMixin, fields
from trytond.pyson import Eval
from trytond.pool import PoolMeta


class AssetAttributeSet(ModelSQL, ModelView):
    "Asset Attribute Set"
    __name__ = 'asset.attribute.set'
    name = fields.Char('Name', required=True, translate=True)
    attributes = fields.Many2Many('asset.attribute-asset.attribute-set',
        'attribute_set', 'attribute', 'Attributes')


class AssetAttribute(DictSchemaMixin, ModelSQL, ModelView):
    "Asset Attribute"
    __name__ = 'asset.attribute'
    sets = fields.Many2Many('asset.attribute-asset.attribute-set',
        'attribute', 'attribute_set', 'Sets')


class AssetAttributeAttributeSet(ModelSQL):
    "Asset Attribute - Set"
    __name__ = 'asset.attribute-asset.attribute-set'
    attribute = fields.Many2One('asset.attribute', 'Attribute',
        ondelete='CASCADE', required=True)
    attribute_set = fields.Many2One('asset.attribute.set', 'Set',
        ondelete='CASCADE', required=True)


class Asset(metaclass=PoolMeta):
    __name__ = 'asset'
    attribute_set = fields.Many2One('asset.attribute.set', 'Set')
    attributes = fields.Dict('asset.attribute', 'Attributes',
        domain=[
            ('sets', '=', Eval('attribute_set', -1)),
            ],
        depends=['attribute_set'],
        states={
            'readonly': ~Eval('attribute_set', {}),
            })
