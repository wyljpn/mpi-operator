# coding: utf-8

"""
    mpijob

    Python SDK for MPI-Operator  # noqa: E501

    The version of the OpenAPI document: v2beta1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mpijob
from mpijob.models.v1_scheduling_policy import V1SchedulingPolicy  # noqa: E501
from mpijob.rest import ApiException

class TestV1SchedulingPolicy(unittest.TestCase):
    """V1SchedulingPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1SchedulingPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mpijob.models.v1_scheduling_policy.V1SchedulingPolicy()  # noqa: E501
        if include_optional :
            return V1SchedulingPolicy(
                min_available = 56, 
                min_resources = {
                    'key' : None
                    }, 
                priority_class = '', 
                queue = ''
            )
        else :
            return V1SchedulingPolicy(
        )

    def testV1SchedulingPolicy(self):
        """Test V1SchedulingPolicy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
