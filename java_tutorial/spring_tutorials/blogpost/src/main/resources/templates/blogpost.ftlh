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

              <#list blogPosts as blogpost>
                  <tr>
                      <td>${blogpost.id}</td>
                      <td>${blogpost.title}</td>
                      <td>${blogpost.description}</td>
                      <td>${blogpost.createdAt}</td>
                      <td><a class="btn btn-primary" href="blogpost/${blogpost.id}">Delete</a></td>
                      <td><a class="btn btn-primary" href="blogpost/update/${blogpost.id}">Update</a></td>
                  </tr>
              </#list>
          </table>
  </div>
</main>
<#include "footer.ftlh">