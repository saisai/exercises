<#include "header.ftlh">
<main>
  <div class="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center bg-body-tertiary">

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