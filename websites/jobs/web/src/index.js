import React from 'react';
import ReactDOM from 'react-dom/client';

import {
  createRoutesFromElements,
  createBrowserRouter,
  Route,
  RouterProvider
} from "react-router-dom";

import Main, {
  loader as contactLoader,
} from './components/th/Main';
import JobThai from './components/th/JobThai';
import ThJobsDb from './components/th/ThJobsDb';

import ErrorPage from './components/th/error-page';
import Apply from './components/th/apply';
import { ShowModal } from './components/th/utils';
import EditApply from './components/th/edit-apply';

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route
      path="/"
      element={<Main />}
      loader={contactLoader}
      errorElement={<ErrorPage />}
    >
      <Route path="/*" element={<ErrorPage />} />
      <Route index element={<ThJobsDb />} />
      <Route
          path="jobsdb"
          element={<ThJobsDb />}       
          loader={contactLoader}    
        />
      <Route
          path="jobthai"
          element={<JobThai />}       
          loader={contactLoader}   
        />
      <Route
          path="apply"
          element={<Apply />}       
          loader={contactLoader}             
        >
          <Route 
            path="img/:id"
            element={<EditApply />}
          />
        </Route> 
    </Route>   
  )
);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
