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


class JobPosition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, position_id=None, type=None, incumbent_name=None, position_open_date=None, target_start_date=None, status=None):
        """
        JobPosition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'position_id': 'str',
            'type': 'str',
            'incumbent_name': 'str',
            'position_open_date': 'datetime',
            'target_start_date': 'datetime',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'position_id': 'positionId',
            'type': 'type',
            'incumbent_name': 'incumbentName',
            'position_open_date': 'positionOpenDate',
            'target_start_date': 'targetStartDate',
            'status': 'status'
        }

        self._id = id
        self._position_id = position_id
        self._type = type
        self._incumbent_name = incumbent_name
        self._position_open_date = position_open_date
        self._target_start_date = target_start_date
        self._status = status

    @property
    def id(self):
        """
        Gets the id of this JobPosition.

        :return: The id of this JobPosition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JobPosition.

        :param id: The id of this JobPosition.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def position_id(self):
        """
        Gets the position_id of this JobPosition.

        :return: The position_id of this JobPosition.
        :rtype: str
        """
        return self._position_id

    @position_id.setter
    def position_id(self, position_id):
        """
        Sets the position_id of this JobPosition.

        :param position_id: The position_id of this JobPosition.
        :type: str
        """

        self._position_id = position_id

    @property
    def type(self):
        """
        Gets the type of this JobPosition.

        :return: The type of this JobPosition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this JobPosition.

        :param type: The type of this JobPosition.
        :type: str
        """

        self._type = type

    @property
    def incumbent_name(self):
        """
        Gets the incumbent_name of this JobPosition.

        :return: The incumbent_name of this JobPosition.
        :rtype: str
        """
        return self._incumbent_name

    @incumbent_name.setter
    def incumbent_name(self, incumbent_name):
        """
        Sets the incumbent_name of this JobPosition.

        :param incumbent_name: The incumbent_name of this JobPosition.
        :type: str
        """

        self._incumbent_name = incumbent_name

    @property
    def position_open_date(self):
        """
        Gets the position_open_date of this JobPosition.

        :return: The position_open_date of this JobPosition.
        :rtype: datetime
        """
        return self._position_open_date

    @position_open_date.setter
    def position_open_date(self, position_open_date):
        """
        Sets the position_open_date of this JobPosition.

        :param position_open_date: The position_open_date of this JobPosition.
        :type: datetime
        """

        self._position_open_date = position_open_date

    @property
    def target_start_date(self):
        """
        Gets the target_start_date of this JobPosition.

        :return: The target_start_date of this JobPosition.
        :rtype: datetime
        """
        return self._target_start_date

    @target_start_date.setter
    def target_start_date(self, target_start_date):
        """
        Sets the target_start_date of this JobPosition.

        :param target_start_date: The target_start_date of this JobPosition.
        :type: datetime
        """

        self._target_start_date = target_start_date

    @property
    def status(self):
        """
        Gets the status of this JobPosition.

        :return: The status of this JobPosition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this JobPosition.

        :param status: The status of this JobPosition.
        :type: str
        """

        self._status = status

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
        if not isinstance(other, JobPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
