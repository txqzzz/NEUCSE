$(function () {
    $.fn.extend({
        SimpleTree: function (options) {
            var option = $.extend({
                click: function (a) {
                }
            }, options);

            option.tree = this;

            option._init = function () {
                this.tree.find("ul ul").hide();
                this.tree.find("ul ul").prev("li").removeClass("open");

                this.tree.find("ul ul[show='true']").show();
                this.tree.find("ul ul[show='true']").prev("li").addClass("open");
            };
            /* option._init() End */

            this.find("li").click(function () {
                option.click($(this).find("a")[0]);
                if ($(this).next("ul").attr("show") == "true") {
                    $(this).next("ul").attr("show", "false");
                    $(this).parent().find("button").first().removeClass("switched arrow-down").addClass('arrow-right');
                } else {
                    $(this).next("ul").attr("show", "true");
                    $(this).parent().find("button").first().addClass("switched arrow-down").removeClass('arrow-right');
                }
                option._init();
            });

            /*this.find("button").click(function () {
                //console.log($(this).parent().next("li").next("ul"));
                if ($(this).parent().next("li").next("ul").attr("show") == "true") {
                    $(this).parent().next("li").next("ul").attr("show", "false");
                    $(this).removeClass("switched");
                    console.log($(this).removeClass("switched"));
                } else {
                    $(this).parent().next("li").next("ul").attr("show", "true");
                    $(this).addClass("switched")
                }
                option._init();
            });*/

            this.find("ul").prev("li").addClass("folder");

            this.find("li").find("a").attr("hasChild", false);
            this.find("ul").prev("li").find("a").attr("hasChild", true);

            option._init();

        }/* SimpleTree Function End */

    });
});