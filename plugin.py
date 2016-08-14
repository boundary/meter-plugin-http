# Copyright 2016 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from meterplugin import Collector
from meterplugin import Plugin
from meterplugin import Measurement
from meterplugin import MeasurementSinkAPI
from random import randrange
from time import time, sleep
from soup import Soup
import logging
import sys

logger = logging.getLogger(__name__)


class HttpCollector(Collector):
    def __init__(self, interval=1000, name=None, url=None, source=None):
        """
        Initialize the HTTP collector
        :param interval: How often in milli-seconds to generate a random number
        :param name: Name of the collector (becomes the thread name)
        :param url: Url to measure the load time
        :param source: Label used for generated measurements
        """
        super(HttpCollector, self).__init__(interval=interval, name=name)
        self.url = url
        self.source = source
        # self.measurement_output = MeasurementSinkAPI()

    def initialize(self):
        """
        Initialize the collector
        :return: None
        """
        pass

    def starting(self):
        """
        Called when collector is starting
        :return: None
        """
        pass

    def measure_page_load(self):
        t0 = time()
        delay = float(randrange(1000, 3000)) / 1000.0
        sleep(delay)
        t1 = time()

        return round((t1 - t0) * 1000.0, 3)

    def collect(self):
        """
        :return:
        """
        logger.info("Measuring page load for: {0}".format(self.url))
        soup = Soup(url=self.url)
        value = soup.measure_load_time()
        m = Measurement(metric='HTTP_PAGE_LOAD',
                        value=value,
                        source=self.source)
        self.measurement_output.send(m)


class HttpPlugin(Plugin):
    def __init__(self):
        super(HttpPlugin, self).__init__()
        logging.basicConfig(level=logging.DEBUG,
                            format='[%(levelname)s] (%(threadName)s) %(message)s',
                            stream=sys.stderr)

    def initialize(self):
        """
        Initialize the plugin
        :return: None
        """
        pass

    def starting(self):
        """
        Plugin is starting
        :return: None
        """
        pass

    def create_collector(self, item):
        """
        Creates the collectors associated with this plugin
        :param item: Parameters from the items array in param.json
        :return: Derived class from Collector
        """

        # Extract parameters from item
        if 'interval' in item:
            interval = item['interval']
        else:
            interval = 1000
        if 'url' in item:
            url = item['url']
        if 'source' in item:
            source = item['source']
            name = source
        else:
            source = url

        return HttpCollector(interval=interval, name=name, url=url, source=source)
