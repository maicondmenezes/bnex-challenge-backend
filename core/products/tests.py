from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Product


class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin', email='admin@admin.com'
        )
        token, created = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.product = Product.objects.create(
            name='Test Product', description='Test Description', value='99.99'
        )
        self.product_url = reverse(
            'product-detail', kwargs={'pk': self.product.pk}
        )

    def tearDown(self):
        self.user.delete()
        super().tearDown()

    def test_create_product(self):
        """
        Ensure we can create a new product.
        """
        url = reverse('product-list')
        data = {
            'name': 'New Product',
            'description': 'New Description',
            'value': '59.99',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(
            Product.objects.get(id=response.data['id']).name, 'New Product'
        )

    def test_get_products_list(self):
        """
        Ensure we can retrieve a list of products.
        """
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_single_product(self):
        """
        Ensure we can retrieve a single product by id.
        """
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)

    def test_update_product(self):
        """
        Ensure we can update an existing product.
        """
        data = {
            'name': 'Updated Name',
            'description': 'Updated Description',
            'value': '79.99',
        }
        response = self.client.put(self.product_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Name')

    def test_partial_update_product(self):
        """
        Ensure we can partially update an existing product.
        """
        data = {'name': 'Partially Updated Name'}
        response = self.client.patch(self.product_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Partially Updated Name')

    def test_delete_product(self):
        """
        Ensure we can delete a product.
        """
        response = self.client.delete(self.product_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
