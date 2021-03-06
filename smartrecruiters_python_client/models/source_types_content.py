# coding: utf-8

"""
    Unofficial python library for the SmartRecruiters API

    The SmartRecruiters API provides a platform to integrate services or applications, build apps and create fully customizable career sites. It exposes SmartRecruiters functionality and allows to connect and build software enhancing it.

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SourceTypesContent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, label=None, actions=None, subtypes=None):
        """
        SourceTypesContent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'label': 'str',
            'actions': 'SourceTypesActions',
            'subtypes': 'list[Identifiable]'
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'actions': 'actions',
            'subtypes': 'subtypes'
        }

        self._id = id
        self._label = label
        self._actions = actions
        self._subtypes = subtypes

    @property
    def id(self):
        """
        Gets the id of this SourceTypesContent.

        :return: The id of this SourceTypesContent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SourceTypesContent.

        :param id: The id of this SourceTypesContent.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def label(self):
        """
        Gets the label of this SourceTypesContent.

        :return: The label of this SourceTypesContent.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this SourceTypesContent.

        :param label: The label of this SourceTypesContent.
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")

        self._label = label

    @property
    def actions(self):
        """
        Gets the actions of this SourceTypesContent.

        :return: The actions of this SourceTypesContent.
        :rtype: SourceTypesActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this SourceTypesContent.

        :param actions: The actions of this SourceTypesContent.
        :type: SourceTypesActions
        """

        self._actions = actions

    @property
    def subtypes(self):
        """
        Gets the subtypes of this SourceTypesContent.

        :return: The subtypes of this SourceTypesContent.
        :rtype: list[Identifiable]
        """
        return self._subtypes

    @subtypes.setter
    def subtypes(self, subtypes):
        """
        Sets the subtypes of this SourceTypesContent.

        :param subtypes: The subtypes of this SourceTypesContent.
        :type: list[Identifiable]
        """
        if subtypes is None:
            raise ValueError("Invalid value for `subtypes`, must not be `None`")

        self._subtypes = subtypes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SourceTypesContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
