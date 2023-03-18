from odoo.tests.common import SavepointCase

class MaterialTest(SavepointCase):

    def setUp(self):
        super(MaterialTest, self).setUp()
        self.material_model = self.env['material.product']
    
    def test_create_material(self):
        data = self.material_model.create({
            'name' : 'testing 1',
            'code' : '001',
            'material_type' : 'fabric',
            'material_buy_price' : 90,     
         })
        message = "Price can\'t under 100"
          
        # assert function() to check if values1 is 
        # greater than value2
        self.assertGreater(data.material_buy_price, 100, message)
        self.assertEqual(data.name, 'testing 1')
        self.assertEqual(data.code, '001')
        self.assertEqual(data.material_type, 'fabric')
        self.assertEqual(data.material_buy_price, 100)


