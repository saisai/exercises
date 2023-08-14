var stompClient = null;

function connect() {
    var socket = new SockJS('/stomp-endpoint');
    var blogpost_id;
    stompClient = Stomp.over(socket);
    stompClient.connect({}, function (frame) {
        console.log('Connected: ' + frame);
        stompClient.subscribe('/topic/greetings', function (greeting) {
            var result = JSON.parse(greeting.body);
            if(!blogpost_id && result.length > 0) {
                console.log('test' + result[0][0]);
                blogpost_id = result[0][0];
            }
            if(blogpost_id && result.length > 0) {
                console.log('test 2' + result[0][0]);
                blogpost_id = result[0][0];
            }
            if(blogpost_id){
                stompClient.send("/app/history", {}, blogpost_id);
            }
//            else {
//                stompClient.send("/app/history", {}, 0);
//            }

            var secondPart = blogpost_id;

            var newResult = []
            for(var i = 1; i < result.length; i++) {
                newResult.push(result[i]);
            }
            if(newResult.length > 0) {
                filledData(newResult, blogpost_id);
            }

        });
    });
}

function disconnect() {
    if (stompClient !== null) {
        stompClient.send("/app/history", {}, 0);
        stompClient.disconnect();
    }
    console.log("Disconnected");
}

function checkTime(i) {
if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
return i;
}

const dayName = (date, locale) =>
      date.toLocaleDateString(locale, { weekday: 'long' });

function myDate() {
      var a = new Date();
      var r = dayName(a);
      return r + '  ' + a.getFullYear() + '/' + leftInsertZero(a.getMonth() + 1) + '/' + leftInsertZero(a.getDate());
}

var mydata = [];
function filledData(data, score_mtd) {
  mydata = data;
  var content = "";
  if (data) {
    var content = '';
    if(data.length >= 1) {

      //content += '<tr class="helloMyTest-second" id="helloMyTest">';
      var newTd = ""
      for (var i = 0; i < data.length; i++) {

            var r = data[i];
            var myDeleteData = r[0] + ',' + r[1] + ',' + r[2];
            newTd += '<td class="my-testing-one" style="width: 30px; padding-left: 10px;" id="my_'+ r[0] +'"><div data-mymore="'+myDeleteData+'" class="my-delete" data-id="'+ r[0] +'" onClick="myDelete(this)">Delete</div>'
                + ' <table>'
                + '   <tr><td> '
                + '     <div><img id="'+ r[0] +'" style="width: 150px; height: 150px;"></div>'
                + '  </td></tr>'
                + '  <tr><td style="padding-top:10px;">'
                + '     <table class="first-table">'
                  + '     <tr><td>ID</td><td>' + r[0] + '</td></tr>'
                  + '     <tr><td>Date</td><td>' + r[1] + '</td></tr>'
                  + '     <tr><td>Description</td><td>' + r[2] + '</td></tr>'
                + '     </table>'
                + ' </td></tr>'
                + '</table>'
                +  '</td>';

                if(i % 5 == 0) {
                    content += '<tr class="helloMyTest-second" id="helloMyTest">';
                    content += newTd;
                    content += '</tr>';
                    newTd = "";
                }
      }

    }

    $('table.myrealtime-second tbody').after(content);
  }
}

function myDelete(e){
    var dataId = parseInt(e.getAttribute("data-id"));
    var myMoreData = e.getAttribute("data-mymore");
    var removeElement = myMoreData.split(',');
    var newArr = mydata.filter(function(itm){
      return itm[0] !== dataId;
    });
    $("#my_"+e.getAttribute("data-id")).remove();
    mydata = newArr;
    $(".helloMyTest-second").remove();
    filledData(mydata, 'test');
}

