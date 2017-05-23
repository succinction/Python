/**
 * Created by JoeHow on 5/22/17.
 */
'use strict';

$('#checkVowel').click(function(){
    event.preventDefault();
    var inpt = $('#inn').val();
    var vees = ['a','e','i','o','u'];
    var verdict = (vees.indexOf(inpt) != -1) ? "is VOWEL" : "is NOT vowel" ;
    $('#message ul').append('<li>' + inpt + ' : ' + verdict + '</li>')
})
