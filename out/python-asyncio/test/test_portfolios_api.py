# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from asana_asyncio.api.portfolios_api import PortfoliosApi


class TestPortfoliosApi(unittest.TestCase):
    """PortfoliosApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PortfoliosApi()

    def tearDown(self) -> None:
        pass

    def test_add_custom_field_setting_for_portfolio(self) -> None:
        """Test case for add_custom_field_setting_for_portfolio

        Add a custom field to a portfolio
        """
        pass

    def test_add_item_for_portfolio(self) -> None:
        """Test case for add_item_for_portfolio

        Add a portfolio item
        """
        pass

    def test_add_members_for_portfolio(self) -> None:
        """Test case for add_members_for_portfolio

        Add users to a portfolio
        """
        pass

    def test_create_portfolio(self) -> None:
        """Test case for create_portfolio

        Create a portfolio
        """
        pass

    def test_delete_portfolio(self) -> None:
        """Test case for delete_portfolio

        Delete a portfolio
        """
        pass

    def test_get_items_for_portfolio(self) -> None:
        """Test case for get_items_for_portfolio

        Get portfolio items
        """
        pass

    def test_get_portfolio(self) -> None:
        """Test case for get_portfolio

        Get a portfolio
        """
        pass

    def test_get_portfolios(self) -> None:
        """Test case for get_portfolios

        Get multiple portfolios
        """
        pass

    def test_remove_custom_field_setting_for_portfolio(self) -> None:
        """Test case for remove_custom_field_setting_for_portfolio

        Remove a custom field from a portfolio
        """
        pass

    def test_remove_item_for_portfolio(self) -> None:
        """Test case for remove_item_for_portfolio

        Remove a portfolio item
        """
        pass

    def test_remove_members_for_portfolio(self) -> None:
        """Test case for remove_members_for_portfolio

        Remove users from a portfolio
        """
        pass

    def test_update_portfolio(self) -> None:
        """Test case for update_portfolio

        Update a portfolio
        """
        pass


if __name__ == '__main__':
    unittest.main()
