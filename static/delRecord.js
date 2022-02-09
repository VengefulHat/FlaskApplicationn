$(function()
{
$('a#deleteRecord').bind('click', function() {
  $.getJSON('http://127.0.0.1:5000/_delete_record', {
    me: $('td[id="me"]').innerHTML()
  }, function(data) {
    $("#result").text(data.result);
  });
  return false;
});
});

///$('td#me').text()

///kasowanie rekordu
$(function()
{
$('button#endexist').bind('click', function() {
   var num = prompt("Podaj ID rekordu: ", "");
  $.getJSON('http://127.0.0.1:5000/_delete_record', {
    me: num
  });
});
});
/// Archiwizacja rekordu
$(function()
{
$('button#archdel').bind('click', function() {
   var num = prompt("Archiwizacja ma na celu wykasowanie konkretnego rekordu" +
       " i przeniesienie go do osobnej bazy, jesli błąd wystąpi ponownie to się tu nie pojawi" +
       " - jeśli występuje juz w bazie (jeśli jest zarchiwizowany): ", "");
  $.getJSON('http://127.0.0.1:5000/_archiwizacja_', {
    me: num
  });
});
});

/// kasowanie z bazy dla http_200 (to te główne domeny tylko)
$(function()
{
$('button#endexist200').bind('click', function() {
   var num = prompt("Podaj ID rekordu: ", "");
  $.getJSON('http://127.0.0.1:5000/_delete_record_200', {
    me: num
  });
});
});

/// archiwizacja dla http_200
$(function()
{
$('button#archdel200').bind('click', function() {
   var num = prompt("Archiwizacja ma na celu wykasowanie konkretnego rekordu" +
       " i przeniesienie go do osobnej bazy, jesli błąd wystąpi ponownie to się tu nie pojawi" +
       " - jeśli występuje juz w bazie (jeśli jest zarchiwizowany): ", "");
  $.getJSON('http://127.0.0.1:5000/_archiwizacja_200', {
    me: num
  });
});
});