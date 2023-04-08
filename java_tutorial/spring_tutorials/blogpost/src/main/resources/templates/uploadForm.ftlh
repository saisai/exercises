<#include "header.ftlh">
<main>
  <div class="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center bg-body-tertiary">

    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file" /><br/><br/>
        <input type="submit" value="Submit" />
    </form>

  </div>
</main>
<#include "footer.ftlh">