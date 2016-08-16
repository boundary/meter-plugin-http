TrueSight Pulse Meter Plugin for HTTP Page Load
===============================================

Meter plugin to measures the page load time of a given URL

### Prerequisites

|     OS    | Linux | Windows | SmartOS | OS X |
|:----------|:-----:|:-------:|:-------:|:----:|
| Supported |   v   |    v    |    v    |  v   |

- Installation of [python 2.7.X or later](https://wiki.python.org/moin/BeginnersGuide/Download)
- Installation of [pip](https://pip.pypa.io/en/stable/installing/)

#### Runtime Environment

|  Runtime | node.js | Python | Java |
|:---------|:-------:|:------:|:----:|
| Required |         |    v   |      |

* [How to install python?](https://wiki.python.org/moin/BeginnersGuide/Download)
* This plugin works with Python 2.7

### Plugin Setup

This plugin requires that the following Python packages are installed:

- `meterplugin`
- `beautifulsoup4`

```
$ pip install beautifulsoup4 meterplugin
```

### Plugin Configuration Fields

|Field Name    |Description                                                      |
|:-------------|:----------------------------------------------------------------|
|URL           |Url to measure the time to load the page                         |
|Interval (ms) |How often (in milliseconds) to measure the time to load a the url|
|Source        |Label to display in the legend for the measurement data          |

### Metrics Collected

|Metric Name     |Description           |
|:---------------|:---------------------|
|HTTP\_PAGE\_LOAD|Web page load duration|

### Dashboards

- HTTP Page Load
