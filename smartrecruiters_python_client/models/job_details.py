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


class JobDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, title=None, ref_number=None, created_on=None, updated_on=None, last_activity_on=None, department=None, location=None, status=None, posting_status=None, target_hiring_date=None, industry=None, function=None, type_of_employment=None, experience_level=None, eeo_category=None, template=None, creator=None, compensation=None, job_ad=None, properties=None, actions=None):
        """
        JobDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'title': 'str',
            'ref_number': 'str',
            'created_on': 'datetime',
            'updated_on': 'datetime',
            'last_activity_on': 'datetime',
            'department': 'Department',
            'location': 'Location',
            'status': 'JobStatus',
            'posting_status': 'PostingStatus',
            'target_hiring_date': 'datetime',
            'industry': 'ModelProperty',
            'function': 'ModelProperty',
            'type_of_employment': 'ModelProperty',
            'experience_level': 'ModelProperty',
            'eeo_category': 'ModelProperty',
            'template': 'bool',
            'creator': 'UserIdentity',
            'compensation': 'Compensation',
            'job_ad': 'JobAdInput',
            'properties': 'list[JobProperty]',
            'actions': 'JobDetailsActions'
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'ref_number': 'refNumber',
            'created_on': 'createdOn',
            'updated_on': 'updatedOn',
            'last_activity_on': 'lastActivityOn',
            'department': 'department',
            'location': 'location',
            'status': 'status',
            'posting_status': 'postingStatus',
            'target_hiring_date': 'targetHiringDate',
            'industry': 'industry',
            'function': 'function',
            'type_of_employment': 'typeOfEmployment',
            'experience_level': 'experienceLevel',
            'eeo_category': 'eeoCategory',
            'template': 'template',
            'creator': 'creator',
            'compensation': 'compensation',
            'job_ad': 'jobAd',
            'properties': 'properties',
            'actions': 'actions'
        }

        self._id = id
        self._title = title
        self._ref_number = ref_number
        self._created_on = created_on
        self._updated_on = updated_on
        self._last_activity_on = last_activity_on
        self._department = department
        self._location = location
        self._status = status
        self._posting_status = posting_status
        self._target_hiring_date = target_hiring_date
        self._industry = industry
        self._function = function
        self._type_of_employment = type_of_employment
        self._experience_level = experience_level
        self._eeo_category = eeo_category
        self._template = template
        self._creator = creator
        self._compensation = compensation
        self._job_ad = job_ad
        self._properties = properties
        self._actions = actions

    @property
    def id(self):
        """
        Gets the id of this JobDetails.

        :return: The id of this JobDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JobDetails.

        :param id: The id of this JobDetails.
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this JobDetails.

        :return: The title of this JobDetails.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this JobDetails.

        :param title: The title of this JobDetails.
        :type: str
        """

        self._title = title

    @property
    def ref_number(self):
        """
        Gets the ref_number of this JobDetails.

        :return: The ref_number of this JobDetails.
        :rtype: str
        """
        return self._ref_number

    @ref_number.setter
    def ref_number(self, ref_number):
        """
        Sets the ref_number of this JobDetails.

        :param ref_number: The ref_number of this JobDetails.
        :type: str
        """

        self._ref_number = ref_number

    @property
    def created_on(self):
        """
        Gets the created_on of this JobDetails.

        :return: The created_on of this JobDetails.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """
        Sets the created_on of this JobDetails.

        :param created_on: The created_on of this JobDetails.
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """
        Gets the updated_on of this JobDetails.
        Job modification date

        :return: The updated_on of this JobDetails.
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """
        Sets the updated_on of this JobDetails.
        Job modification date

        :param updated_on: The updated_on of this JobDetails.
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def last_activity_on(self):
        """
        Gets the last_activity_on of this JobDetails.
        Indicates last activity associated with a job

        :return: The last_activity_on of this JobDetails.
        :rtype: datetime
        """
        return self._last_activity_on

    @last_activity_on.setter
    def last_activity_on(self, last_activity_on):
        """
        Sets the last_activity_on of this JobDetails.
        Indicates last activity associated with a job

        :param last_activity_on: The last_activity_on of this JobDetails.
        :type: datetime
        """

        self._last_activity_on = last_activity_on

    @property
    def department(self):
        """
        Gets the department of this JobDetails.

        :return: The department of this JobDetails.
        :rtype: Department
        """
        return self._department

    @department.setter
    def department(self, department):
        """
        Sets the department of this JobDetails.

        :param department: The department of this JobDetails.
        :type: Department
        """

        self._department = department

    @property
    def location(self):
        """
        Gets the location of this JobDetails.

        :return: The location of this JobDetails.
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this JobDetails.

        :param location: The location of this JobDetails.
        :type: Location
        """

        self._location = location

    @property
    def status(self):
        """
        Gets the status of this JobDetails.

        :return: The status of this JobDetails.
        :rtype: JobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this JobDetails.

        :param status: The status of this JobDetails.
        :type: JobStatus
        """

        self._status = status

    @property
    def posting_status(self):
        """
        Gets the posting_status of this JobDetails.

        :return: The posting_status of this JobDetails.
        :rtype: PostingStatus
        """
        return self._posting_status

    @posting_status.setter
    def posting_status(self, posting_status):
        """
        Sets the posting_status of this JobDetails.

        :param posting_status: The posting_status of this JobDetails.
        :type: PostingStatus
        """

        self._posting_status = posting_status

    @property
    def target_hiring_date(self):
        """
        Gets the target_hiring_date of this JobDetails.

        :return: The target_hiring_date of this JobDetails.
        :rtype: datetime
        """
        return self._target_hiring_date

    @target_hiring_date.setter
    def target_hiring_date(self, target_hiring_date):
        """
        Sets the target_hiring_date of this JobDetails.

        :param target_hiring_date: The target_hiring_date of this JobDetails.
        :type: datetime
        """

        self._target_hiring_date = target_hiring_date

    @property
    def industry(self):
        """
        Gets the industry of this JobDetails.

        :return: The industry of this JobDetails.
        :rtype: ModelProperty
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """
        Sets the industry of this JobDetails.

        :param industry: The industry of this JobDetails.
        :type: ModelProperty
        """

        self._industry = industry

    @property
    def function(self):
        """
        Gets the function of this JobDetails.

        :return: The function of this JobDetails.
        :rtype: ModelProperty
        """
        return self._function

    @function.setter
    def function(self, function):
        """
        Sets the function of this JobDetails.

        :param function: The function of this JobDetails.
        :type: ModelProperty
        """

        self._function = function

    @property
    def type_of_employment(self):
        """
        Gets the type_of_employment of this JobDetails.

        :return: The type_of_employment of this JobDetails.
        :rtype: ModelProperty
        """
        return self._type_of_employment

    @type_of_employment.setter
    def type_of_employment(self, type_of_employment):
        """
        Sets the type_of_employment of this JobDetails.

        :param type_of_employment: The type_of_employment of this JobDetails.
        :type: ModelProperty
        """

        self._type_of_employment = type_of_employment

    @property
    def experience_level(self):
        """
        Gets the experience_level of this JobDetails.

        :return: The experience_level of this JobDetails.
        :rtype: ModelProperty
        """
        return self._experience_level

    @experience_level.setter
    def experience_level(self, experience_level):
        """
        Sets the experience_level of this JobDetails.

        :param experience_level: The experience_level of this JobDetails.
        :type: ModelProperty
        """

        self._experience_level = experience_level

    @property
    def eeo_category(self):
        """
        Gets the eeo_category of this JobDetails.

        :return: The eeo_category of this JobDetails.
        :rtype: ModelProperty
        """
        return self._eeo_category

    @eeo_category.setter
    def eeo_category(self, eeo_category):
        """
        Sets the eeo_category of this JobDetails.

        :param eeo_category: The eeo_category of this JobDetails.
        :type: ModelProperty
        """

        self._eeo_category = eeo_category

    @property
    def template(self):
        """
        Gets the template of this JobDetails.

        :return: The template of this JobDetails.
        :rtype: bool
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this JobDetails.

        :param template: The template of this JobDetails.
        :type: bool
        """

        self._template = template

    @property
    def creator(self):
        """
        Gets the creator of this JobDetails.

        :return: The creator of this JobDetails.
        :rtype: UserIdentity
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this JobDetails.

        :param creator: The creator of this JobDetails.
        :type: UserIdentity
        """

        self._creator = creator

    @property
    def compensation(self):
        """
        Gets the compensation of this JobDetails.

        :return: The compensation of this JobDetails.
        :rtype: Compensation
        """
        return self._compensation

    @compensation.setter
    def compensation(self, compensation):
        """
        Sets the compensation of this JobDetails.

        :param compensation: The compensation of this JobDetails.
        :type: Compensation
        """

        self._compensation = compensation

    @property
    def job_ad(self):
        """
        Gets the job_ad of this JobDetails.

        :return: The job_ad of this JobDetails.
        :rtype: JobAdInput
        """
        return self._job_ad

    @job_ad.setter
    def job_ad(self, job_ad):
        """
        Sets the job_ad of this JobDetails.

        :param job_ad: The job_ad of this JobDetails.
        :type: JobAdInput
        """

        self._job_ad = job_ad

    @property
    def properties(self):
        """
        Gets the properties of this JobDetails.

        :return: The properties of this JobDetails.
        :rtype: list[JobProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this JobDetails.

        :param properties: The properties of this JobDetails.
        :type: list[JobProperty]
        """

        self._properties = properties

    @property
    def actions(self):
        """
        Gets the actions of this JobDetails.

        :return: The actions of this JobDetails.
        :rtype: JobDetailsActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this JobDetails.

        :param actions: The actions of this JobDetails.
        :type: JobDetailsActions
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
        if not isinstance(other, JobDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
