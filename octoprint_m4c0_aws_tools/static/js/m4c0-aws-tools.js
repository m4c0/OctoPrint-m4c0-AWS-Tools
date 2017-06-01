/*
 * View model for OctoPrint-m4c0-AWS-Tools
 *
 * Author: Eduardo Costa
 * License: AGPLv3
 */
$(function() {
    function view_model(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        view_model,

        // e.g. loginStateViewModel, settingsViewModel, ...
        [ /* "loginStateViewModel", "settingsViewModel" */ ],

        // e.g. #settings_plugin_m4c0-aws-tools, #tab_plugin_m4c0-aws-tools, ...
        [ /* ... */ ]
    ]);
});
