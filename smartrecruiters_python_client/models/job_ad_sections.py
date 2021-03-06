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


class JobAdSections(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, company_description=None, job_description=None, qualifications=None, additional_information=None, videos=None):
        """
        JobAdSections - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'company_description': 'JobAdSection',
            'job_description': 'JobAdSection',
            'qualifications': 'JobAdSection',
            'additional_information': 'JobAdSection',
            'videos': 'JobAdVideos'
        }

        self.attribute_map = {
            'company_description': 'companyDescription',
            'job_description': 'jobDescription',
            'qualifications': 'qualifications',
            'additional_information': 'additionalInformation',
            'videos': 'videos'
        }

        self._company_description = company_description
        self._job_description = job_description
        self._qualifications = qualifications
        self._additional_information = additional_information
        self._videos = videos

    @property
    def company_description(self):
        """
        Gets the company_description of this JobAdSections.

        :return: The company_description of this JobAdSections.
        :rtype: JobAdSection
        """
        return self._company_description

    @company_description.setter
    def company_description(self, company_description):
        """
        Sets the company_description of this JobAdSections.

        :param company_description: The company_description of this JobAdSections.
        :type: JobAdSection
        """

        self._company_description = company_description

    @property
    def job_description(self):
        """
        Gets the job_description of this JobAdSections.

        :return: The job_description of this JobAdSections.
        :rtype: JobAdSection
        """
        return self._job_description

    @job_description.setter
    def job_description(self, job_description):
        """
        Sets the job_description of this JobAdSections.

        :param job_description: The job_description of this JobAdSections.
        :type: JobAdSection
        """

        self._job_description = job_description

    @property
    def qualifications(self):
        """
        Gets the qualifications of this JobAdSections.

        :return: The qualifications of this JobAdSections.
        :rtype: JobAdSection
        """
        return self._qualifications

    @qualifications.setter
    def qualifications(self, qualifications):
        """
        Sets the qualifications of this JobAdSections.

        :param qualifications: The qualifications of this JobAdSections.
        :type: JobAdSection
        """

        self._qualifications = qualifications

    @property
    def additional_information(self):
        """
        Gets the additional_information of this JobAdSections.

        :return: The additional_information of this JobAdSections.
        :rtype: JobAdSection
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """
        Sets the additional_information of this JobAdSections.

        :param additional_information: The additional_information of this JobAdSections.
        :type: JobAdSection
        """

        self._additional_information = additional_information

    @property
    def videos(self):
        """
        Gets the videos of this JobAdSections.

        :return: The videos of this JobAdSections.
        :rtype: JobAdVideos
        """
        return self._videos

    @videos.setter
    def videos(self, videos):
        """
        Sets the videos of this JobAdSections.

        :param videos: The videos of this JobAdSections.
        :type: JobAdVideos
        """

        self._videos = videos

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
        if not isinstance(other, JobAdSections):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
