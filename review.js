/**
 * Created by JoeHow on 5/22/17.
 */
'use strict';

$('#getColor').click(function () {
    event.preventDefault();
    var color = $('#color').val();

    $('body').css('background-color', color);

    $('#message').html(color);

    // console.log(color);
})



$('#addToDo').click(function(){
    event.preventDefault()
    var input = prompt('enter name ')
    $('#todo ul').append('<li>' + input + '</li>')

})