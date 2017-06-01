# coding=utf-8

from datetime import datetime

import boto3
import octoprint.printer

class temperature_probe(octoprint.printer.PrinterCallback):

	def __init__(self):
		self._cloudwatch = boto3.client('cloudwatch')

	def on_printer_add_temperature(self, data):
		timestamp = datetime.fromtimestamp(data['time'])

		metrics = [
			self._build_metric('tool0', data['tool0'], timestamp),
			self._build_metric('bed', data['bed'], timestamp)
			]

		self._cloudwatch.put_metric_data(Namespace='OctoPrint/Temperature', MetricData=metrics)

	def _build_metric(self, tool, data, timestamp):
		metric = dict(Unit='None', Timestamp=timestamp)
		metric['MetricName'] = tool
		metric['Value'] = data['actual']
		return metric

