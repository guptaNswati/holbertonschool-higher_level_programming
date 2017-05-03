$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else {
    $('header').addClass('red');
    $('header').removeClass('green');
  }
});
