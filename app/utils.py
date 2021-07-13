import logging
from featureflags.client import CfClient


cf = CfClient('Your SDK key')

__all__ = ['cf']
