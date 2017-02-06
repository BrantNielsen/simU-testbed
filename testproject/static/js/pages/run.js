/* global parameterTypeAbbreviations, parameters, parameterOptions */
require(['jquery', 'forms/InputForm'], function ($, InputForm) {
    InputForm.initParameterTypes(parameterTypeAbbreviations);
    InputForm.buildForm($("#jsInputForm"), parameters.data, parameterOptions.data);
});