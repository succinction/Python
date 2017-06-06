// /**
//  * Created by chris on 5/22/17.
//  */
//
// $('#addToDo').click(function () {
//     event.preventDefault();
//     $('#toDoInput').toggle('slow');
// });
//
// $('#enter').click(function () {
//     event.preventDefault();
//     var count = $('#toDoList tr').length;
//     var item = $('#toDoInputText');
//     var html = '<tr><td class="row0">' + count + '</td><td id="td_' + count + '" class="row1">' + item.val() + '</td><td class="row2"><a class="doneLink" href="#" id="done_' + count + '">Done</a></td></tr>';
//     $('#toDoList').append(html);
//     item.val('');
//     $('#toDoInput').toggle('slow');
// });
//
// $('.doneLink').click(function () {
//     event.stopPropagation();
//     console.log(this);
// });
//
//
// // ignore this
// $('.input').keypress(function (e) {
//     if (e.which === 13) {
//         $(this).blur();
//         $('#enter').focus().click();
//     }
// });




// /**
//  * Created by JoeHow on 5/22/17.
//  */
'use strict';


$('#addToDo').click(function(){
    event.preventDefault()
    $('#todoInput').toggle('slow');
    $('#todoInputText').focus();
})

$('#enter').click(function(){
    event.preventDefault()
    var item = $('#todoInputText');
    var count = $('#todoList tr').length;
    var html = '<tr>' + '<td id="td_' + count + '"  class="row1">' + item.val() +'</td>' + '<td class="row2">  <a onclick="done(this)" href="#" id="done_' + count + '">Done</a>  </td>' +  '</tr>';
    $('#todoList').append(html);
    item.val('');
    $('#todoInput').toggle('slow');
})
function done (el) {
    event.preventDefault();
    var id = el.id.replace ( /[^\d.]/g, '' );
    var itemid = '#td_' + id;
    $(itemid).css('text-decoration', 'line-through');
    console.log(itemid)
}


// $('.doneLink').click(function () {
//     event.stopPropagation();
//     console.log(this);
// });