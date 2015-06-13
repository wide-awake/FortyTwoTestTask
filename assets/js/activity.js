// This have nothing to do with activity.js
// Just more pythonic way to format strings
// TODO: move this away
String.prototype.format = function() {
    var formatted = this;
    for (var i = 0; i < arguments.length; i++) {
        var regexp = new RegExp('\\{'+i+'\\}', 'gi');
        formatted = formatted.replace(regexp, arguments[i]);
    }
    return formatted;
};


// Print number of request per page from django settings
document.getElementById("requests_to_show").innerHTML = window.swampdragon_settings.request_to_show;


// Subscribe once swampdragon is connected
swampdragon.open(function () {
    swampdragon.subscribe('httprequests', 'httprequests');

});

// This is the list of httprequests
var httprequestsList = document.getElementById("httprequests");


// New channel message received
swampdragon.onChannelMessage(function (channels, req) {
    // Add the notification
    if (req.action === "created") {
        addHttpRequests((req.data));
    }
});



// Add new httprequests
function addHttpRequests(req) {
	// format request
	var req_formated = '"{0} {1} {2} {3}" {4} '.format(req.method, req.url, req.server_protocol, req.status_code, req.content_len);

    // Add the new request
    var li = document.createElement("li");
    li.innerHTML = '<span class="request_date">{0}</span>, {1}'.format(req.date_formated, req_formated);
    httprequestsList.insertBefore(li, httprequestsList.firstChild);

	// Update number of requests in element and title
	document.getElementById("overall").innerHTML = req.overall;
	document.title = "{0} requsts so far".format(req.overall);

	// Hightkight new element for a while
	highlightFor(httprequestsList.firstChild, "#E3E3E3", 1.6);

    // Remove excess requests
	var requsts_to_show = window.swampdragon_settings.request_to_show;
    while (httprequestsList.getElementsByTagName("li").length > requsts_to_show) {
        httprequestsList.getElementsByTagName("li")[requsts_to_show].remove();
    }
}


// Hightkight given element
function highlightFor(element, color, seconds){
    var origcolor = element.style.backgroundColor;
    element.style.backgroundColor = color;
    var t = setTimeout(function(){
       element.style.backgroundColor = origcolor;
    },(seconds*1000));
}