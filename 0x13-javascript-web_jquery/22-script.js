$.get('http://swapi.co/api/films?format=json',
  function (data) {
    $.each(data['results'], function (i, item) {
      $('UL#list_movies').append('<li>' + item['title'] + '</li>');
    });
  });
