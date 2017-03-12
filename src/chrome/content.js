$(function() {
  console.log("Reading page url and sending to Backend");
  var url = window.location.href;
  console.log("Detected url", url);
  console.log("sending to server")
  var data;
  $.get({
    url: "https://localhost:5000/read_url",
    data: {"url":url},
    success: function (data) {
      console.log('content data', data);
      chrome.runtime.onMessage.addListener(
        function(message, sender, sendResponse) {
            switch(message.type) {
                case "getData":
                    console.log('getData' ,data);
                    sendResponse(data);
                    break;
                default:
                    console.error("Unrecognised message: ", message);
            }
        });
      }
    });



});
