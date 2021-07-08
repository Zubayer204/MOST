// get cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// subscribe form 
$("#success-alert").hide();
$("#subscribe-form").submit(function (event) {
  let formData = {
    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
    email: $("input[name='email']").val()
  };
  let url = $("#subscribe-form")[0].action;

  $.ajax({
    type: 'POST',
    url: url,
    data: formData,
    dataType: 'json',
    encode: true
  }).done(function(data) {
    console.log(data);
    $("#alert-msg").text(data.msg);
    $("#success-alert").attr('class', data.style)
  });
  $("#success-alert").fadeTo(3000, 500).slideUp(500, function(){
    $("#success-alert").slideUp(500);
  });
  event.preventDefault();  
});

// ask and save location
function getLocation(callback) {
    var promise = new Promise(function(resolve, reject) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                function(position){
                    resolve({lat: position.coords.latitude, lon: position.coords.longitude})
                },
                function(error) {
                  if (error.code == error.PERMISSION_DENIED)
                    reject("Unknown")
                }
            );
        } else {
          reject("Unknown");
        }
    });

    return promise;
}

const csrftoken = getCookie('csrftoken');
var locationPromise = getLocation();
// locationPromise
// .then(function(loc) { console.log(loc); })
// .catch(function(err) { console.log("No location"); });
locationPromise
      .then(function(loc) {
        let newData = {
          lat: loc.lat,
          lon: loc.lon,
          r_url: window.location.href.replace(window.location.origin, '')
        };
        let settings = {
          type: 'POST',
          url: "/api/visitor/",
          headers: {'X-CSRFToken': csrftoken},
          data: newData,
          dataType: 'json',
          encode: true
        };
        $.ajax(settings).done(function(data) {
          console.log(data);
        });
      })
      .catch(function(err) {
        let newData = {
          lat: 0,
          lon: 0,
          r_url: window.location.href.replace(window.location.origin, '')
        };
        let settings = {
          type: 'POST',
          url: "/api/visitor/",
          headers: {'X-CSRFToken': csrftoken},
          data: newData,
          dataType: 'json',
          encode: true
        };
        $.ajax(settings).done(function(data) {
          console.log(data);
        });
      });
