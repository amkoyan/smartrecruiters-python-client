# coding: utf-8

"""
    Customer API - version 1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class JobStatusHistoryContent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, changed_on=None, status=None, actions=None):
        """
        JobStatusHistoryContent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'changed_on': 'datetime',
            'status': 'JobStatus',
            'actions': 'JobStatusHistoryActions'
        }

        self.attribute_map = {
            'changed_on': 'changedOn',
            'status': 'status',
            'actions': 'actions'
        }

        self._changed_on = changed_on
        self._status = status
        self._actions = actions

    @property
    def changed_on(self):
        """
        Gets the changed_on of this JobStatusHistoryContent.

        :return: The changed_on of this JobStatusHistoryContent.
        :rtype: datetime
        """
        return self._changed_on

    @changed_on.setter
    def changed_on(self, changed_on):
        """
        Sets the changed_on of this JobStatusHistoryContent.

        :param changed_on: The changed_on of this JobStatusHistoryContent.
        :type: datetime
        """

        self._changed_on = changed_on

    @property
    def status(self):
        """
        Gets the status of this JobStatusHistoryContent.

        :return: The status of this JobStatusHistoryContent.
        :rtype: JobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this JobStatusHistoryContent.

        :param status: The status of this JobStatusHistoryContent.
        :type: JobStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def actions(self):
        """
        Gets the actions of this JobStatusHistoryContent.

        :return: The actions of this JobStatusHistoryContent.
        :rtype: JobStatusHistoryActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this JobStatusHistoryContent.

        :param actions: The actions of this JobStatusHistoryContent.
        :type: JobStatusHistoryActions
        """

        self._actions = actions

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
        if not isinstance(other, JobStatusHistoryContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other