define(["jquery"], function(jQuery) {
    var $ = jQuery;

    var InputForm = {};

    InputForm.parameterTypeAbbreviations = {};

    InputForm.knownParameterTypes = {};

    InputForm.knownParameterTypes.INTEGER = "integer";
    InputForm.knownParameterTypes.STRING = "string";
    InputForm.knownParameterTypes.FLOAT = "float";
    InputForm.knownParameterTypes.FILE = "file";
    InputForm.knownParameterTypes.SELECT = "select";
    InputForm.knownParameterTypes.RADIO = "radio";
    InputForm.knownParameterTypes.CHECKBOX = "checkbox";

    InputForm.initParameterTypes = function(parameterTypeAbbreviations) {
        InputForm.parameterTypeAbbreviations = parameterTypeAbbreviations;
    };

    InputForm.buildForm = function($form, parameters, parameterOptions) {
        linkParametersAndOptions(parameters, parameterOptions);

        var formId = $form.attr("id") || "form" + Math.floor(Math.random() * 10000000);
        var data = parameters.data || [];

        for (var i = 0; i < parameters.length; i++) {
            $form.append($createInputGroup(parameters[i], formId));
        }
    };

    function linkParametersAndOptions(parameters, parameterOptions) {
        var i;
        var parameter;
        var option;

        var parameterIdIndex = {};
        var optionIdIndex = {};

        for (i = 0; i < parameters.length; i++) {
            parameter = parameters[i];
            parameterIdIndex[parameter.id] = parameter;
        }

        for (i = 0; i < parameterOptions.length; i++) {
            option = parameterOptions[i];
            optionIdIndex[option.id] = option;

            parameter = parameterIdIndex[option.parameter_id];

            if (typeof parameter === "undefined") {
                console.log("ERROR: Parameter with id '" + option.parameter_id + "' not found.");
            } else {
                parameter.options = parameter.options || [];
                parameter.options.push(option);
            }
        }

        for (i = 0; i < parameters.length; i++) {
            parameter = parameters[i];

            if (parameter.parent_option_id !== null) {
                option = optionIdIndex[parameter.parent_option_id];

                if (typeof option === "undefined") {
                    console.log("ERROR: Option with id '" + parameter.parent_option_id + "' not found.");
                } else {
                    option.parent_option = option;
                }
            }
        }
    }

    function $createInputGroup(parameter, formId) {
        var $formGroup = $("<div></div>").addClass("form-group");

        var $input = $createInput(parameter, formId);

        if ($input instanceof jQuery) {
            $formGroup.append($input);
        } else {
            return $();
        }

        var hasLabel = (typeof parameter.label === "string");
        var hasHelp = (typeof parameter.help === "string");

        if (hasLabel) {
            var $label = $("<label></label>").text(parameter.label);

            if ($input.length === 1) {
                var inputId = $input.attr("id");

                if (typeof inputId === "string") {
                    $label.attr("for", inputId);
                }
            }

            $formGroup.prepend($label);
        }

        if (hasHelp) {
            if (hasLabel) {
                var $helpButton = $("<a></a>").addClass("label-help js-simple-help");

                $helpButton.attr("href", "#");
                $helpButton.attr("data-toggle", "tooltip");
                $helpButton.attr("title", parameter.help);

                var $helpIcon = $("<i></i>").addClass("fa fa-question-circle");
                $helpButton.append($helpIcon);

                $label.after($helpButton);
            } else {
                var $helpText = $("<p></p>").addClass("help-block");
                $helpText.text(parameter.help);

                $formGroup.append($helpText);
            }
        }

        return $formGroup;
    }

    function $createInput(parameter, formId) {
        var known = InputForm.knownParameterTypes;
        var knownType = getKnownType(InputForm.parameterTypeAbbreviations[parameter.type]);

        var $input;

        switch (knownType) {
            case known.INTEGER:
            case known.FLOAT:
            case known.STRING:
                $input = $inputTextTag(parameter, knownType);
                break;
            case known.RADIO:
            case known.CHECKBOX:
                $input = $checkOrRadioButtons(parameter, knownType);
                break;
            case known.SELECT:
                $input = $selectTag(parameter);
                break;
            case known.FILE:
                $input = $inputFileTag(parameter);
                break;
            default:
                console.log("ERROR: Package parameter type \"" + parameter.type + "\" is unknown.");
                return null;
        }

        if ($input.length === 1) {
            $input.attr("id", formId + "-" + parameter.name);
        }

        return $input;
    }

    function $inputTextTag(parameter, knownType) {
        var known = InputForm.knownParameterTypes;
        var $tag = $("<input>");

        if (knownType === known.INTEGER || knownType === known.FLOAT) {
            $tag.attr("type", "number");

            if (typeof parameter.min_value === "number") {
                $tag.attr("min", parameter.min_value);
            }

            if (typeof parameter.max_value === "number") {
                $tag.attr("max", parameter.min_value);
            }

            if (typeof parameter.step_value === "number") {
                $tag.attr("step", parameter.step_value);
            }
        } else {
            $tag.attr("type", "text");
        }

        $tag.attr("name", parameter.name);
        $tag.addClass("form-control");

        if (parameter.required) {
            $tag.prop("required", true);
        }

        if (typeof parameter.label === "string") {
            $tag.attr("placeholder", parameter.label);
        }

        if (parameter.default_value !== null) {
            $tag.attr("value", parameter.default_value);
        }

        return $tag;
    }

    function $checkOrRadioButtons(parameter, knownType) {
        var known = InputForm.knownParameterTypes
        var inputType = (knownType === known.RADIO)? "radio" : "checkbox";

        var $result = $();

        if (!Array.isArray(parameter.options)) {
            return $result;
        }

        for (var i = 0; i < parameter.options.length; i++) {
            var thisOption = parameter.options[i];

            var $wrapper = $("<div></div>").addClass(inputType);

            var $label = $("<label></label>");
            $wrapper.append($label);

            var $input = $("<input>");
            $input.attr("type", inputType);
            $input.attr("name", parameter.name);
            $input.attr("value", parameter.value);

            if (thisOption.is_default) {
                $input.prop("checked", true);
            }

            $label.append($input);

            var $text = $("<span></span>");
            $text.text(thisOption.label);

            $label.append($text);

            $result = $result.add($wrapper);
        }

        return $result;
    }

    function $selectTag(parameter) {
        var $select = $("<select></select>").addClass("form-control");
        $select.attr("name", parameter.name);

        for (var i = 0; i < parameter.options.length; i++) {
            var thisOption = parameter.options[i];

            var $option = $("<option></option>");
            $option.text(thisOption.label);
            $option.attr("value", thisOption.value);

            if (thisOption.is_default) {
                $option.prop("selected", true);
            }

            $select.append($option);
        }

        return $select;
    }

    function $inputFileTag(parameter) {
        var $input = $("<input>");
        $input.attr("type", "file");
        $input.attr("name", parameter.name);

        if (typeof parameter.file_accept === "string") {
            $input.attr("accept", parameter.file_accept);
        }

        if (parameter.required) {
            $input.prop("required", true);
        }

        return $input;
    }

    function getKnownType(type) {
        if (typeof type === "undefined") {
            return null;
        }

        type = type.toLowerCase();

        for (var knownType in InputForm.knownParameterTypes) {
            if (InputForm.knownParameterTypes.hasOwnProperty(knownType) && InputForm.knownParameterTypes[knownType] === type) {
                return type;
            }
        }

        return null;
    }

    return InputForm;
});