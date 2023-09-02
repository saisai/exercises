var stompClient = null;


function setCurrentDateTime() {
    document.getElementById("currentDateTime").innerHTML = new Date();
}

// return Milliseconds
function getTime() {
//    var result = document.getElementById("currentDateTime").value;
//    console.log("hello result " + result);
//    console.log("html " + $("#currentDateTime").html());
//    console.log("val " + $("#currentDateTime").val());

    var htmlResult = $("#currentDateTime").html()

    var newDate = new Date(htmlResult);
    var time = newDate.getTime();
    console.log("hello " + time);
    document.getElementById("currentDateTimeToGetTime").innerHTML = time;
    document.getElementById("currentDateTimeToGetTime2").innerHTML = JSON.stringify(prev_id);
    return time
}

// 3,600,000 milliseconds == 1 hour
// 5 minutes = 300,000 milliseconds
// 1 minute = 60,000 milliseconds
// 15 minutes = 900,000 milliseconds
// 30 minutes = 1,800,000 milliseconds
// 1 hour in milliseconds javascript
function getDifferntTime() {
    var now = new Date();
    var setUpTime =  parseInt( $("#currentDateTimeToGetTime").html() );
    document.getElementById("setUpTime").innerHTML = setUpTime
    var differentTime  = now.getTime() - setUpTime;
    document.getElementById("differentTime").innerHTML = differentTime;
    return differentTime;
}

function leftInsertZero(int_num) {
    return pad(int_num, 2, '0');
}

  function startTime() {
    const today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    try {
      document.getElementById('realtime-hour-minute').innerHTML = h + ":" + m;
      document.getElementById('realtime-seconds').innerHTML = ":" + s;
      setTimeout(startTime, 1000);
    } catch (err) {
      //console.log("error");
    }
  }


function pad(s, w, c) {
    s = s + '';
    c = c || '0';
    return s.length >= w ? s : new Array(w - s.length + 1).join(c) + s;
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

var prev_id = [0];

function connect() {
    var socket = new SockJS('/stomp-endpoint');
    var blogpost_id;
    stompClient = Stomp.over(socket);
    stompClient.connect({}, function (frame) {
        //console.log('Connected: ' + frame);
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
            else {
                stompClient.send("/app/history", {}, 0);
            }

            if(result && result[0])
            {
                filledFirst(result[0], result[0][0]);

                console.log("prev id " + prev_id);
                console.log("blogpost_id " + blogpost_id);

                if(! prev_id.includes(blogpost_id)) {
                    setCurrentDateTime();
                    //getTime();
                    setTimeout(getTime, 1000);
                    prev_id = [];
                    prev_id.push(blogpost_id);
                }
                //getTime();
            }

            var newResult = []
            for(var i = 1; i < result.length; i++) {
                newResult.push(result[i]);
            }
            if(newResult.length > 0) {
                $(".helloMyTest-second").remove();
                filledData(newResult, blogpost_id);
            }

            startTime();

//            if(blogpost_id) {
//                //setTimeout(getDifferntTime, 1000);
//                getDifferntTime();
//            }

        });
    });
}

// https://stackoverflow.com/questions/7188145/call-a-javascript-function-every-5-seconds-continuously
// 1 minute = 60,000 milliseconds
const interval = setInterval(function() {
   // method to be executed;
   var diffTime = getDifferntTime();
   var runAtWhen = 600000;
   if(diffTime > runAtWhen ) {
      if(mydata.length > 0) {
        deleteAll();
      }

   }

   //if(mydata.length > 0) {
        deleteAll();
    //}

   console.log("mydata " + JSON.stringify(mydata));


 }, 60000 );
// clearInterval(interval);

//const interval2 = setInterval(function() {
//   // method to be executed;
//
//   deleteAll();
// }, 10000);
function disconnect() {
    if (stompClient !== null) {
        stompClient.send("/app/history", {}, 0);
        stompClient.disconnect();
    }
    console.log("Disconnected");
}


var mydata = [];

