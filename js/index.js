let optionName = document.querySelectorAll('.function')
$(optionName).hide();
$(document).ready(function () {
  let menu = document.querySelector('.menu');
  let optionName = document.querySelectorAll('.function')
  $(menu).hover(function () {
    $(optionName).show()
    $(this).css('width', '220px');
  }, function () {
    $(optionName).hide()
    $(this).css('width', '100px');
  });
});
$(document).ready(function () {
  let picId;
  $('.option').hover(function () {
    picId = $(this).find('img').attr('id');
    $('#' + picId).attr("src", "../icon/" + picId + "_blue.png");
    $(this).siblings().css("background-color", "#B6FFFF");
    $(this).css("background-color", "rgba(255, 255, 255, 0.3)");
  }, function () {
    picId = $(this).find('img').attr('id');
    $('#' + picId).attr("src", "../icon/" + picId + ".png");
    $(this).siblings().css("background-color", "transparent");
    $(this).css("background-color", "#000000");
  });
});
$(document).ready(function () {
  $('.decoration').hover(function () {
    $(this).css("background-color", "#B6FFFF");
  }, function () {
    $(this).css("background-color", "#000000");
  });
});
