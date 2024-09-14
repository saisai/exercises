import React from 'react';
import { Link } from 'react-router-dom';
import SignIn from './components/SignIn'
import SignUp from './components/SignUp';
import SignInSide from './components/SignInSide'
import StickyFooter from './components/StickyFooter'
import Album from './components/Album';
import Pricing from './components/Pricing';
import Checkout from './components/checkout/Checkout';
import Blog from './components/blog/Blog';
import Dashboard from './components/dashboard/Dashboard';

function SingInApp() {
  return (
    <div >
      <Dashboard />
    </div>
	);
}

export default SingInApp;