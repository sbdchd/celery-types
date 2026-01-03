import boto3 as boto3
from botocore import exceptions as exceptions
from botocore.awsrequest import AWSRequest as AWSRequest
from botocore.httpsession import get_cert_path as get_cert_path
from botocore.response import get_response as get_response

__all__ = ("AWSRequest", "exceptions", "get_cert_path", "get_response")
