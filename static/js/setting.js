$(document).ready(function () {
  $('.store').hover(function () {
    $(this).find('img').attr("src", "../static/icon/" + $(this).find('img').attr('id') + "_blue.png");
    $(this).find('p').show();
  }, function () {
    $(this).find('img').attr("src", "../static/icon/" + $(this).find('img').attr('id') + ".png");
    $(this).find('p').hide();
  });
  $('.reset').hover(function () {
    $(this).find('img').attr("src", "../static/icon/" + $(this).find('img').attr('id') + "_blue.png");
    $(this).find('p').show();
  }, function () {
    $(this).find('img').attr("src", "../static/icon/" + $(this).find('img').attr('id') + ".png");
    $(this).find('p').hide();
  });
  $('.logout').hover(function () {
    $(this).find('img').attr("src", "../static/icon/" + $(this).find('img').attr('id') + "_blue.png");
    $(this).find('p').show();
  }, function () {
    $(this).find('img').attr("src", "../static/icon/" + $(this).find('img').attr('id') + ".png");
    $(this).find('p').hide();
  });
});