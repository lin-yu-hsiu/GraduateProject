let optionName = document.querySelectorAll('.function')
let menu = document.querySelector('.menu');

$(document).ready(function () {
  $(menu).hover(function () {
    $(optionName).fadeIn(300)
    $(this).css('width', '190px');
  }, function () {
    $(optionName).hide()
    $(this).css('width', '100px');
  });
});
$(document).ready(function () {
  let picId;
  $('.option').hover(function () {
    picId = $(this).find('img').attr('id');
    $('#' + picId).attr("src", "../static/icon/" + picId + "_blue.png");
    $(this).siblings().css("background-color", "#B6FFFF");
    $(this).css("background-color", "rgba(255, 255, 255, 0.3)");
  }, function () {
    picId = $(this).find('img').attr('id');
    $('#' + picId).attr("src", "../static/icon/" + picId + ".png");
    $(this).siblings().css("background-color", "transparent");
    $(this).css("background", "transparent");
  });
});
$(document).ready(function () {
  $('.decoration').hover(function () {
    $(this).css("background-color", "#B6FFFF");
  }, function () {
    $(this).css("background", "transparent");
  });
});
