define([
    'base/js/namespace'
], function(
    Jupyter
) {
    function load_ipython_extension() {

        var handler = function () {
            window.location = "http://spark.apache.org/";
        };

        var action = {
            icon: 'fa-play-circle', 
            help    : 'Click here to redirect to Spark Website',
            handler : handler
        };

        var prefix = 'add-action-button';
        var action_name = 'redirect-on-action';

        var full_action_name = Jupyter.actions.register(action, action_name, prefix); 
        Jupyter.toolbar.add_buttons_group([full_action_name]);
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});