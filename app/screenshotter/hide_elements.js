// hides elements from tweet UI to make prettier screenshots

// thanks https://stackoverflow.com/questions/10596417/is-there-a-way-to-get-element-by-xpath-using-javascript-in-selenium-webdriver
function getElementByXpath(path) {
    return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

const TARGETS = [
    // bullet before number of views
    "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div[1]/div/div[2]",
    // number of views
    "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div[1]/div/div[3]",
    // retweets/quotes/likes/bookmarks stats bar
    "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]",
    // reply/retweet/like/bookmmark/share actions bar
    "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[7]"
];

TARGETS.forEach(elem_xpath => {
    let elem = getElementByXpath(elem_xpath);
    if(!!elem)
        elem.style.visibility = "hidden";
});