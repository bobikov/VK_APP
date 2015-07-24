// chrome.browserAction.onClicked.addListener(function(tab) {
//     chrome.tabs.executeScript(tab.id, {file: "spamKiller.js"});
// });

chrome.tabs.onUpdated.addListener(function (tab){
    chrome.tabs.executeScript(tab.id, {file: "spamKiller.js"});
});