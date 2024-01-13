import React from 'react';
import ReactDOM from 'react-dom/client';
import { createRoot } from "react-dom/client";
import App from './App';

import {
  createRoutesFromElements,
  createBrowserRouter,
  Route,
  RouterProvider
} from "react-router-dom";

import Main from './components/th/Main';
import JobThai from './components/th/JobThai';
import ThJobsDb from './components/th/ThJobsDb';

import ErrorPage from './components/th/error-page';

// createRoot(document.getElementById("root")).render(
//   <React.StrictMode>
//     <BrowserRouter>
//       <Route
//         path="/"
//         element={<Main />}
//       >
//         <Route path="jobthai">
//           <Route
//             index
//             element={<JobThai />}
//           />
//           <Route
//             path="jobsdb"
//             element={<ThJobsDb />}
//           />
//         </Route>
//         <Route index element={<ThJobsDb />} />
//       </Route>
//       <Route path="*" element={<div>Not found</div>} />
//     </BrowserRouter>
//   </React.StrictMode>,
// );


// const router = createBrowserRouter([
//   {
//     path: "/",
//     element: <Main />,
//     errorElement: <ErrorPage />,
//     children: [
     
      

//         { index: true, element: <ThJobsDb />, },
//         {
//           path: "jobthai",
//           element: <JobThai />,
//         },
//         {
//           path: "jobsdb",
//           element: <ThJobsDb />,
//         },         

  
//     ],
//   },
// ]);

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route
      path="/"
      element={<Main />}
      errorElement={<ErrorPage />}
    >
      <Route path="/*" element={<ErrorPage />} />
      <Route index element={<ThJobsDb />} />
      <Route
          path="jobsdb"
          element={<ThJobsDb />}          
        />
      <Route
          path="jobthai"
          element={<JobThai />}          
        />
    </Route>   
  )
);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);


