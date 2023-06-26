import React from 'react';

import PropTypes from 'prop-types';

import Footer from './Footer';
import Header from './Header';

const Layout = ({ children }) => (
  <div>
    <Header />
    <div className="pt-20">
      <main>{children}</main>
    </div>
    <Footer />
  </div>
);

Layout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default Layout;
