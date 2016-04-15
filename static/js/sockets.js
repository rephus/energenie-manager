var socketTemplate;

$( document ).ready(function() {
  socketTemplate = $('#socket-template').html();
   Mustache.parse(socketTemplate);

   loadSockets();


});

var loadSockets = function(){
  $.ajax({
    url: "sockets",
    success: function(json){
      var rendered = Mustache.render(socketTemplate, json.sockets);
      $("#sockets").html(rendered);

      loadSwitches();
    }
  })

}

var loadSwitches = function(){

  //$('#switch-checkbox').val($(this).is(':checked'));

 $('.switch-checkbox').change(function() {
   var status = $(this).is(":checked");
   var socket = $(this).attr('id');

   console.log("Switch socket " + socket + " status " + status);
   $.ajax({
     url: "switch",
     data: {
       socket: socket,
       status: status
     }
   });

  });
}
