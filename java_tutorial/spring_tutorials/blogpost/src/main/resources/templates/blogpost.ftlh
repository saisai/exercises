<#include "header.ftlh">
<main>
  <div class="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center bg-body-tertiary">
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@mdo">Add</button>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">New message</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="recipient-name" class="col-form-label">Title:</label>
                <input type="text" name="title" class="form-control" id="recipient-name">
              </div>
              <div class="mb-3">
                  <label for="recipient-name" class="col-form-label">Link:</label>
                  <input type="text" name="link" class="form-control" id="recipient-name">
              </div>
              <div class="mb-3">
                <label for="message-text" class="col-form-label">Description:</label>
                <textarea class="form-control" name="description" id="message-text"></textarea>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" id="submit">Send message</button>
          </div>
        </div>
      </div>
    </div>

    <table  class="table table-hover">
              <tr>
                  <th>Id</th>
                  <th>Title</th>
                  <th>Description</th>
                  <th >Created At</th>
                  <th colspan="2">&nbsp;</th>
              </tr>

              <#list blogPosts.page.content as blogpost>
                  <tr>
                      <td>${blogpost.id}</td>
                      <td>${blogpost.title}</td>
                      <td>${blogpost.description}</td>
                      <td>${blogpost.createdAt}</td>
                      <td><a class="btn btn-primary" href="/blogpost/${blogpost.id}">Delete</a></td>
                      <td><a class="btn btn-primary" href="/blogpost/update/${blogpost.id}">Update</a></td>
                  </tr>
              </#list>
          </table>




           <!-- start -->
           <div class="panel-footer">
                       <div class="row">


                           <div class="col col-xs-2">
                               Total items: ${blogPosts.page.totalElements}- item ${(blogPosts.page.number )*blogPosts.page.size +1 } -
                               ${(blogPosts.page.number )*blogPosts.page.size +blogPosts.page.numberOfElements  }
                           </div>
                           <div class="col col-xs-10">
                                               <nav aria-label="Page navigation" class="paging">
                                                   <#if (blogPosts.page.totalPages> 1)>
                                                       <ul class="pagination">

                                                           <li class="page-item ${(blogPosts.paging.isPrevEnabled())?string('' , 'disabled')}">
                                                               <a class="page-link" href="/blogpost/?pageNumber=${blogPosts.paging.pageNumber - 1}"
                                                                  tabindex="-1">Previous</a>
                                                           </li>

                                                           <#list blogPosts.paging.getItems() as item>
                                                               <#if (item.pageItemType.name() == 'PAGE')>
                                                                   <li class="page-item ${(item.index == blogPosts.paging.pageNumber)?string('active' , '')}">
                                                                       <a class="page-link" href="/blogpost/?pageNumber=${item.index}">${item.index}</a>
                                                                   </li>
                                                               </#if>
                                                               <#if (item.pageItemType.name() == 'DOTS')>
                                                                   <li class="page-item disabled">
                                                                       <a class="page-link" href="#">...</a>
                                                                   </li>
                                                               </#if>
                                                           </#list>


                                                           <li class="page-item ${(blogPosts.paging.isNextEnabled())?string('' , 'disabled')}">
                                                               <a class="page-link" href="/blogpost/?pageNumber=${blogPosts.paging.pageNumber + 1}"
                                                               >Next</a>
                                                           </li>

                                                       </ul>
                                                   </#if>
                                               </nav>
                                           </div>


                       </div>
                   </div>

           <!-- end -->

  </div>
</main>
<#include "footer.ftlh">
<script>
/*
var exampleModal = document.getElementById('exampleModal')
exampleModal.addEventListener('show.bs.modal', function (event) {
    alert("test");
  // Button that triggered the modal
  var button = event.relatedTarget
  // Extract info from data-bs-* attributes
  var recipient = button.getAttribute('data-bs-whatever')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  var modalTitle = exampleModal.querySelector('.modal-title')
  var modalBodyInput = exampleModal.querySelector('.modal-body input')

  modalTitle.textContent = 'New message to ' + recipient
  modalBodyInput.value = recipient
})
*/

$(document).ready(function() {
    $("#submit").on("click", function() {
      	$.ajax({
            type: 'POST',
            url: '/blogpost/ajax',
            data: {
                title: $('input[name="title"]').val(),
                link: $('input[name="link"]').val(),
                description: $('textarea[name="description"]').val()
            },
            success: function(text) {
                $(".btn-close").trigger("click");
                location.reload();
                //$(document.body).text('Response: ' + text);
            },
            error: function (jqXHR) {
                alert('Error: ' + jqXHR.status);
                //$(document.body).text('Error: ' + jqXHR.status);
            }
        });
    });

});

</script>