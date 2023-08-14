<#import "/spring.ftl" as spring />
<#include "header.ftlh">
<script>
$(function(){
    disconnect();
    $("a#mypopup").on("click", function(){
        $('div.popup').show();
        connect();
        return false;
    });

    $("button.close").on("click", function(event){
      $('div.popup').hide();
      console.log("mydata length" + mydata.length);
      mydata = [];
      console.log("after mydata length" + mydata.length);
      $('tr.helloMyTest-second').remove();
      disconnect();
     });
});
</script>
<style>

.center_popup{
  display:table;
  margin: 10px auto;
  overflow: scroll !important;
}

.mypopup-data-display {
  border: 1px solid #fefefe;
  color: #666;
}

table.first-table td {
  padding: 3px;
  font-weight: bold;
}

.popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 9999;
  background-color: rgba(0, 0, 0, .3);
}
.popup .inner {
  background: #fff;
  border: 1px solid #ccc;
  width: 100%;
  height: 100%;
  position: fixed;
}
.popup .inner button {
  position: fixed;
  padding: 2px 8px;
  right: 20px;
  top: 15px;
  background-color: #EEE;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
}
.popup .mypopup-banner {
  position:fixed;
  color: #fff;
  left: 40%;
  font-weight: bold;
  font-size: 20px;
  line-height: 65px;
}

.mypopup-header {
  background: #d54ccf;
  widht:100%;
  height: 40px;
  line-height:40px;
  font-weight:bold;
  padding-left: 30px;
  color: #000000;
}

</style>
<main>

  <div id="main-content" class="container" style="padding-top: 10px;">
      <div class="row">
          <div class="popup" style="display: none;">
                <div style="background:#6528e0; height: 65px;"><div style="float:left;"><img style="height:65px; line-height: 65px;"></div><div class="mypopup-banner">Test</div></div>
                <div class="inner">
                  <div style="display: block;">
                  <div class="mypopup-header">Test 2</div>
                  <div style="height: 250px;width: 100%;">
                    <div style="padding-left: 30px;padding-top:15px;">
                      <table class="my-realtime-table-first" style="width: 100%">
                        <thead></thead>
                        <tbody></tbody>
                      </table>
                    </div>
                  </div>
                  <div class="mypopup-header">Test 3</div>
                    <div style="padding-left: 30px;padding-top:15px; height: 300px; overflow-y: scroll;">
                      <table class="myrealtime-second" style="width: 100%">
                        <thead></thead>
                        <tbody></tbody>
                      </table>
                    </div>
                  </div>
                  <button class="close" title="Close">X</button>
                </div>
              </div>
      </div>
  </div>

</main>
<#include "footer.ftlh">