function filledFirst(data, score) {

    if(data !== undefined) {
        $(".first-data-tr").remove();
        my_content = '';
        my_content += '<tr class="first-data-tr" data-cost_level="'+score+'" value="'+score+'">';
         my_content += '<td style="width:20%;">'
              + '  <div style="padding-left: 10px;" class="l user-img"><img  id="'+ data[1] +'" data-_capture="'+ data[2] +'" style="width: 150px; height: 150px;" class="mtd-image radius img-user"  >' + '' + '</div>'
              + '  </td>'
              + '  <td style="width:30%;"><div class="l">'
              + ' <table class="first-table">'
              + ' <tr><td>Employee ID</td><td>' + data[0] + '</td></tr>'
              + ' <tr><td>First Name</td><td>' + data[1] + '</td></tr>'
              + ' <tr><td>Department</td><td>' + data[2] + '</td></tr>'
              + ' </table>'
              + ' </div></td>'
              + '<td style="width:50%;">'
              + '<div><span id="realtime-hour-minute" style="font-size: 100px;"></span><span id="realtime-seconds" style="font-size: 30px;"></span></div>'
              + '<div><span style="font-weight: bold; font-size: 20px;">' + myDate() + '</span></div>'
              + '</td>';
         my_content += '</tr>';
         $('table.my-realtime-table-first tbody').after(my_content);
    }
}


function filledData(data, score_mtd) {
  mydata = data;
  console.log("fillData lenght " + mydata.length);
  if (data) {
    var content = '';
    if(data.length >= 1) {
      var newTd = ""
      var fiveRows = 5;
      for (var i = 0; i < mydata.length; i++) {
        if (i % fiveRows === 0 && i > 0) {
            content += '</tr><tr class="helloMyTest-second">';
          }
        var r = mydata[i];
        newTd = '<td class="my-testing-one" style="width: 30px; padding-left: 10px;" id="my_'+ r[0] +'"><div class="my-delete" data-id="'+ r[0] +'" onClick="myDelete(this)">Delete</div>'
            + ' <table>'
            + '   <tr><td> '
            + '     <div><img id="'+ r[0] +'" style="float:left; width: 150px; height: 150px;"></div>'
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
        content += newTd;
      }
      content = '<tr class="helloMyTest-second">' + content + '</tr>';
      $('table.myrealtime-second tbody').after(content);
    }

  }
}

function myDelete(e){
    var dataId = parseInt(e.getAttribute("data-id"));
    var newArr = mydata.filter(function(itm){
      return itm[0] !== dataId;
    });

    var json = {
           "blogPostID" : dataId
          };

    $.ajax({
           type : "POST",
           contentType : "application/json",
           url : "/updateDelete",
           data : JSON.stringify(json),
           dataType : 'json',
           cache : false,
           timeout : 600000,
           success : function(data) {
//            var html = '';
//            var len = data.length;
//            html += '<option value="0"></option>';
//            for (var i = 0; i < len; i++) {
//             html += '<option value="' + data[i].id + '">'
//               + data[i].name
//               + '</option>';
//            }
//            html += '</option>';
//            $('#cityId').html(html);
           },
           error : function(e) {
            console.log("Update dlete " + JSON.stringify(e));
           }
          });

    $("#my_"+e.getAttribute("data-id")).remove();
    mydata = newArr;
    $(".helloMyTest-second").remove();
    filledData(mydata, 'test');
}

// https://stackoverflow.com/questions/10632346/how-to-format-a-date-in-mm-dd-yyyy-hhmmss-format-in-javascript
Number.prototype.padLeft = function(base,chr){
    var  len = (String(base || 10).length - String(this).length)+1;
    return len > 0? new Array(len).join(chr || '0')+this : this;
}

function deleteAll(){
    var time = parseInt($("#currentDateTimeToGetTime").html());
    var tmp = new Date(time);
    var endTime =`${tmp.getFullYear()}-${(tmp.getMonth()+1).padLeft()}-${tmp.getDate().padLeft()} ${tmp.getHours().padLeft()}:${tmp.getMinutes().padLeft()}:${tmp.getSeconds().padLeft()}`
    var json = {
           "endTime" : endTime
          };

    $.ajax({
           type : "POST",
           contentType : "application/json",
           url : "/deleteAll",
           data : JSON.stringify(json),
           dataType : 'json',
           cache : false,
           timeout : 600000,
           success : function(data) {
//            var html = '';
//            var len = data.length;
//            html += '<option value="0"></option>';
//            for (var i = 0; i < len; i++) {
//             html += '<option value="' + data[i].id + '">'
//               + data[i].name
//               + '</option>';
//            }
//            html += '</option>';
//            $('#cityId').html(html);
           },
           error : function(e) {
            console.log("Update dlete " + JSON.stringify(e));
           }
          });

    $(".first-data-tr").remove();
    $(".helloMyTest-second").remove();

    if (stompClient !== null) {
        stompClient.send("/app/history", {}, 0);
        console.log("Delete All " + stompClient);
    }

}
