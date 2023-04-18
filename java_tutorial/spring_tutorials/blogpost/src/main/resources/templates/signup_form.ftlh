<#include "header.ftlh">
<main>
  <div class="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center bg-body-tertiary">

   <form action="/process_register" method="post">

       <div class="row mb-3">
         <label for="inputEmail3" class="col-sm-2 col-form-label">Email</label>
         <div class="col-sm-10">
           <input type="text" class="form-control" id="inputEmail3" name="email"  >
         </div>
       </div>

       <div class="row mb-3">
         <label for="inputPassword3" class="col-sm-2 col-form-label">Password</label>
         <div class="col-sm-10">
           <input type="password" class="form-control" id="inputPassword3" name="password" >
         </div>
       </div>

       <div class="row mb-3">
         <label for="inputPassword3" class="col-sm-2 col-form-label">First Name</label>
         <div class="col-sm-10">
           <input type="text" class="form-control" id="inputPassword3" name="firstName" >
         </div>
       </div>

       <div class="row mb-3">
         <label for="inputPassword3" class="col-sm-2 col-form-label">Last Name</label>
         <div class="col-sm-10">
           <input type="text" class="form-control" id="inputPassword3" name="lastName" >
         </div>
       </div>


       <button type="submit" class="btn btn-primary">Sign Up</button>
     </form>



  </div>
 </main>

 <#include "footer.ftlh">
