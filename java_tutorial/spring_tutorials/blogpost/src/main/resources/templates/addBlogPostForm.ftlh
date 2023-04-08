<#import "/spring.ftl" as spring />
<#include "header.ftlh">
<main>
  <div class="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center bg-body-tertiary">
  <#if blogPost??>
     <@spring.formInput "blogPost.title"/> <@spring.showErrors "<br>"/> <br /><br />
     <@spring.formInput "blogPost.link"/> <@spring.showErrors "<br>"/>
  <#else>

<form action="/blogpost/add" method="post">

    <div class="row mb-3">
      <label for="inputEmail3" class="col-sm-2 col-form-label">Title</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="inputEmail3" name="title" >
      </div>
    </div>

    <div class="row mb-3">
      <label for="inputPassword3" class="col-sm-2 col-form-label">Link</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="inputPassword3" name="link">
      </div>
    </div>

    <div class="row mb-3">
          <label for="inputPassword3" class="col-sm-2 col-form-label">Description</label>
          <div class="col-sm-10">
            <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" name="description"></textarea>
          </div>
    </div>
    <button type="submit" class="btn btn-primary">Add</button>
  </form>
 </#if>
  </div>
</main>
<#include "footer.ftlh">