define(["jquery"], function(jQuery) {
    var $ = jQuery;

    var InputForm = {};

    InputForm.parameterTypeAbbreviations = parameterTypeAbbreviations || {};

    InputForm.knownParameterTypes = {};

    InputForm.knownParameterTypes.INTEGER = "integer";
    InputForm.knownParameterTypes.STRING = "string";
    InputForm.knownParameterTypes.FLOAT = "float";
    InputForm.knownParameterTypes.FILE = "file";
    InputForm.knownParameterTypes.SELECT = "select";
    InputForm.knownParameterTypes.RADIO = "radio";
    InputForm.knownParameterTypes.CHECKBOX = "checkbox";

    InputForm.buildForm = function($form, parameters, options) {
        console.dir(parameters);
        console.dir(InputForm.parameterTypeAbbreviations);

        var parameterIdIndex = {};
        var optionIdIndex = {};

        for (var parameter in parameters) {
            parameterIdIndex[parameter.id] = parameter;
        }

        for (var option in options) {
            optionIdIndex[option.id] = option;

            var parameter = parameterIdIndex[option.parameter_id];


            if (typeof parameter === "undefined") {
                console.log("ERROR: Parameter with id '" + option.parameter_id + "' not found.");
            } else {
                parameter.options = parameter.options || [];
                parameter.options.push(option);
            }
        }

        for (var parameter in data) {

        }



        /*var formId = $form.attr("id") || "form" + Math.floor(Math.random() * 10000000);
        var data = parameters.data || [];

        for (var parameter in data) {
            $form.append($createInputGroup(parameter, formId));
        }*/
    };

    function $createInputGroup(parameter, formId) {
        var paramId = formId + "-" + parameter.name;

        var $formGroup = $("<div></div>").addClass("form-group");

        var $input = $createInput(parameter, paramId);

        if ($input instanceof jQuery) {
            $formGroup.append($input);
        } else {
            return $();
        }


        $formGroup.append($createInput(parameter, paramId));


    }

    function $createInput(parameter, paramId) {
        var known = InputForm.knownParameterTypes;
        var knownType = getKnownType(InputForm.parameterTypeAbbreviations[parameter.type]);

        var $input;

        switch (knownType) {
            case known.INTEGER:
            case known.STRING:
            case known.FLOAT:
                $input = $inputTag(parameter, knownType);
                break;
            case known.RADIO:
                //$input = $inputChoiceTags(parameter, )

            default:
                console.log("ERROR: Package parameter type \"" + parameter.type + "\" is unknown.");
                return null;
        }
    }

    function $inputTag(parameter, knownType) {

    }

    function $inputChoiceTags(parameter, knownType, tagType) {

    }

    function getKnownType(type) {
        if (typeof type === "undefined") {
            return null;
        }

        type = type.toLowerCase();

        for (var knownType in InputForm.knownParameterTypes) {
            if (type == knownType) {
                return knownType;
            }
        }

        return null;
    }

    return InputForm;
});