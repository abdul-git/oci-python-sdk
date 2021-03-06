# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TerraformVersionSummary(object):
    """
    A Terraform version supported for use with stacks.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TerraformVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this TerraformVersionSummary.
        :type name: str

        """
        self.swagger_types = {
            'name': 'str'
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = None

    @property
    def name(self):
        """
        Gets the name of this TerraformVersionSummary.
        A supported Terraform version. Example: `0.12.x`


        :return: The name of this TerraformVersionSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TerraformVersionSummary.
        A supported Terraform version. Example: `0.12.x`


        :param name: The name of this TerraformVersionSummary.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
