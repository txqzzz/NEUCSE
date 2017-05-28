$("#nav > li").hover(function () {
    var ul = $(this).find('ul')[0];
    $(ul).slideDown(200);
}, function () {
    var ul = $(this).find('ul')[0];
    $(ul).slideUp(20);
});