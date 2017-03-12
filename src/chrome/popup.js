chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {type: "getData"}, function(data) {
            console.log('data');
            console.log(data);
            $('p#data').html(data);
        });
    });
