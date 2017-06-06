/**
 * Created by JoeHow on 6/5/17.
 */
'use strict';


var x = document.getElementById("location");
var getLocation = function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}
var lat;
var lon;
function showPosition(position) {
    lat = position.coords.latitude
    lon = position.coords.longitude
    x.innerHTML = "Latitude: " + position.coords.latitude +
    "<br>Longitude: " + position.coords.longitude;
    newWeather();
}

$('#getLoc').click(getLocation)

// $('#newWeather').click(function () {
var newWeather = function () {
//    event.preventDefault();
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather",
        type: "GET",
        data: {
            'APPID': 'c8eac569cc2d3fdfcacf8e3d12ab728f',
            'lat': lat,
            'lon': lon
        },
        success: function (data) {
            console.log('SUCCESS')

            $("#weather").html(data.name + " : " + data.weather[0].description + " : " + data.weather[0].main)
            console.log("THIS : ",data)
        },
        error: function (data) {
            console.log("ERROR");
            console.log(data);
        }
    });
}