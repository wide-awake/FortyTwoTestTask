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



(function poll() {
    setTimeout(function() {

        var overall = parseInt($("#overall").text());
        var httprequestsList = document.getElementById("httprequests");
        var requsts_to_show = 25;

        $.ajax({
            url: "/requests/ajax/get_httpreq",
            type: "GET",
	        data: {elements_so_far:  overall},
            success: function(data) {
                console.log("we got: " + data);
                console.log("type: " + typeof(data));
	            console.log("old: " + overall);

                var new_elements = (data.match(/<li>/g)  || []).length;
                console.log("new " + new_elements);


	            // Add the new request
                if (new_elements > 0) {
                    var li = document.createElement("li");
			        li.innerHTML = data;
			        httprequestsList.insertBefore(li, httprequestsList.firstChild);

				    // Update number of requests in element and title
				    document.getElementById("overall").innerHTML = overall + new_elements;
				    document.title = "{0} requsts so far".format(overall + new_elements);

	                // Remove excess requests
	                while (httprequestsList.getElementsByTagName("li").length > requsts_to_show) {
			            httprequestsList.getElementsByTagName("li")[requsts_to_show].remove();
	                }
                }
            },
            //dataType: "json",
            complete: poll,
            timeout: 5000
        })
    }, 6000);
})();

// Hightkight given element
function highlightFor(element, color, seconds){
    var origcolor = element.style.backgroundColor;
    element.style.backgroundColor = color;
    var t = setTimeout(function(){
       element.style.backgroundColor = origcolor;
    },(seconds*1000));
}