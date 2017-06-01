# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class m4c0_aws_tools_plugin(octoprint.plugin.SettingsPlugin,
                            octoprint.plugin.AssetPlugin,
                            octoprint.plugin.TemplatePlugin):

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict()

	##~~ TemplatePlugin mixin

	def get_template_configs(self):
		return [ dict(type="settings", custom_bindings=False) ]

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/m4c0-aws-tools.js"],
			css=["css/m4c0-aws-tools.css"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			m4c0awstools=dict(
				displayName="m4c0's AWS Tools Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="m4c0",
				repo="OctoPrint-m4c0-AWS-Tools",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/m4c0/OctoPrint-m4c0-AWS-Tools/archive/{target_version}.zip"
			)
		)

__plugin_name__="m4c0's AWS Tools"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = m4c0_aws_tools_plugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

